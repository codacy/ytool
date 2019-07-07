import io
import sys
import pytest

from collections import OrderedDict
from ..ytool import YTool
#from .ytool.ytool import ytool

TEST_YAML = """\
apiVersion: v1
appVersion: "1.0"
description: this a typical k8s chart file
name: rudder
#This is a comment
version: 0.1.0

#There is some space above this line
some:
  not_so_nested: "is it"
  very:
    nested:
      element: "value"
      another_one: "another_value"
"""

def test_get_leaf_and_key_for_nested_element():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    leaf, key = parser.get_leaf_and_key(data, "some.very.nested.another_one")
    assert leaf == OrderedDict([('element', 'value'), ('another_one', 'another_value')])
    assert key == "another_one"


def test_get_leaf_and_key_for_non_nested_element():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    leaf, key = parser.get_leaf_and_key(data, "name")
    assert key == "name"
    assert leaf == OrderedDict([
        ('apiVersion', 'v1'),
        ('appVersion', '1.0'),
        ('description', 'this a typical k8s chart file'),
        ('name', 'rudder'),
        ('version', '0.1.0'),
        ('some', OrderedDict([
            ('not_so_nested', 'is it'),
            ('very', OrderedDict([
                ('nested', OrderedDict([
                    ('element', 'value'),
                    ('another_one', 'another_value')]))]))
        ]))
    ])


def test_get_leaf_and_key_exception_for_wrong_plain_key():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    with pytest.raises(KeyError):
        parser.get_leaf_and_key(data, "not_a_key")


def test_get_leaf_and_key_exception_for_wrong_nested_key():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    with pytest.raises(KeyError):
        parser.get_leaf_and_key(data, "some.very.wrong.element")


def test_get_leaf_and_key_exception_for_wrong_final_key():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    with pytest.raises(KeyError):
        parser.get_leaf_and_key(data, "some.very.nested.non_existing_element")


def test_non_nested_value_replacement():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    test_value = 9.9
    parser.set_path_value(data, "version", test_value)
    assert data["version"] == test_value


def test_nested_value_replacement():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    test_value = "changed"
    parser.set_path_value(data, "some.very.nested.element", test_value)
    assert data["some"]["very"]["nested"]["element"] == test_value


def test_multiple_value_replacement():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    test_value1 = 9.9
    test_value2 = "changed"

    parser.set_path_value(data, "version", test_value1)
    parser.set_path_value(data, "some.very.nested.element", test_value2)
    assert data["version"] == test_value1
    assert data["some"]["very"]["nested"]["element"] == test_value2


def test_format_is_preserved():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    assert parser.dump(data) == TEST_YAML


def test_format_is_preserved_when_values_change():
    parser = YTool()
    parser.preserve_quotes = True
    data = parser.load(TEST_YAML)

    test_value = "changed"
    original_value = "value"
    test_string = '      element: "value"'

    parser.set_path_value(data, "some.very.nested.element", test_value)

    diff = [(x1,x2) for (x1,x2) in zip(TEST_YAML.split('\n'), parser.dump(data).split('\n')) if x1 != x2]
    assert len(diff) == 1
    assert diff[0][0] == test_string
    assert diff[0][1] == test_string.replace(original_value, test_value, 1)
