import os
import json
import aiofiles


def _get_headers(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Header file not found: {file_path}")

    headers = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    headers[key.strip()] = value.strip()
    except OSError as e:
        raise RuntimeError(f"Failed to read headers from {file_path}") from e

    return headers


async def _get_headers_async(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Header file not found: {file_path}")

    headers = {}
    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
            async for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    headers[key.strip()] = value.strip()
    except OSError as e:
        raise RuntimeError(f"Failed to read headers from {file_path}") from e

    return headers


def _get_body(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Body file not found: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to read body from {file_path}") from e


async def _get_body_async(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Body file not found: {file_path}")

    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
            content = await file.read()
        return json.loads(content)
    except (OSError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to read body from {file_path}") from e
