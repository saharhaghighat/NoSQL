import redis


class BloomFilter:
    def __init__(self, filter_name, user_id, capacity=10000, error_rate=0.01):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        self.view_filter_name = f"{filter_name}:{user_id}:view"
        self.purchase_filter_name = f"{filter_name}:{user_id}:purchase"
        self.view_count_filter_name = f"{filter_name}:{user_id}:view:count"

        self.capacity = capacity
        self.error_rate = error_rate

        if not self.redis_client.exists(self.view_filter_name):
            self.redis_client.execute_command("BF.RESERVE", self.view_filter_name, self.error_rate, self.capacity)

        if not self.redis_client.exists(self.purchase_filter_name):
            self.redis_client.execute_command("BF.RESERVE", self.purchase_filter_name, self.error_rate, self.capacity)

        if not self.redis_client.exists(self.view_count_filter_name):
            self.redis_client.execute_command("CF.RESERVE", self.view_count_filter_name, self.error_rate, self.capacity)

    def add_view(self, item):
        self.redis_client.execute_command("BF.ADD",
                                          self.view_filter_name,
                                          item)
        self.redis_client.execute_command(
            "CF.ADD",
            self.view_count_filter_name,
            item
        )
    def add_purchase(self, item):
        self.redis_client.execute_command("BF.ADD",self.purchase_filter_name, item)

    def has_viewed(self, item):
        exist_result = self.redis_client.execute_command("BF.EXISTS",self.view_filter_name, item)
        if exist_result:
            return True
        return False


    def has_purchased(self, item):
        purchased_result = self.redis_client.execute_command("BF.EXISTS",self.purchase_filter_name, item)
        if purchased_result:
            return True
        return False

    def view_count(self, item):
        count = self.redis_client.execute_command(
            "CF.COUNT",
            self.view_count_filter_name,
            item
        )
        return count