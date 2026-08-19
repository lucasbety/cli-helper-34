import time
import functools

# Memoization decorator to cache results of expensive computations
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]
    return wrapper

# Example expensive function that calculates Fibonacci
@memoize
def fibonacci(n):
    if n < 0:
        raise ValueError('Negative arguments are not supported')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Performance improvement in computing Fibonacci series
start_time = time.time()
for i in range(35):  # Example for first 35 Fibonacci numbers
    print(f'Fibonacci of {i} is {fibonacci(i)}')
end_time = time.time()
print(f'Computation time: {end_time - start_time} seconds')