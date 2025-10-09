import requests
import os, sys

# 发送 POST 请求
response = requests.post(sys.argv[1])

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()  # 解析 JSON 数据

    for path, content in data.items():
        # 确保目录存在
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        # 写入文件
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    print("所有文件已成功写入。")
else:
    print(f"请求失败，状态码：{response.status_code}")
