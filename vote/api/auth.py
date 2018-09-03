import time
from vote import redis

QUIT = False
LIMIT = 1000000


# 尝试获取令牌并返回对应的用户
def check_token(token: str):
    return redis.hget("login:", token)
    pass


def update_token(user, token: str, item=None):
    timestamp = time.time()
    redis.hset("login:", token, user)
    redis.zadd("recent:", token, timestamp)
    if item:
        redis.zadd("viewed:" + token, item, timestamp)
        redis.zremrangebyrank("viewed:" + token, 0, -26)
    pass


def clean_session():
    while not QUIT:
        size = redis.zcard("recent:")
        if size <= LIMIT:
            time.sleep(1)
            continue
        end_index = min(size - LIMIT, 100)
        tokens = redis.zrange("recent:", 0, end_index - 1)
        session_keys = []
        for token in tokens:
            session_keys.append("viewed:" + token)
        redis.delete(*session_keys)
        redis.hdel("login:", *tokens)
        redis.zrem("recent:", *token)
