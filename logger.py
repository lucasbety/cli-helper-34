import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file, level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    log = setup_logger('app.log')
    log.info('Logger is set up successfully.')