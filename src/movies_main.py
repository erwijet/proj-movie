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

    collection.most_votes('movie', 5)
    collection.most_votes('tvSpecial', 5)
    collection.most_votes('movie', 2)
    collection.most_votes('videoGame', 1)
    collection.most_votes('tvSeries', 5)


if __name__ == '__main__':
    main(argv)
