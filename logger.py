import logging
import logging.handlers
import os

# Constants for logging
LOG_LEVEL = logging.DEBUG
LOG_FILE_PATH = 'app.log'
LOG_MAX_BYTES = 1024 * 1024  # 1 MB
LOG_BACKUP_COUNT = 5

# Logger setup function
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL)

    # Create a rotating file handler
    handler = logging.handlers.RotatingFileHandler(LOG_FILE_PATH, 
                                                   maxBytes=LOG_MAX_BYTES, 
                                                   backupCount=LOG_BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Optional: add console handler for debug output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Example usage
def main():
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')

if __name__ == '__main__':
    main()