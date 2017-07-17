"""
Module to display movie object, attributes and instances
"""
import webbrowser


class Movie():
    """
    This is a movie class which takes the input parameters
    (movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating)
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, storyline, image_url, youtube_url, rating):
        """
        This is the initialization method
        """
        self.title = title
        self.storyline = storyline
        self.image_url = image_url
        self.youtube_url = youtube_url
        self.rating = movie_rating
  
    def show_trailer(self):
        """
        This method will show the trailer of the selected movie on the browser
        """
