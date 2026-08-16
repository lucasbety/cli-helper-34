import os

# File types constant
TEXT_FILE = '.txt'
CSV_FILE = '.csv'
JSON_FILE = '.json'

# Status constants
SUCCESS = 0
FAILURE = 1

# Default configurations
DEFAULT_ENCODING = 'utf-8'
DEFAULT_DELIMITER = ','

# API URLs
BASE_API_URL = 'https://api.example.com/'
USER_ENDPOINT = BASE_API_URL + 'users/'
POST_ENDPOINT = BASE_API_URL + 'posts/'

# Common message templates
ERROR_MESSAGE = 'An error occurred while processing your request.'
SUCCESS_MESSAGE = 'Operation completed successfully.'

# File size limits (in bytes)
MAX_FILE_SIZE = 10485760  # 10 MB
MIN_FILE_SIZE = 1024       # 1 KB

# Environment variables
ENV_MODE = os.getenv('ENV_MODE', 'development')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'

# Logging constants
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Other constants
TIMEOUT_DURATION = 30  # in seconds