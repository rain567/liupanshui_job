from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode

# url = "https://accounts.douban.com/passport/login_popup?login_source=anony"
# url = "https://accounts.douban.com"
# url = "https://accounts.douban.com/passport/login?redir=https://accounts.douban.com/"
url = "https://accounts.douban.com/j/mobile/login/basic"
headers = {
    # 'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>',
    # 'Content-Length': '<calculated when request is sent>',
    "User-Agent": 'PostmanRuntime/7.26.8',
    'Cookie': 'bid=yPpV_Zudq4M; dbcl2="228684977:8iWsyGHiOfk"; ck=Sl19'
    # 'Host': '<calculated when request is sent>'
}
# 转码解析
form_data = {
    "remember": "true",
    "name": "18885422645",
    "password": "mcj967567"
}
form_data = urlencode(form_data)
# 构造请求
# Requert(url,headers,data)：有data参数就是post请求，没有就是get请求
request = Request(url, headers=headers,data=form_data.encode())
# 发送请求
response = urlopen(request)

print(response.read().decode())
print(response.geturl())