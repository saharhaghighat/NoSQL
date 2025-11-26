import redis

class LeaderBoard:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
        self.key = "leaderboard"

    def add_score(self, user_id, score):
        self.redis_client.zadd(self.key,{user_id : score})

    def edit_score(self, user_id, score_delta):
        self.redis_client.zincrby(self.key, score_delta ,user_id)

    def get_top_users(self, count):
        tops = self.redis_client.zrevrange(self.key, 0, count-1, withscores=True)
        return tops

    def get_rank(self, user_id):
        rank = self.redis_client.zrevrank(self.key, user_id)
        return rank

    def get_score(self, user_id):
        score = self.redis_client.zscore(self.key, user_id)
        return score

    def remove_user(self, user_id):
        self.redis_client.zrem(self.key, user_id)