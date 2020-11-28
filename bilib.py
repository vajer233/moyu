# import requests
# import json

# def dingTalk():
#     headers={
#         "Content-Type": "application/json"
#             }
#     data={
#             "actionCard": {
#                 "title":"哔哩哔哩英文人声三日榜",
#                 "text": "![a.jpg](https://i.loli.net/2020/08/06/j1d7S8kamNhvBor.jpg) 哔哩哔哩英文人声三日榜 \n放松一下，听首歌吧～",
#                 "singleTitle":"查看网页",
#                 "hideAvatar":"0",
#                 "singleURL": 'https://m.bilibili.com/audio/am30474',
#             },
#         "msgtype": "actionCard",
#           }
#     json_data=json.dumps(data)
#     requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=94d6f3103ea61db64868ddc6ef02778f1ae2adf8334780db2860efa2a321c1cd',data=json_data,headers=headers)
# dingTalk()

