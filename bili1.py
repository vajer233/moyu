import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=c92c80978be7d47ebaa12f450302c68194bc100994025563d85170e1c55f9183'
# 罗翔说刑法,毕导THU,何同学
bili_ids = ['517327498','254463269','163637592']
yesterday = time.time()-60*60*24  # 1天前

obj = {
    "msgtype": "text",
    "text": {
        "content": 'B站:'+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    }
}
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)



for bid in bili_ids:
    bili_url = 'https://api.bilibili.com/x/space/arc/search?mid='+bid+'&pn=1&ps=25&jsonp=jsonp'

    r = requests.get(bili_url)
    videos = r.json()['data']['list']['vlist']
    for video in videos:
        if(video['created']>yesterday):
            print(video['title'],video['description'],video['author'])
            print(video['created'])
            obj = {
                "msgtype": "link",
                "link": {
                    "text": video['description']+'B站',
                    "title": video['title'],
                    "picUrl": 'http:'+video['pic'],
                    "messageUrl": "https://www.bilibili.com/video/av%s" %(video['aid'])
                }
            }
            requests.post(url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(obj)
            )
