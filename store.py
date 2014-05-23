import os
import redis

redis_url = os.getenv('REDISTOGO_URL')
if redis_url is None:
	redis = redis.from_url("redis://redistogo:e53d9c9eee21af1cb977ac1c75e493e2@angelfish.redistogo.com:9536/")
else:
	redis = redis.from_url(redis_url)
