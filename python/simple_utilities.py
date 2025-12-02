import logging
import csv
import requests
from typing import List, Dict, Any, Callable
from functools import wraps
import time


def setup_logging(level: int = logging.INFO, log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s") -> None:
    """Configure root logger with the given level and format."""
    logging.basicConfig(level=level, format=log_format)


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """Read a CSV file and return a list of dictionaries."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def write_csv(file_path: str, data: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    """Write a list of dictionaries to a CSV file with the specified fieldnames."""
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def call_api(url: str, method: str = 'GET', retries: int = 3, **kwargs) -> requests.Response:
    """Make an HTTP API call with simple retry logic. Supports GET and POST methods."""
    for attempt in range(retries):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, **kwargs)
            elif method.upper() == 'POST':
                response = requests.post(url, **kwargs)
            else:
                raise ValueError("Unsupported HTTP method: {}".format(method))
            response.raise_for_status()
            return response
        except requests.RequestException:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)


def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
    """Validate that a dictionary matches the expected types defined in the schema."""
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True


def timed_cache(expiration: int = 60):
    """Decorator that caches function results for a given number of seconds."""
    def decorator(func: Callable):
        cache: Dict[Any, Any] = {}

        @wraps(func)
        def wrapped(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < expiration:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result

        return wrapped

    return decorator
