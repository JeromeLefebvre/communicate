import os
import redis

#redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_url = os.getenv('REDISTOGO_URL', 'redis://redistogo:e53d9c9eee21af1cb977ac1c75e493e2@angelfish.redistogo.com:9536/')
redis = redis.from_url(redis_url)
