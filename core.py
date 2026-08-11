import time
import requests
from requests.exceptions import RequestException

def retry_decorator(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except RequestException as e:
                    attempts += 1
                    if attempts < max_retries:
                        print(f'Retry {attempts}/{max_retries} for {func.__name__}. Error: {e}')
                        time.sleep(delay)
                    else:
                        print(f'Max retries reached for {func.__name__}. Error: {e}')
                        raise
        return wrapper
    return decorator

@retry_decorator(max_retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an error for bad responses
    return response.json()  

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except Exception:
        print('Failed to fetch data')