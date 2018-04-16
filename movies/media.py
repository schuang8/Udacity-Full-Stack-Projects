"""@package docstring
Documentation for the media module
"""

import webbrowser


class Movie():
    """ Movie class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Default constructor for Movie class """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ show_trailer method opens the youtube link
            stored in trailer_youtube_url
        """
        webbrowser.open(self.trailer_youtube_url)
