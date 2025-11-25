import redis
import time

class CollaborativeEditor:
    def __init__(self, document_id):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        self.document_key = f"document:{document_id}"
        self.user_cursor_key = f"document:{document_id}:cursors"
        self.edit_history_key = f"document:{document_id}:history"
        self.user_activity_key = f"document:{document_id}:activity"

    def update_cursor(self, user_id, cursor_position):
        self.redis_client.hset(self.user_cursor_key, user_id, cursor_position)

    def update_document(self, user_id, new_text):
        current_text = self.redis_client.get(self.document_key)
        if current_text is None:
            current_text = ""
        self.redis_client.rpush(self.edit_history_key, current_text)

        self.redis_client.set(self.document_key, new_text)

        self.redis_client.hset(self.user_cursor_key, user_id, len(new_text))

        timestamp = int(time.time())
        self.redis_client.hset(self.user_activity_key, user_id, timestamp)

    def undo_last_edit(self):
        last_text = self.redis_client.rpop(self.edit_history_key)
        if last_text is None:
            return "No edits to undo."

        self.redis_client.set(self.document_key, last_text)
        return "Undo successful."

    def get_document(self):
        text = self.redis_client.get(self.document_key)
        return text if text is not None else ""

    def get_cursors(self):
        cursors = self.redis_client.hgetall(self.user_cursor_key)
        return cursors

    def get_active_users(self, timeout=300):
        now = int(time.time())
        users = self.redis_client.hgetall(self.user_activity_key)

        active_users = {}

        for user_id, last_activity in users.items():
            last_activity = int(last_activity)
            if now - last_activity <= timeout:
                active_users[user_id] = last_activity

        return active_users
