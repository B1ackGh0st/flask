# -*- coding: utf-8 -*-
class Configuration(object):
    DEBUG = True
    STATIC_FOLDER = '/static'
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
