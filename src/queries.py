from util import *


class QueryableFilmCollection:
    films: dict

    def __init__(self, tsv_item_path, tsv_ratings_path):
        self.films = {}

        # load ratings first into dictionary
        with open(tsv_ratings_path) as ratings_file:
            for line in ratings_file:
                film_rating = FilmRating.from_tsv(line)
                self.films[film_rating.tconst] = film_rating

        # the load ilm items and update dictionary

        with open(tsv_item_path) as item_file:
            for line in item_file:
                film_item = FilmItem.from_tsv(line)
                self.films[film_item.tconst] = Film(
                    film_item, self.films.get(film_item.tconst))

    def lookup(self, tconst: str):
        return self.films[tconst]

    def contains(self, title_type: str, words: str):
        pass

    def year_and_genre(self, title_type: str, year: int, genre: str):
        pass

    def runtime(self, title_type: str, min_minutes: int, max_minutes: int):
        pass

    def most_votes(self, title_type: str, num: int):
        pass

    def top(self, title_type: str, start_year: int, end_year: int):
        pass
