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

    cmd = ''  # scope

    VALID_QUERIES = ['CONTAINS', 'LOOKUP', 'MOST_VOTES',
                     'RUNTIME', 'TOP', 'YEAR_AND_GENRE']

    while cmd != '\\q':
        cmd, *args = input('query expresion # ').split(' ')

        if cmd not in VALID_QUERIES and cmd != '\\?':
            print()     # newline
            continue    # process nexy command

        # map cmd to the collection attribute function
        # with the same name. Then, invoke that attribute function
        # and pass the args specified to it

        if cmd in VALID_QUERIES:
            getattr(collection, cmd.lower())(*args)
            continue  # process next command

        if cmd == '\\?':
            with open('help.txt') as f:
                content = ''.join([line for line in f])
                print(content)


if __name__ == '__main__':
    main(argv)
