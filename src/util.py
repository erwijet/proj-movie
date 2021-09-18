from dataclasses import dataclass
from time import time


@dataclass
class FilmItem:
    tconst: str
    title_type: str
    primary_title: str
    original_title: str
    is_adult: bool
    start_year: int
    end_year: int
    runtime_minutes: int
    genres: tuple

    def __str__(self) -> str:
        return 'MOVIE: Identifier: {0}, Title: {1}, Type: {2}, Year: {3}, Runtime: {4}, Genres: {5}'.format(
            self.tconst, self.primary_title, self.title_type, self.start_year, self.runtime_minutes, ', '.join(self.genres))

    @staticmethod
    def from_tsv(tsv_parsable: str):
        """
        python does not allow class constructor overloading,
        so we implement a static factory method to handle the parsing
        of text and functional creation of instances of self, without
        modifying the contruction added from the @dataclass decorator

        :return: an instance of FilmItem, who's values have been populated
        from tsv_parsable, a tab-seperated string containging the values to be
        parsed
        """

        # inital parse of props
        props = tsv_parsable.split('\t')

        # replace str-binary value with boolean values for prop
        # "is_adult" at idx 4
        PROP_is_adult_IDX = 4
        props[PROP_is_adult_IDX] = props[PROP_is_adult_IDX] == '1'

        # replace any occurances of '\\n' with None
        props = [prop if prop != '\\N' else None for prop in props]

        # cast prop idxs 5-7 to integers (start_year, end_year, runtime_min)
        props = [int(props[i]) if i in range(5, 8) and props[i]
                 is not None else props[i] for i in range(len(props))]

        # construct tuple for prop "genre" at idx 8
        PROP_GENRE_IDX = 8
        props[PROP_GENRE_IDX] = tuple(props[PROP_GENRE_IDX].split(','))

        return FilmItem(*props)


@dataclass
class FilmRating:
    tconst: str
    rating: float
    num_ratings: int

    def __str__(self) -> str:
        return 'RATING: Identifier: {0}, Rating: {1}, Votes: {2}'.format(self.tconst, self.rating, self.num_ratings)

    @staticmethod
    def from_tsv(tsv_parsable: str):
        """
        python does not allow class constructor overloading,
        so we implement a static factory method to handle the parsing
        of text and functional creation of instances of self, without
        modifying the contruction added from the @dataclass decorator

        :return: an instance of FilmRating, who's values have been populated
        from tsv_parsable, a tab-seperated string containging the values to be
        parsed
        """

        props = tsv_parsable.split('\t')

        # convert prop at idx 1 (rating) to float

        props[1] = float(props[1])

        # convert prop at idx 2 (num_ratings) to int

        props[2] = int(props[2])

        return FilmRating(*props)


@dataclass
class Film:
    """
    bind a given instance of FilmItem to its corresponding
    instance of FilmRating
    """

    film_item: FilmItem
    film_rating: FilmRating


def timed_function(func):
    """
    timed_function function decorator

    when applied, the specified function's runtime
    will be measured and printed following the excution of
    the function, func

    :return: the function, func, wrapped with the timing
    functionality
    """
    def wrapped(*args):
        t0 = time()
        func(*args)
        t = time()

        print('elapsed time (s): ' + str((t - t0)))

    return wrapped
