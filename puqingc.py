import requests
import json
import random


def random_sentence():
    a = "起来！站到十二点！"
    b = "都几点了还讲话！"
    c = "下来！去写200字反思再睡！"
    if random.randint(1, 3) == 1:
        return a
    if random.randint(1, 3) == 2:
        return b
    if random.randint(1, 3) == 3:
        return c


def dingTalk():
    headers = {
        "Content-Type": "application/json"
    }
    data = {"msgtype": "text",
            "text": {
                "content": random_sentence()
            }
            }
    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token'
            '=c33c89e30a81b9c7ab78c93acf0a48e0cdf1e5923f78ef3f774c65105352ec26',
        data=json_data, headers=headers)


dingTalk()
