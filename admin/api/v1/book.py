import os
import socket
from flask import Blueprint
from redis import Redis

book = Blueprint("book", __name__)

"""
redis = Redis(host=os.environ.get("REDIS_HOST", '127.0.0.1'), port=6379)
"""


@book.route("/get")
def get_book():
    return "get book"


"""
@book.route("/redis")
def hello_redis():
    redis.incr("hits")
    hit = redis.get('hits')
    hostname = socket.gethostname()
    message = 'hello Container world!  {hit} times and my hostname is {host_name}.\n'.format(hit=hit,
                                                                                             host_name=hostname)
    return message
"""
