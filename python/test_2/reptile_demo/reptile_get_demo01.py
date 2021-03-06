from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import quote
import re


def get_html(url):
    headers = {
        'User_Agent': UserAgent().chrome,
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def main():
    content = input("请输入搜索的内容：")
    base_url = "http://www.baidu.com/s?wd={}".format(quote(content))
    info = get_html(base_url)
    match = re.search(r'约[^<]*', info.decode())
    print('{}结果'.format(match.group()))


if __name__ == '__main__':
    main()