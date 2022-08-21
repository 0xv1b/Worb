import redis
from flask import current_app, g

client = redis.Redis()