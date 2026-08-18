import time
from functools import wraps


def timeit(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def memoize(func):
    """Decorator to cache function results for performance optimization."""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@timeit
@memoize
def compute_value(x, y):
    """Expensive computation that we want to optimize."""
    time.sleep(1)  # Simulating a time-consuming operation
    return x * y
