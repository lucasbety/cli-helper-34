import logging
import sys

class Logger:
    def __init__(self, name, log_file='app.log', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def log_execution_time(self, func):
        import time
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.logger.info(f'Execution time of {func.__name__}: {end_time - start_time:.4f} seconds')
            return result
        return wrapper

# Usage example
if __name__ == '__main__':
    log = Logger(__name__)
    log.info('Logger initialized')

    @log.log_execution_time
    def sample_function():
        time.sleep(2)
        log.info('Sample function executed')

    sample_function()