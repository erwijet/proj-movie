from sys import argv
from queries import QueryableFilmCollection

from util import *


def main(argv):

    if len(argv) > 1:
        _, size = argv
    else:
        size = 'large'

    collection = QueryableFilmCollection(
        'data/' + size + '.basics.tsv',
        'data/' + size + '.ratings.tsv')

    cmd = ''

    while cmd != '\\q':
        cmd, *args = input('query expresion # ').split(' ')

        if cmd == 'CONTAINS':
            collection.contains(*args)
        if cmd == 'LOOKUP':
            collection.lookup(*args)
        if cmd == 'MOST_VOTES':
            collection.most_votes(*args)
        if cmd == 'RUNTIME':
            collection.runtime(*args)
        if cmd == 'TOP':
            collection.top(*args)
        if cmd == 'YEAR_AND_GENRE':
            collection.year_and_genre(*args)
        if cmd == '\\?':
            with open('help.txt') as f:
                print(''.join([l for l in f]))
        else:
            print()  # newline


if __name__ == '__main__':
    main(argv)
