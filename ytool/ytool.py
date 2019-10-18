from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO


class YTool(YAML):
    """
    YTool is a simple extension of ruamel.yaml useful for changing
    values when using paths to refer to nested objects.
    """

    def get_leaf_and_key(self, data, path, delimiter="."):
        """
        Find leaf in the yaml tree containing a key extracted from a path
        For instance, when the yaml data is

        ```
        this:
            nested:
                object1: value1
                object2: value2
        ```
        and this function is called with path=`this.nested.object1` it returns
        `OrderedDict([(object1, value1)`, (object2, value2)]) and `object1`


        args:
            data (OrderedDict): ruamel parsed yaml data
            path (str): path to key to search for
            delimiter (str): path delimiter. Default is '.'

        returns:
            leaf, key (OrderedDict, str): the `leaf` in the yaml tree containing `key`

        raises:
            KeyError: if any of the elements of the path is not a valid key in the corresponding yaml leaf
        """
        keys = path.split(delimiter)

        # find the innermost dict holding the key we want to change
        leaf = data
        for key in keys[:-1]:
            if key in leaf:
                leaf = leaf[key]
            else:
                raise KeyError(f"Key '{key}' not found in '{leaf}'")

        # get last key, checking if it is valid
        last_key = keys[-1]
        if last_key in leaf:
            return leaf, last_key
        else:
            raise KeyError(f"Key '{last_key}' not found in '{leaf}'")

    def set_path_by_value(self, data, path, searchKVPair, replaceKVPair):
        """
                Find leaf in the yaml tree containing a key-value pair extracted from a path
                For instance, when the yaml data is

                ```
                this:
                    nested:
                        object1: value1
                        object2: value2

                this:
                    nested:
                    - key1: value1
                      key2: value2
                    - key1: value3
                      key2: value4
                ```
                and this function is called with path=`this.nested (key1, value3) (key2, value4)` it returns
                `OrderedDict([(key1, value3)`, (key2, value4)]) and `key2`


                args:
                    data (OrderedDict): ruamel parsed yaml data
                    path (str): path to key to search for
                    searchKVPair (tuple): the key and value pair for searching for an element
                    replaceKVPair (tuple): the key and value pair with new values to replace on the element

                returns:
                    leaf, key (OrderedDict, str): the `leaf` in the yaml tree containing `key` if found.
                    tree, key (OrderedDict, str): if the `leaf` could not be found.
                """
        tree, key = self.get_leaf_and_key(data, path)
        for leaf in tree[key]:
            if leaf[searchKVPair[0]] == searchKVPair[1]:
                leaf[replaceKVPair[0]] = replaceKVPair[1]
                return leaf, replaceKVPair[0]

        return tree, key

    def set_path_value(self, data, path, value, delimiter="."):
        """
        Set a value of `data` for a given path

        args:
            data (OrderedDict): ruamel parsed yaml data
            path (str): path to the key to change
            value (Any): value to assign to the key
            delimiter (str): path delimiter. Default is '.'
        """
        leaf, key = self.get_leaf_and_key(data, path, delimiter)
        leaf[key] = value

    def dump(self, data, stream=None, **kw):
        """
        Wrapper around the ruamel dump function which writes to a
        string stream if no stream is provided. Useful for testing.
        Taken from the ruamel documentation:
            https://yaml.readthedocs.io/en/latest/example.html#output-of-dump-as-a-string

        args:
            data (OrderedDict): ruamel parsed yaml data
            stream (Union[Path, StreamType]): stream where to dump the data
            **kw (Any=Any): ruamel dump flags and respective values
        """
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()

        YAML.dump(self, data, stream, **kw)

        if inefficient:
            return stream.getvalue()
