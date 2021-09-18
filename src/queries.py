from time import time
from util import *


class QueryableFilmCollection:
    films: dict

    def __init__(self, tsv_item_path, tsv_ratings_path):
        self.films = {}

        # load ratings first into dictionary
        with open(tsv_ratings_path) as ratings_file:
            file_iter = iter(ratings_file)
            # explicity consume and discard the first line (headers)
            next(file_iter)

            for line in file_iter:
                film_rating = FilmRating.from_tsv(line.strip('\n'))
                self.films[film_rating.tconst] = film_rating

        # then load film items and update dictionary

        with open(tsv_item_path) as item_file:
            file_iter = iter(item_file)
            # explicity consume and discard the first line (headers)
            next(file_iter)

            for line in item_file:
                film_item = FilmItem.from_tsv(line.strip('\n'))
                self.films[film_item.tconst] = Film(
                    film_item, self.films.get(film_item.tconst))

    @timed_function
    def lookup(self, tconst: str) -> None:
        print('Processing LOOKUP ', tconst)

        results = self.films.get(tconst)
        print('\t' + str(results.film_item) if results is not None and results.film_item is not
              None else '\tMovie not found!')
        print('\t' + str(results.film_rating)
              if results is not None and results.film_rating != None else '\tRating not found!')

    @timed_function
    def contains(self, title_type: str, words: str) -> None:
        print('Processing CONTAINS', title_type, words)

        results = list(filter(lambda film:
                              film.film_item.title_type == title_type and
                              words in film.film_item.primary_title, self.films.values()))
        for film in results:
            print('\t' + str(film.film_item))

        if len(results) == 0:
            print('\tNo match found!')

    @timed_function
    def year_and_genre(self, title_type: str, year: int, genre: str) -> None:
        print('Processing YEAR_AND_GENRE', title_type, year, genre)

        results = list(filter(lambda film:
                              film.film_item.title_type == title_type and
                              film.film_item.start_year == year and
                              genre in film.film_item.genres, self.films.values()))

        results.sort(key=lambda film: film.film_item.primary_title)

        for film in results:
            print('\t' + str(film.film_item))

        if len(results) == 0:
            print('\tNo match found!')

    @timed_function
    def runtime(self, title_type: str, min_minutes: int, max_minutes: int) -> None:
        print('Processing RUNTIME', title_type, min_minutes, max_minutes)

        results = list(filter(lambda film:
                              film.film_item.runtime_minutes is not None and
                              film.film_item.title_type == title_type and
                              film.film_item.runtime_minutes >= min_minutes and
                              film.film_item.runtime_minutes <= max_minutes, self.films.values()))

        results.sort(key=lambda film: film.film_item.primary_title)
        results.sort(
            key=lambda film: film.film_item.runtime_minutes, reverse=True)

        for film in results:
            print('\t' + str(film.film_item))

        if len(results) == 0:
            print('\tNo match found!')

    @timed_function
    def most_votes(self, title_type: str, num: int) -> None:
        print('Processing MOST_VOTES', title_type, num)

        sorted_films = sorted(filter(
            lambda film:
                film.film_rating is not None and
                film.film_item.title_type == title_type,
            self.films.values()),
            key=lambda film: film.film_rating.num_ratings, reverse=True)

        results = sorted_films[:num]  # take the top "num" results

        # now we sort by alpha and then by num votes again
        # we do this here to avoid sorting the entire contents of the
        # dictionary, and even though we are re-sorting by num votes,
        # assuming O(n) sort time, if len(results) is less than half
        # of the total films in the dictionary matching title_type,
        # this approach is still more efficient because (2 * j * O(n)) + O(n)
        # where j < 0.5 is will always be strictly smaller than O(n) * 2

        # </rant>

        results.sort(key=lambda film: film.film_item.primary_title)
        results.sort(
            key=lambda film: film.film_rating.num_ratings, reverse=True)

        for film in results:
            print('\t' + str(film.film_item))

        if len(results) == 0:
            print('\tNo match found!')

    @ timed_function
    def top(self, title_type: str, num: int, start_year: int, end_year: int) -> list[Film]:
        print('Processing TOP ', title_type, num, start_year, end_year)

        # select films matching title_type, exclude films
        # outside year range and also exclude any films with
        # less than 1000 ratings (as per project spec)
        filtered = list(filter(lambda film:
                               film.film_item is not None and
                               film.film_rating is not None and
                               film.film_item.title_type == title_type and
                               film.film_rating.num_ratings >= 1000 and
                               film.film_item.start_year >= start_year and
                               film.film_item.start_year <= end_year, self.films.values()))

        for year in range(start_year, end_year + 1):

            results = sorted(
                sorted(
                    sorted(
                        filter(lambda film: film.film_item.start_year ==
                               year, filtered),
                        key=lambda film: film.film_item.primary_title),
                    key=lambda film: film.film_rating.num_ratings, reverse=True),
                key=lambda film: film.film_rating.rating, reverse=True)[:num]

            print('\tYEAR: ' + str(year))

            i = 1
            for film in results:
                print('\t\t{0}. RATING: {1}, VOTES: {2}, MOVIE: {3}'.format(
                    i, film.film_rating.rating, film.film_rating.num_ratings, film.film_item))
                i += 1

            if len(results) == 0:
                print('\t\tNo match found!')
