
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
__author__ = "UniCourt India"
__version__ = "v2.2018.03.26"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True



class TestingConfig(Config):
    TESTING = True