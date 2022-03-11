"""Welcome"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace
# pylint: disable=trailing-newlines
import os
import operator
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_movie_data(movie_id):
    """Takes movie_id and returns the title, tagline and genres"""
    BASE_URL = "https://api.themoviedb.org/3/movie/" + str(movie_id)

    params = {
        "api_key": os.getenv("tmdb_key"),
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    title = data["title"]

    tagline = data["tagline"]

    genres = data["genres"]
    new_genres = list(map(operator.itemgetter("name"), genres))
    final_genres = ", ".join(new_genres)

    poster_path = data["poster_path"]
    img_url = "https://image.tmdb.org/t/p/w500" + str(poster_path)

    return title, tagline, final_genres, img_url, movie_id


def get_wiki_data(title):
    """Takes title of movie and returns wikipedia article"""
    # used api info sample code
    start = requests.Session()

    WIKI_URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "info",
        "inprop": "url|talkid",
    }
    response = start.get(url=WIKI_URL, params=PARAMS)
    data = response.json()
    key = data["query"]["pages"]
    for genre_id in key:  # must find movie id in order to find full url for the movie
        return data["query"]["pages"][genre_id]["fullurl"]
