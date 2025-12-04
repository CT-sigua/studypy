import requests
import json

def tianqi(ct):
    url = f"https://v2.xxapi.cn/api/weather?city={ct}&key=4078ba0a30295147"

    payload = {}
    headers = {'User-Agent': 'xiaoxiaoapi/1.0.0'}

    response = requests.request("GET",url,headers=headers,data=payload)

    # print(f'{ct}天气:',response.text)
    tq_text = response.text
    tq_json = json.loads(tq_text)
    # wendu = tq_json["data"]["data"][1]
    air_quality = tq_json["data"]["data"][1]["air_quality"]
    date = tq_json["data"]["data"][1]["date"]
    temperature = tq_json["data"]["data"][1]["temperature"]
    weather = tq_json["data"]["data"][1]["weather"]
    wind = tq_json["data"]["data"][1]["wind"]
    print(f'{ct}天气：{weather} 空气质量{air_quality} 星期{date} 温度{temperature} {wind}')
    
#pip install requests
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。
#UnboundLocalError: cannot access local variable 'requests' where it is not associated with a value 

# json.load(file): 从一个文件对象中读取JSON数据。需要打开文件并将文件对象传递给该函数。
# json.loads(string): 从一个JSON格式的字符串中读取数据。直接将字符串作为参数传递给该函数。

# tianqi('西安')