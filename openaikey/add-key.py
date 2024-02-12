import openai
from datetime import datetime, timedelta
def create_openai_key(api_key, key_name=None, expire_date=None, quota=None):
    openai.api_key = api_key
    try:
        response = openai.Model.list()
        print("密钥有效。")
        if key_name is None:
            key_name = input("请输入密钥名称：")
        if expire_date is None:
            expire_date = input("请输入密钥过期日期（格式：YYYY-MM-DD）：")
            expire_date = datetime.strptime(expire_date, "%Y-%m-%d")
        if quota is None:
            quota = int(input("请输入密钥额度："))
        return {"name": key_name, "key": api_key, "expire_date": expire_date, "quota": quota}
    except Exception as e:
        print("密钥无效，请重新输入。")
        return None
def add-key():
    api_key = input("请输入OpenAI API密钥：")
    key_info = create_openai_key(api_key)
    if key_info:
        print("创建的密钥信息：", key_info)
        return key_info
