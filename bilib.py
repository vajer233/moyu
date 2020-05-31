import requests
import json

def dingTalk():
    headers={
        "Content-Type": "application/json"
            }
    data={
            "actionCard": {
                "title":"哔哩哔哩英文人声三日榜",
                "text": "![9f510fb30f2442a7c2e40af4da43ad4bd01302fc.jpg](https://i.loli.net/2020/05/31/Ft23lbGiWR57JPQ.jpg) 哔哩哔哩英文人声三日榜 \n放松一下，听首歌吧～",
                "singleTitle":"查看网页",
                "hideAvatar":"0",
                "singleURL": 'https://m.bilibili.com/audio/am30474',
            },
        "msgtype": "actionCard",
          }
    json_data=json.dumps(data)
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=94d6f3103ea61db64868ddc6ef02778f1ae2adf8334780db2860efa2a321c1cd',data=json_data,headers=headers)
dingTalk()

