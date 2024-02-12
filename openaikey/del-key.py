import openai
from datetime import datetime, timedelta

class OpenAIKeyPool:
    def __init__(self):
        self.keys = []

    def delete_key(self, key):
        for i, key_info in enumerate(self.keys):
            if key_info["key"] == key:
                del self.keys[i]
                print(f"已删除密钥 {key_info['name']} ({key_info['key']})。")
        print("未找到该密钥。")
        return no

    def del-key():
        pool = OpenAIKeyPool()
        c=pool.delete_key(key)
        return c
        
        
