import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string4fq44q5363#^$^$&@#'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UR2B_MAIL_SUBJECT_PREFIX = '[UR2B]'
    UR2B_MAIL_SENDER = '75027422@qq.com'
    UR2B_ADMIN = os.environ.get('UR2B_ADMIN')
    UR2B_POSTS_PER_PAGE = 20
    UR2B_FOLLOWERS_PER_PAGE = 50
    UR2B_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lansheng@127.0.0.1/myflask?charset=utf8mb4'


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:lansheng@127.0.0.1/myflask?charset=utf8mb4'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lansheng@127.0.0.1/myflask?charset=utf8mb4'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
