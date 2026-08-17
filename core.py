import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    """
    Perform a GET request with retry logic.
    :param url: The URL to send the request to.
    :param retries: Number of times to retry on failure.
    :param delay: Delay between retries in seconds.
    :return: The response object if successful.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
                continue  # Retry
            raise NetworkError(f"Network request failed after {retries} attempts: {e}")

# Example usage of the retry_request function
if __name__ == '__main__':
    try:
        response = retry_request('https://jsonplaceholder.typicode.com/posts')
        print(response.json())
    except NetworkError as e:
        print(e)