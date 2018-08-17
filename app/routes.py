from app import app
from redis import Redis
import os
import socket

redis = Redis(host=os.environ.get("REDIS_HOST", '127.0.0.1'), port=6379)


@app.route("/")
def hello():
    return "hello world"


@app.route("/redis")
def hello_redis():
    redis.incr("hits")
    hit = redis.get('hits')
    hostname = socket.gethostname()
    message = 'hello Container world!  {hit} times and my hostname is {host_name}.\n'.format(hit=hit,
                                                                                             host_name=hostname)
    return message
