from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "http://www.baidu.com"

user_agent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
              "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"]


headers = {
        "User-Agent":choice(user_agent)
    }


request = Request(url, headers=headers)

response = urlopen(request)

a = response.read()

print(a.decode())

