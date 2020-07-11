import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "jFjhvkGVJjFjV5jFJ8Vv6j5vjKV"