import aiohttp
import requests

from kinopapi.requests._handlers import _request, _request_async


# MOVIE_PREVIEW_CARD
def movie_preview_card(movieId: int) -> requests.Response:
    """API-запрос для получения карточки фильма по его ID."""
    return _request("MOVIE_PREVIEW_CARD", movieId=movieId)


# [ ASYNC ] MOVIE_PREVIEW_CARD
async def movie_preview_card_async(movieId: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения карточки фильма по его ID."""
    return await _request_async("MOVIE_PREVIEW_CARD", movieId=movieId)


# MOVIE_TRAILERS_WITH_ORDER
def movie_trailers_with_order(movieId: int) -> requests.Response:
    """API-запрос для получения трейлеров фильма в заданном порядке по его ID."""
    return _request("MOVIE_TRAILERS_WITH_ORDER", movieId=movieId)


# [ ASYNC ] MOVIE_TRAILERS_WITH_ORDER
async def movie_trailers_with_order_async(movieId: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения трейлеров фильма в заданном порядке по его ID."""
    return await _request_async("MOVIE_TRAILERS_WITH_ORDER", movieId=movieId)


# MOVIES_IN_CINEMA_WITH_FEATURING
def movies_in_cinema_with_featuring(region_id: int) -> requests.Response:
    """API-запрос для получения списка фильмов в кинотеатрах с учетом региона."""
    return _request("MOVIES_IN_CINEMA_WITH_FEATURING", regionId=region_id)


# [ ASYNC ] MOVIES_IN_CINEMA_WITH_FEATURING
async def movies_in_cinema_with_featuring_async(
    region_id: int,
) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения списка фильмов в кинотеатрах с учетом региона."""
    return await _request_async("MOVIES_IN_CINEMA_WITH_FEATURING", regionId=region_id)


# MOVIE_USERS_REVIEWS
def movie_users_reviews(movie_id: int) -> requests.Response:
    """API-запрос для получения пользовательских отзывов о фильме по его ID."""
    return _request("MOVIE_USERS_REVIEWS", movieId=movie_id)


# [ ASYNC ] MOVIE_USERS_REVIEWS
async def movie_users_reviews_async(movie_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения пользовательских отзывов о фильме по его ID."""
    return await _request_async("MOVIE_USERS_REVIEWS", movieId=movie_id)


# ORIGINAL_MOVIES
def original_movies(movie_id: int) -> requests.Response:
    """API-запрос для получения оригинальных фильмов по ID фильма."""
    return _request("ORIGINAL_MOVIES", movieId=movie_id)


# [ ASYNC ] ORIGINAL_MOVIES
async def original_movies_async(movie_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения оригинальных фильмов по ID фильма."""
    return await _request_async("ORIGINAL_MOVIES", movieId=movie_id)
