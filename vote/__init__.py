import os
from redis import Redis

redis = Redis(host=os.environ.get("REDIS_HOST", '116.85.24.98'), port=6379)