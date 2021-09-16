from dataclasses import dataclass


@dataclass
class FilmItem:
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    isAdult: bool
    startYear: int
    endYear: int
    runtimeMinutes: int
    genres: tuple(str)

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
        # "isAdult" at idx 4
        PROP_ISADULT_IDX = 4
        props[PROP_ISADULT_IDX] = props[PROP_ISADULT_IDX] == '1'

        # replace any occurances of '\\n' with None
        props = [prop if prop != '\\N' else None for prop in props]

        # construct tuple for prop "genre" at idx 8
        PROP_GENRE_IDX = 8
        props[PROP_GENRE_IDX] = tuple(props[PROP_GENRE_IDX].split(','))

        return FilmItem(*props)


@dataclass
class FilmRating:
    tconst: str
    rating: float
    num_ratings: int

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
        return FilmRating(*props)


@dataclass(frozen=True)
class Film:
    """
    bind a given instance of FilmItem to its corresponding
    instance of FilmRating
    """

    film_item: FilmItem
    film_rating: FilmRating
