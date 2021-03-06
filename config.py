# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KgJyHDJuDjDJ'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SUBJECT_PREFIX = '[UAV-HiRAP]'
    MAIL_SENDER = 'DoNotReply <donotreply@uav-hirap.org>'
    UPLOADED_PHOTOS_DEST = basedir
    LANGUAGES = {
        'en': u'English',
        'zh': u'中文'
    }
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  #see app/__init__.py create_app()

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'hwsmtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    with open(os.path.join(basedir,'email_config.txt')) as f:
        email_config = eval(f.read())
    MAIL_USERNAME = email_config.get('MAIL_USERNAME')
    MAIL_PASSWORD = email_config.get('MAIL_PASSWORD')
    MAIL_ADMIN = email_config.get('MAIL_ADMIN')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    MAIL_SERVER = 'hwsmtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    with open(os.path.join(basedir, 'email_config.txt')) as f:
        email_config = eval(f.read())
    MAIL_USERNAME = email_config.get('MAIL_USERNAME')
    MAIL_PASSWORD = email_config.get('MAIL_PASSWORD')
    MAIL_ADMIN = email_config.get('MAIL_ADMIN')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}