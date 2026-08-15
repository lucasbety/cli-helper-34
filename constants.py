import time
import random

RETRIES = 3  # Number of retries for network operations
BACKOFF_FACTOR = 2  # Exponential backoff factor

class NetworkException(Exception):
    pass


def retry_on_failure(func):
    """Decorator to retry a network operation on failure."""
    def wrapper(*args, **kwargs):
        for attempt in range(RETRIES):
            try:
                return func(*args, **kwargs)
            except NetworkException as e:
                if attempt < RETRIES - 1:
                    wait_time = BACKOFF_FACTOR ** attempt + random.uniform(0, 1)
                    time.sleep(wait_time)  # Exponential backoff
                else:
                    raise e  # Exceeded retries
    return wrapper

@retry_on_failure
def perform_network_operation():
    # Simulated network operation that raises an exception
    if random.random() < 0.7:  # 70% chance of failure
        raise NetworkException("Network error occurred")
    return "Network operation successful!"
