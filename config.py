#!/usr/env/python3
# -*- coding: UTF-8 -*-

class AppConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xh:xh@localhost/xh?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @staticmethod
    def init_app(app):
        app.config['RESTFUL_JSON']['ensure_ascii'] = False
