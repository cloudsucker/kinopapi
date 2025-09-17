import os
import importlib.util

# getting kinopoisk_api package directory
PACKAGE_NAME = "kinopapi"
PACKAGE_SPEC = importlib.util.find_spec(PACKAGE_NAME)
PACKAGE_PATH = os.path.dirname(PACKAGE_SPEC.origin)

# BASE_PATHS:
CONFIGURE_FOLDER = os.path.join(PACKAGE_PATH, "templates")
BASE_HEADERS_PATH = os.path.join(CONFIGURE_FOLDER, "headers")
BASE_BODIES_PATH = os.path.join(CONFIGURE_FOLDER, "bodies")

# ANOTHER HEADERS ARE NOT NEEDED YET:
DEFAULT_HEADER_PATH = os.path.join(BASE_HEADERS_PATH, "default.txt")

# REQUESTS_BODIES_PATH:
FILM_API_BODIES_PATH = os.path.join(BASE_BODIES_PATH, "film/")
TVSERIES_API_BODIES_PATH = os.path.join(BASE_BODIES_PATH, "tvseries/")
MOVIE_API_BODIES_PATH = os.path.join(BASE_BODIES_PATH, "movie/")
SEARCH_API_BODIES_PATH = os.path.join(BASE_BODIES_PATH, "search/")
PERSON_API_BODIES_PATH = os.path.join(BASE_BODIES_PATH, "person/")


# GRAPHQL TEMPLATE:
GRAPHQL_TEMPLATE = "https://graphql.kinopoisk.ru/graphql/?operationName={}"


# = = = = = = = = = = = = = = = = SEARCH = = = = = = = = = = = = = = = = = =


SEARCH = {
    # SEARCH BY NAME
    "SUGGEST_SEARCH": {
        "operation_name": "SuggestSearch",
        "headers": DEFAULT_HEADER_PATH,
        "body": SEARCH_API_BODIES_PATH + "SuggestSearch.json",
        "method": "POST",
        "params": ["searchQuery"],
        "body_key": "variables.keyword",
    },
}


# = = = = = = = = = = = = = = = = TVSERIES = = = = = = = = = = = = = = = = = =


TVSERIES = {
    # Инфа сериала по его id (вроде как не работает с фильмами)
    "TVSERIES_BASE_INFO": {
        "operation_name": "TvSeriesBaseInfo",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesBaseInfo.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_SIMILAR_MOVIES": {
        "operation_name": "TvSeriesSimilarMovies",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesSimilarMovies.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    # MAX: 30
    "TVSERIES_EPISODES": {
        "operation_name": "TvSeriesEpisodes",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesEpisodes.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_TRIVIAS": {
        "operation_name": "TvSeriesTrivias",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesTrivias.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_SOUNDTRACKS": {
        "operation_name": "TvSeriesSoundtracks",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesSoundtracks.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_MEDIA_POSTS": {
        "operation_name": "TvSeriesMediaPosts",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesMediaPosts.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_MOVIE_LISTS_RELATIONS": {
        "operation_name": "TvSeriesMovieListsRelations",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesMovieListsRelations.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
    "TVSERIES_CRITIC_REVIEWS": {
        "operation_name": "TvSeriesCriticReviews",
        "headers": DEFAULT_HEADER_PATH,
        "body": TVSERIES_API_BODIES_PATH + "TvSeriesCriticReviews.json",
        "method": "POST",
        "params": ["tvSeriesId"],
        "body_key": "variables.tvSeriesId",
    },
}


# = = = = = = = = = = = = = = = = FILM = = = = = = = = = = = = = = = = = =


FILM = {
    # Инфа фильма по его id (работает с некоторыми сериалами)
    "FILM_BASE_INFO": {
        "operation_name": "FilmBaseInfo",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmBaseInfo.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
    "FILM_SIMILAR_MOVIES": {
        "operation_name": "FilmSimilarMovies",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmSimilarMovies.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
    "FILM_TRIVIAS": {
        "operation_name": "FilmTrivias",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmTrivias.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
    "FILM_MEDIA_POSTS": {
        "operation_name": "FilmMediaPosts",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmMediaPosts.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
    "FILM_SOUNDTRACKS": {
        "operation_name": "FilmSoundtracks",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmSoundtracks.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
    "FILM_MOVIE_LISTS_RELATIONS": {
        "operation_name": "FilmMovieListsRelations",
        "headers": DEFAULT_HEADER_PATH,
        "body": FILM_API_BODIES_PATH + "FilmMovieListsRelations.json",
        "method": "POST",
        "params": ["filmId"],
        "body_key": "variables.filmId",
    },
}


# = = = = = = = = = = = = = = = = MOVIE = = = = = = = = = = = = = = = = = =


MOVIE = {
    "MOVIE_PREVIEW_CARD": {
        "operation_name": "MoviePreviewCard",
        "headers": DEFAULT_HEADER_PATH,
        "body": MOVIE_API_BODIES_PATH + "MoviePreviewCard.json",
        "method": "POST",
        "params": ["movieId"],
        "body_key": "variables.movieId",
    },
    # SEEMS LIKE NO TRAILERS HERE, JUST PREVIEW PICS OF THEM
    "MOVIE_TRAILERS_WITH_ORDER": {
        "operation_name": "MovieTrailersWithOrder",
        "headers": DEFAULT_HEADER_PATH,
        "body": MOVIE_API_BODIES_PATH + "MovieTrailersWithOrder.json",
        "method": "POST",
        "params": ["movieId"],
        "body_key": "variables.movieId",
    },
    "MOVIES_IN_CINEMA_WITH_FEATURING": {
        "operation_name": "MoviesInCinemaWithFeaturing",
        "headers": DEFAULT_HEADER_PATH,
        "body": MOVIE_API_BODIES_PATH + "MoviesInCinemaWithFeaturing.json",
        "method": "POST",
        "params": ["regionId"],
        "body_key": "variables.regionId",
    },
    "MOVIE_USERS_REVIEWS": {
        "operation_name": "MovieUsersReviews",
        "headers": DEFAULT_HEADER_PATH,
        "body": MOVIE_API_BODIES_PATH + "MovieUsersReviews.json",
        "method": "POST",
        "params": ["movieId"],
        "body_key": "variables.movieId",
    },
    "ORIGINAL_MOVIES": {
        "operation_name": "OriginalMovies",
        "headers": DEFAULT_HEADER_PATH,
        "body": MOVIE_API_BODIES_PATH + "OriginalMovies.json",
        "method": "POST",
        "params": ["movieId"],
        "body_key": "variables.movieId",
    },
}


# = = = = = = = = = = = = = = = = PERSON = = = = = = = = = = = = = = = = = =


PERSON = {
    "PERSON_PREVIEW_CARD": {
        "operation_name": "PersonPreviewCard",
        "headers": DEFAULT_HEADER_PATH,
        "body": PERSON_API_BODIES_PATH + "PersonPreviewCard.json",
        "method": "POST",
        "params": ["personId"],
        "body_key": "variables.personId",
    },
}


# = = = = = = = = = = = = = = = = ALL IN ONE = = = = = = = = = = = = = = = = = =


REQUESTS_CONFIG = {**SEARCH, **TVSERIES, **FILM, **MOVIE, **PERSON}
