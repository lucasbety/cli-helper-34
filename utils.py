import time
import requests

class NetworkError(Exception):
    pass


def retry_request(url, retries=3, delay=2):
    """
    Attempts to send a GET request to the specified URL with retry logic.
    :param url: The URL to send the request to.
    :param retries: Number of retry attempts.
    :param delay: Delay between attempts in seconds.
    :return: The response object if successful.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                print(f'Retry {attempt + 1}/{retries} failed: {e}. Retrying in {delay} seconds...')
                time.sleep(delay)
            else:
                raise NetworkError(f'Failed to reach {url} after {retries} attempts.') from e
