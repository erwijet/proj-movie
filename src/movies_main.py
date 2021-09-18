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

    collection.top('movie', 3, 1994, 1995)
    collection.top('movie', 10, 1990, 1995)
    collection.top('movie', 20, 2010, 2010)
    collection.top('movie', 10, 2015, 2019)
    collection.top('movie', 1, 2000, 2020)
    collection.top('videoGame', 5, 2010, 2020)
    collection.top('tvSeries', 4, 2000, 2019)


if __name__ == '__main__':
    main(argv)
