import logging

# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

class NetworkOperations:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
        
    def retry(self, func, *args, **kwargs):
        for attempt in range(self.max_retries):
            try:
                logger.info(f'Attempt {attempt + 1} for {func.__name__}')
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f'Error on attempt {attempt + 1}: {e}')
                if attempt == self.max_retries - 1:
                    logger.critical('Max retries reached, operation failed.')
                    raise
                
    def example_network_call(self, url):
        # Simulates a network call that might fail
        logger.info(f'Making network call to {url}')
        raise Exception('Network error simulated')

# Usage example:
if __name__ == '__main__':
    net_ops = NetworkOperations(max_retries=5)
    try:
        net_ops.retry(net_ops.example_network_call, 'http://example.com')
    except Exception:
        logger.critical('Operation could not be completed.')
