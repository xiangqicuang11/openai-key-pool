import openai
from datetime import datetime, timedelta
class OpenAIKeyPool:
    def __init__(self):
        self.keys = []

    def save_keys(self, file_path):
        with open(file_path, "w") as f:
            for key_info in self.keys:
                f.write(f"{key_info['name']},{key_info['key']},{key_info['expire_date']},{key_info['quota']}")
def sava-key(key,name,time,quota):
    pool = OpenAIKeyPool()
    pool.save_keys("keys.txt")
