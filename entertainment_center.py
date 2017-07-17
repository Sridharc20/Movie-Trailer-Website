import media
import fresh_tomatoes

# instance of a movie class
toy_story = media.Movie(
    "Toy Story", 
    "A story of a boy and his toys that comes to life",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc", 
    "G")

avatar = media.Movie(
    "Avatar", 
    "A marine on an alien planet", 
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # noqa 
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 
    "G")
# print "avatar.storyline:",avatar.storyline
ice_age = media.Movie(
    "Ice Age: Collision Course", 
    " Scrat keeps struggling to control the alien ship until it crashes on Mars, destroying all life on the planet.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Ice_age_collision_course.jpg/220px-Ice_age_collision_course.jpg",  # noqa
    "https://www.youtube.com/watch?v=s6kGpBTZyr0", 
    "G")
print "please enter the movie details:"
print "Enter Movie Name:"
movie_name = raw_input()
print "Enter Movie story line"
movie_story_line = raw_input()
print "Enter movie poster image location"
movie_poster = raw_input()
print "Enter movie trailer youtube link"
movie_youtube_link = raw_input()
print "Can you please rate the movie", media.Movie.VALID_RATINGS
movie_rating = raw_input()
print "Thanks for sharing the movie details, please verify in the browser"
m = media.Movie(
    movie_name, 
    movie_story_line, 
    movie_poster, 
    movie_youtube_link, 
    movie_rating)
movies = [toy_story, avatar, ice_age, m]
fresh_tomatoes.open_movies_page(movies)
