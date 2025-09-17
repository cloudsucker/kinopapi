import aiohttp
import requests

from kinopapi.requests._handlers import _request, _request_async


# SUGGEST_SEARCH
def suggest_search(query: str) -> requests.Response:
    """API-запрос для получения предложений по поисковому запросу."""
    return _request("SUGGEST_SEARCH", searchQuery=query)


# [ ASYNC ] SUGGEST_SEARCH
async def suggest_search_async(query: str) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения предложений по поисковому запросу."""
    return await _request_async("SUGGEST_SEARCH", searchQuery=query)
