import aiohttp
import requests

from kinopapi.requests._handlers import _request, _request_async


# PERSON_PREVIEW_CARD
def person_preview_card(person_id: int) -> requests.Response:
    """API-запрос для получения данных человека из киноиндустрии."""
    return _request("PERSON_PREVIEW_CARD", personId=person_id)


# [ ASYNC ] PERSON_PREVIEW_CARD
async def person_preview_card_async(person_id: int) -> aiohttp.ClientResponse:
    """Асинхронный API-запрос для получения данных человека из киноиндустрии."""
    return await _request_async("PERSON_PREVIEW_CARD", personId=person_id)
