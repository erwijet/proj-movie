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
    genres: str

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

        props = tsv_parsable.split('\t')

        # boolean values are given as binary strings;
        #   fix them here
        props[4] = props[4] == '1'

        # replace any occurances of '\\n' with None
        props = [prop if prop != '\\N' else None for prop in props]

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
