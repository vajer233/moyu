import requests
import json
import time
url = 'https://oapi.dingtalk.com/robot/send?access_token=94d6f3103ea61db64868ddc6ef02778f1ae2adf8334780db2860efa2a321c1cd'
# YouTube听力精选
bili_ids = ['6926237']
yesterday = time.time()-60*60*24*2  # 1天前
obj = {
    "msgtype": "text",
        "text": {
            "content": 'https://m.bilibili.com/audio/am30474' ,
    }
}
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
