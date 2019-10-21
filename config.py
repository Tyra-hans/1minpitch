import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('158b370c0bb817944038f22c47007071')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/minutepitch'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}