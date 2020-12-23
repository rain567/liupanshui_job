from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode

url = "http://10.67.15.11:8888/auth/login/doLogin"
headers = {
    "User-Agent": 'PostmanRuntime/7.26.8',
    'Cookie': 'bid=yPpV_Zudq4M; dbcl2="228684977:8iWsyGHiOfk"; ck=Sl19'
}
# 转码解析
form_data = {
    "name": "18885422645",
    "password": "b02861485facff132407bbd02fbc616e"
}
form_data = urlencode(form_data)
# 构造请求
# Requert(url,headers,data)：有data参数就是post请求，没有就是get请求
request = Request(url, headers=headers,data=form_data.encode())
# 发送请求
response = urlopen(request)

print(response.read().decode())
print(response.geturl())