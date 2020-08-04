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
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=c33c89e30a81b9c7ab78c93acf0a48e0cdf1e5923f78ef3f774c65105352ec26',data=json_data,headers=headers)
dingTalk()
