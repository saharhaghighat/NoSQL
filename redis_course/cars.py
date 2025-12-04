import redis


class QueraCar:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        self.key = "queras_car_nodes"

    def add_node(self, node_id, latitude, longitude):
        self.redis_client.geoadd(self.key, (longitude, latitude, node_id))

    def remove_node(self, node_id):
        self.redis_client.zrem(self.key, node_id)

    def find_nearby_nodes(self, car_node_id, radius_km):
        result = self.redis_client.georadiusbymember(
            self.key,
            car_node_id,
            radius_km,
            unit="km",
            withcoord=True
        )

        nearby = []
        for node, coords in result:
            if node == car_node_id:
                continue

            lon, lat = coords
            nearby.append((node, (lat, lon)))

        return nearby

    def remove_nearby_nodes(self, car_node_id, radius_km):
        result = self.redis_client.georadiusbymember(
            self.key,
            car_node_id,
            radius_km,
            unit="km"
        )

        for node in result:
            if node != car_node_id:
                self.redis_client.zrem(self.key, node)
