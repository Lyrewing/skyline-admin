from vote import redis


def hits():
    redis.incr("hits")
    hit = redis.get('hits')
    print(hit)
