import aiohttp
import requests

from kinopapi.requests._handlers import _request, _request_async


# FILM_BASE_INFO
def film_base_info(film_id: int) -> requests.Response:
    """API-запрос для получения информации о фильме по его ID."""
    return _request("FILM_BASE_INFO", filmId=film_id)


# [ ASYNC ] FILM_BASE_INFO
async def film_base_info_async(film_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения информации о фильме по его ID."""
    return await _request_async("FILM_BASE_INFO", filmId=film_id)


# FILM_SIMILAR_MOVIES
def film_similar_movies(filmId: int) -> requests.Response:
    """API-запрос для получения похожих фильмов по ID фильма."""
    return _request("FILM_SIMILAR_MOVIES", filmId=filmId)


# [ ASYNC ] FILM_SIMILAR_MOVIES
async def film_similar_movies_async(filmId: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения похожих фильмов по ID фильма."""
    return await _request_async("FILM_SIMILAR_MOVIES", filmId=filmId)


# FILM_TRIVIAS
def film_trivias(film_id: int) -> requests.Response:
    """API-запрос для получения интересных фактов о фильме по его ID."""
    return _request("FILM_TRIVIAS", filmId=film_id)


# [ ASYNC ] FILM_TRIVIAS
async def film_trivias_async(film_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения интересных фактов о фильме по его ID."""
    return await _request_async("FILM_TRIVIAS", filmId=film_id)


# FILM_MEDIA_POSTS
def film_media_posts(film_id: int) -> requests.Response:
    """API-запрос для получения медиа-постов фильма по его ID."""
    return _request("FILM_MEDIA_POSTS", filmId=film_id)


# [ ASYNC ] FILM_MEDIA_POSTS
async def film_media_posts_async(film_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения медиа-постов фильма по его ID."""
    return await _request_async("FILM_MEDIA_POSTS", filmId=film_id)


# FILM_SOUNDTRACKS
def film_soundtracks(film_id: int) -> requests.Response:
    """API-запрос для получения саундтрека фильма по его ID."""
    return _request("FILM_SOUNDTRACKS", filmId=film_id)


# [ ASYNC ] FILM_SOUNDTRACKS
async def film_soundtracks_async(film_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения саундтрека фильма по его ID."""
    return await _request_async("FILM_SOUNDTRACKS", filmId=film_id)


# FILM_MOVIE_LISTS_RELATIONS
def film_movie_lists_relations(film_id: int) -> requests.Response:
    """API-запрос для получения отношений фильмов с другим контентом по его ID."""
    return _request("FILM_MOVIE_LISTS_RELATIONS", filmId=film_id)


# [ ASYNC ] FILM_MOVIE_LISTS_RELATIONS
async def film_movie_lists_relations_async(film_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения отношений фильмов с ругим контентом по его ID."""
    return await _request_async("FILM_MOVIE_LISTS_RELATIONS", filmId=film_id)
