import requests
import json
def dingTalk():
    headers={
        "Content-Type": "application/json"
            }
    data={"msgtype": "text",
            "text": {
                 "content": "起来了啊，把内务和卫生都做好再走啊！"
            }
          }
    json_data=json.dumps(data)
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=dcb2b6c5bba9e3e79263112f17ffe6f37ce1e0ce7a4b5fee4ff01f3ad70fa7cb',data=json_data,headers=headers)
dingTalk()