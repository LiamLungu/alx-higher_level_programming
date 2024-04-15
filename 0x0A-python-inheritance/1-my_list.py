#!/usr/bin/python3
"""My List class Documentation"""


class MyList(list):
    """MyList class inherits from the python class list"""

    def print_sorted(self):
        """Prints the current instance of the class MyList sorted."""
        print(sorted(self))
