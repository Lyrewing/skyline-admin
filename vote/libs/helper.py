from vote.libs import redis


def hits():
    redis.incr("hits")
    hit = redis.get('hits')
    print(hit)
