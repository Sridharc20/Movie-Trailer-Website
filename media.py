"""
Module to display movie object, attributes and instances
"""

import webbrowser


class Movie():
	"""This is a movie class which takes the input parameters (movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating) """


	VALID_RATINGS = ["G","PG","PG-13","R"]
	#constructor
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating):
		#instance variables
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = movie_rating
	#Instance method
	def show_trailer(self):
		""" This method will show the trailer of the selected movie"""
		webbrowser.open(self.trailer_youtube_url)


