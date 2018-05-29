# -*- coding: utf-8 -*-
class Configuration(object):
    DEBUG = True
    STATIC_FOLDER = '/static'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False