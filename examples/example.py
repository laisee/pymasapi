if __name__ == '__main__' and __package__ is None:
    from os import path, sys

    # __file__ should be defined in this case
    PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    sys.path.append(PARENT_DIR)

from pymasapi.client import *
