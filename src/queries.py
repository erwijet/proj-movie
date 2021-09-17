from time import time
from util import *


class QueryableFilmCollection:
    films: dict

    def __init__(self, tsv_item_path, tsv_ratings_path):
        self.films = {}

        # load ratings first into dictionary
        with open(tsv_ratings_path) as ratings_file:
            for line in ratings_file:
                film_rating = FilmRating.from_tsv(line.strip('\n'))
                self.films[film_rating.tconst] = film_rating

        # then load film items and update dictionary

        with open(tsv_item_path) as item_file:
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

    @ timed_function
    def year_and_genre(self, title_type: str, year: int, genre: str) -> list[Film]:
        return list(filter(lambda film:
                           film.film_item.title_type == title_type and
                           film.film_item.start_year == year and
                           genre in film.film_item.genre), self.films.values())

    @ timed_function
    def runtime(self, title_type: str, min_minutes: int, max_minutes: int) -> list[Film]:
        return list(filter(lambda film:
                           film.film_item.title_type == title_type and
                           film.film_item.runtimeMinutes >= min_minutes and
                           film.film_item.runtimeMinutes <= max_minutes), self.films.values())

    @ timed_function
    def most_votes(self, title_type: str, num: int) -> list[Film]:
        return list(
            sorted(
                filter(
                    lambda film: film.film_item.title_type == title_type,
                    self.films.values()),
                key=lambda film: film.film_rating.num_votes))[:num]

    @ timed_function
    def top(self, title_type: str, num: int, start_year: int, end_year: int) -> list[Film]:

        # select films matching title_type, exclude films
        # outside year range and also exclude any films with
        # less than 1000 ratings (as per project spec)
        filtered = filter(lambda film:
                          film.film_item.title_type == title_type and
                          film.film_rating.num_ratings >= 1000 and
                          film.film_item.start_year >= start_year and
                          film.film_item.end_year <= end_year, self.films.values())

        return [sorted(filter(lambda film: film.film_item.start_year == year, filtered), key=lambda film: film.film_rating.rating)[:num]
                for year in range(start_year, end_year)]
