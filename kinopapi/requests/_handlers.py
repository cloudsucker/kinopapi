import aiohttp
import requests

from kinopapi.templates import _get_headers, _get_body
from kinopapi.templates import _get_headers_async, _get_body_async
from kinopapi.config import REQUESTS_CONFIG, GRAPHQL_TEMPLATE


def _build_request_body(config, kwargs):
    body = _get_body(config["body"])

    if config["params"]:
        for param in config["params"]:
            if param not in kwargs:
                raise ValueError(f"Missing request parameter: {param}")

            if config.get("body_key"):
                keys = config["body_key"].split(".")
                temp_body = body
                for key in keys[:-1]:
                    temp_body = temp_body.get(key, {})
                temp_body[keys[-1]] = kwargs[param]
    return body


async def _build_request_body_async(config, kwargs):
    body = await _get_body_async(config["body"])

    if config["params"]:
        for param in config["params"]:
            if param not in kwargs:
                raise ValueError(f"Missing request parameter: {param}")

            if config.get("body_key"):
                keys = config["body_key"].split(".")
                temp_body = body
                for key in keys[:-1]:
                    temp_body = temp_body.get(key, {})
                temp_body[keys[-1]] = kwargs[param]
    return body


def _request(request_type: str, **kwargs) -> requests.Response:
    if request_type not in REQUESTS_CONFIG:
        raise ValueError(f"Request type not found: {request_type}.")

    config = REQUESTS_CONFIG[request_type]
    headers = _get_headers(config["headers"])
    body = _build_request_body(config, kwargs)
    url = GRAPHQL_TEMPLATE.format(config["operation_name"])

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response

    except requests.RequestException as e:
        print(f"Request could not be completed: {e}")


async def _request_async(request_type: str, **kwargs) -> aiohttp.ClientResponse:
    if request_type not in REQUESTS_CONFIG:
        raise ValueError(f"Request type not found: {request_type}.")

    config = REQUESTS_CONFIG[request_type]
    headers = await _get_headers_async(config["headers"])
    body = await _build_request_body_async(config, kwargs)
    url = GRAPHQL_TEMPLATE.format(config["operation_name"])

    session = aiohttp.ClientSession()
    try:
        response = await session.post(url, json=body, headers=headers)
        response.raise_for_status()
        # idk why, but this shit needs to make this function work
        _ = await response.text()
        # without this line getting errors:
        #   - "aiohttp.client_exceptions.ClientConnectionError: Connection closed"
        #   - "RuntimeError: Connection closed."
        # and await response.wait_for_close() doesn't helps here ;D
        return response

    except aiohttp.ClientError as e:
        print(f"Request could not be completed: {e}")
    finally:
        await session.close()
