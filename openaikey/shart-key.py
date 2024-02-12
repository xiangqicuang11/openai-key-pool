import openai
from datetime import datetime, timedelta

class OpenAIKeyPool:
    def __init__(self):
        self.keys = []

    def check_quota(self, key):
        for key_info in self.keys:
            if key_info["key"] == key:
                if key_info["quota"] is not None:
                    return f"密钥",{key_info['name']},({key_info['key']}),的额度为,{key_info['quota']}。
                else:
                    return f "密钥",{key_info['name']},({key_info['key']}),没有设置额度。"
        return "未找到该密钥。"

def shart-key(key):
    pool = OpenAIKeyPool()
    return pool.check_quota(key)
