import aiohttp
import requests

from kinopapi.requests._handlers import _request, _request_async


# TVSERIES_TRIVIAS
def tvseries_trivias(tvseries_id: int) -> requests.Response:
    """API-запрос для получения интересных фактов о сериале по его ID."""
    return _request("TVSERIES_TRIVIAS", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_TRIVIAS
async def tvseries_trivias_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения интересных фактов о сериале по его ID."""
    return await _request_async("TVSERIES_TRIVIAS", tvSeriesId=tvseries_id)


# TVSERIES_SIMILAR_MOVIES
def tvseries_similar_movies(tvseries_id: int) -> requests.Response:
    """API-запрос для получения списка похожих сериалов по ID сериала."""
    return _request("TVSERIES_SIMILAR_MOVIES", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_SIMILAR_MOVIES
async def tvseries_similar_movies_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения списка похожих сериалов по ID сериала."""
    return await _request_async("TVSERIES_SIMILAR_MOVIES", tvSeriesId=tvseries_id)


# TVSERIES_EPISODES
def tvseries_episodes(tvseries_id: int) -> requests.Response:
    """API-запрос для получения списка серий сериала по его ID."""
    return _request("TVSERIES_EPISODES", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_EPISODES
async def tvseries_episodes_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения списка серий сериала по его ID."""
    return await _request_async("TVSERIES_EPISODES", tvSeriesId=tvseries_id)


# TVSERIES_BASE_INFO
def tvseries_base_info(tvseries_id: int) -> requests.Response:
    """API-запрос для получения базовой информации о сериале по его ID."""
    return _request("TVSERIES_BASE_INFO", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_BASE_INFO
async def tvseries_base_info_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения базовой информации о сериале по его ID."""
    return await _request_async("TVSERIES_BASE_INFO", tvSeriesId=tvseries_id)


# TVSERIES_SOUNDTRACKS
def tvseries_soundtracks(tvseries_id: int) -> requests.Response:
    """API-запрос для получения саундтреков сериала по его ID."""
    return _request("TVSERIES_SOUNDTRACKS", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_SOUNDTRACKS
async def tvseries_soundtracks_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения саундтреков сериала по его ID."""
    return await _request_async("TVSERIES_SOUNDTRACKS", tvSeriesId=tvseries_id)


# TVSERIES_MEDIA_POSTS
def tvseries_media_posts(tvseries_id: int) -> requests.Response:
    """API-запрос для получения медиа-постов сериала по его ID."""
    return _request("TVSERIES_MEDIA_POSTS", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_MEDIA_POSTS
async def tvseries_media_posts_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения медиа-постов сериала по его ID."""
    return await _request_async("TVSERIES_MEDIA_POSTS", tvSeriesId=tvseries_id)


# TVSERIES_MOVIE_LISTS_RELATIONS
def tvseries_movie_lists_relations(tvseries_id: int) -> requests.Response:
    """API-запрос для получения связей сериала с киносписками по его ID."""
    return _request("TVSERIES_MOVIE_LISTS_RELATIONS", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_MOVIE_LISTS_RELATIONS
async def tvseries_movie_lists_relations_async(
    tvseries_id: int,
) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения связей сериала с киносписками по его ID."""
    return await _request_async(
        "TVSERIES_MOVIE_LISTS_RELATIONS", tvSeriesId=tvseries_id
    )


# TVSERIES_CRITIC_REVIEWS
def tvseries_critic_reviews(tvseries_id: int) -> requests.Response:
    """API-запрос для получения критических отзывов о сериале по его ID."""
    return _request("TVSERIES_CRITIC_REVIEWS", tvSeriesId=tvseries_id)


# [ ASYNC ] TVSERIES_CRITIC_REVIEWS
async def tvseries_critic_reviews_async(tvseries_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения критических отзывов о сериале по его ID."""
    return await _request_async("TVSERIES_CRITIC_REVIEWS", tvSeriesId=tvseries_id)
