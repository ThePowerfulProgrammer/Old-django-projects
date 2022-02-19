from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()

key = '7d6216389a32b10277a26cdf348a9f68'
Eapi_request = 'https://api.themoviedb.org/3/movie/550?api_key=7d6216389a32b10277a26cdf348a9f68/discover/movie?sort_by=popularity.desc'

tmdb.api_key = key

tmdb.language = 'en'
tmdb.debug = True

