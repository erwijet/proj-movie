from sys import argv
from enum import Enum
from queries import QueryableFilmCollection

from util import *


class DataSetType(Enum):
    SMALL = 'small'
    LARGE = 'large'


def main(argv):
    collection = QueryableFilmCollection(
        'C:/Users/17198/rit/projects/csapx/project-1-movies-erwijet/data/small.basics.tsv', 'C:/Users/17198/rit/projects/csapx/project-1-movies-erwijet/data/small.ratings.tsv')

    collection.year_and_genre('movie', 1995, 'Action')


if __name__ == '__main__':
    main(argv)
