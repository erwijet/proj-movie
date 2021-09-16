from sys import argv
from enum import Enum
from queries import QueryableFilmCollection

from util import *


class DataSetType(Enum):
    SMALL = 'small'
    LARGE = 'large'


def main(argv):
    collection = QueryableFilmCollection(
        '../data/small.basics.tsv', '../data/small.ratings.tsv')

    print(collection)


if __name__ == '__main__':
    main(argv)
