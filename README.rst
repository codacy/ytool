======
YTool
======

A simple tool to set values in yaml files preserving format and comments.
This command line tool is based on `ruamel.yaml <https://pypi.org/project/ruamel.yaml>`__

^^^^^^^^^^^^^^^^^^^^^^^^
Install:
^^^^^^^^^^^^^^^^^^^^^^^^

Ytool can be installed simply by running:

.. code-block:: bash

    $ pip install ytool


^^^^^^^^^^^^^^^^^^^^^^^^
Example:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ ytool -f some.yaml -s some.string.key value -d float_key 9.9  -i int.key.path 10


The output format can be specified to match an existing file:


.. code-block:: bash

    $ ytool -f some.yaml -s some.string.key value \
        --format-width 150 \
        --format-ident "{mapping: 2, sequence: 4, offset: 2}"


^^^^^^^^^^^^^^^^^^^^^^^^
Help:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ usage: ytool [-h] --file FILE [--set-string path value] [--set-int path value]
             [--set-float path value] [--output OUTPUT] [--edit-file] [--verbose]
             [--format-explicit-start] [--format-width WIDTH] [--format-indent INDENT]

    Set values in yaml file preserving format and comments.

    optional arguments:
      -h, --help            show this help message and exit
      --file FILE, -f FILE  Name of the chart file to change
      --set-string path value, -s path value
                            Set string value for path
      --set-int path value, -i path value
                            Set integer value for path
      --set-float path value, -d path value
                            Set float value for path
      --output OUTPUT, -o OUTPUT
                            Name of output file
      --edit-file, -e       Edit input file directly
      --verbose, -v         Print debug information to stdout
      --format-explicit-start, -x
                            Set explicit start
      --format-width WIDTH, -w WIDTH
                            Set max width for output
      --format-indent INDENT, -m INDENT
                            Set indent format, eg. "{mapping: 2, sequence: 4, offset: 2}"


---------------
What is Codacy?
---------------

`Codacy <https://www.codacy.com/>`__ is an Automated Code Review Tool
that monitors your technical debt, helps you improve your code quality,
teaches best practices to your developers, and helps you save time in
Code Reviews.

^^^^^^^^^^^^^^^^^^^^^^^^
Among Codacy’s features:
^^^^^^^^^^^^^^^^^^^^^^^^

-  Identify new Static Analysis issues
-  Commit and Pull Request Analysis with GitHub, BitBucket/Stash, GitLab
   (and also direct git repositories)
-  Auto-comments on Commits and Pull Requests
-  Integrations with Slack, HipChat, Jira, YouTrack
-  Track issues in Code Style, Security, Error Proneness, Performance,
   Unused Code and other categories

Codacy also helps keep track of Code Coverage, Code Duplication, and
Code Complexity.

Codacy supports PHP, Python, Ruby, Java, JavaScript, and Scala, among
others.

^^^^^^^^^^^^^^^^^^^^
Free for Open Source
^^^^^^^^^^^^^^^^^^^^

Codacy is free for Open Source projects.
