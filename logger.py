import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger(__name__)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

# Example usage within the module
if __name__ == '__main__':
    log = Logger('exampleLogger')
    log.info('Logger initialized and ready.')