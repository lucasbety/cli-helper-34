
import os

class Config:
    """Configuration management class."""
    def __init__(self):
        self.environment = os.getenv('ENV', 'development')
        self.debug = self.is_debug_mode()
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
        self.secret_key = os.getenv('SECRET_KEY', 'default_secret')

    def is_debug_mode(self):
        """Determine if the application is in debug mode."""
        return self.environment == 'development'

    def get_config_as_dict(self):
        """Return configuration as a dictionary."""
        return {
            'environment': self.environment,
            'debug': self.debug,
            'database_url': self.database_url,
            'secret_key': self.secret_key
        }

# Example usage
if __name__ == '__main__':
    config = Config()
    print(config.get_config_as_dict())
