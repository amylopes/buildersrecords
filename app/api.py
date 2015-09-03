# -*- coding: utf-8 -*-

"""
    app.api
    ~~~~~~~~~~~~~~~~

    API module
"""

from app import api_manager
from app.jwt import auth_func
from app.models import User, Project, Category, Item


api_manager.create_api(User,
    methods         = ['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix      = '/api',
    preprocessors   = dict(GET_SINGLE = [auth_func], GET_MANY = [auth_func]),
    collection_name = 'users')

api_manager.create_api(Project,
    methods         = ['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix      = '/api',
    preprocessors   = dict(GET_SINGLE = [auth_func], GET_MANY = [auth_func]),
    collection_name = 'projects')

api_manager.create_api(Category,
    methods         = ['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix      = '/api',
    preprocessors   = dict(GET_SINGLE = [auth_func], GET_MANY = [auth_func]),
    collection_name = 'categories')

api_manager.create_api(Item,
    methods         = ['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix      = '/api',
    preprocessors   = dict(GET_SINGLE = [auth_func], GET_MANY = [auth_func]),
    collection_name = 'items')
