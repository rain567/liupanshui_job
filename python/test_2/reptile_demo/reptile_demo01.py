# coding=utf-8
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json


def get_html(url, page):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://www.lpssy.edu.cn/_web/leadermail/initLookReplies.do?_p=YXM9MyZ0PTI0MSZwPTEmbT1OJg__&leaderMailBoxId=5&request_locale=zh_CN&localeCH=true'
    }
    data = {
        'page': page,
        'rows': 10,
        'pwd': '',
    }
    request = Request(url, headers=headers, data=urlencode(data).encode())
    response = urlopen(request)
    return response.read()


def save_html(filename, html_bytes):
    with open(filename, 'wb') as f:
        f.write(html_bytes)


def main():
    # for index in range(10):
    #     info = get_html('http://www.lpssy.edu.cn/_web/leadermail/lookReplyMail.do?_p=YXM9MyZ0PTI0MSZwPTEmbT1OJg__&tt=0.017348217914192166&localeCH=true&request_locale=zh_CN&leaderMailBoxId=5', index)
    #     save_html('第{}页.json'.format(index), info)

    for index in range(10):
        with open('第{}页.json'.format(index), 'r', encoding='utf-8') as file:
            # print(file.read())
            json_dict = json.load(file, encoding='urf-8')
            for row in json_dict['rows']:
                print(row['content'])


if __name__ == '__main__':
    main()