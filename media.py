import webbrowser
#Class Movie
class Movie():
	"""Documentation"""


	VALID_RATINGS=["G","PG","PG-13","R"]
	#constructor
	def __init__(udacity,movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating):
		#instance variables
		udacity.title=movie_title
		udacity.storyline=movie_storyline
		udacity.poster_image_url=poster_image
		udacity.trailer_youtube_url=trailer_youtube
		udacity.rating=movie_rating
	#Instance method
	def show_trailer(udacity):
		webbrowser.open(udacity.trailer_youtube_url)


