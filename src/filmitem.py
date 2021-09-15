from dataclasses import dataclass


@dataclass(frozen=True)
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
    def factory(tsv_parsable: str):
        """
        python does not allow class constructor overloading,
        so we implement a static factory method to handle the parsing
        of text and functional creation of instances of self, without
        modifying the contruction added from the @dataclass decorator

        :return: an instance of FilmItem, who's values have been populated
        from tsv_parsable, a tab-seperated string containging the values to be
        parsed
        """
        return FilmItem(*tsv_parsable.split('\t'))
