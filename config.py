#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'adison'
# @Time    : 2017/11/21

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# database
DEV_DATABASE_URL = os.getenv('DATABASE_URI') or 'sqlite:///%s' % os.path.join(basedir, 'data_sqlite.db')
TEST_DATABASE_URL = os.getenv('DATABASE_URI') or 'sqlite:///%s' % os.path.join(basedir, 'data_sqlite.db')
PRODUCT_DATABASE_URL = 'mysql+pymysql://root:jcm52011@127.0.0.1:3306/blog?charset=utf8mb4'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxx'
    # 每次请求结束后自动commit
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 管理员
    ADMIN_EMAIL = 'jcm610@foxmail.com'
    ADMIN_USERNAME = 'woody'
    ADMIN_PASSWORD = '123456'

    #redis
    

    BABEL_DEFAULT_LOCALE = 'zh_CN'

    CACHE_KEY = "blog:%s"

    @staticmethod
    def init_app(app):
        pass


# 开发
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or DEV_DATABASE_URL


# 测试
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or TEST_DATABASE_URL


# 发布
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or PRODUCT_DATABASE_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
