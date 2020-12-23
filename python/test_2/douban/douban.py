from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import quote
import json
import time
import random
import pandas as pd

# 爬取的类型
tags = '电影'


def get_html(url):
    headers = {
        'User-Agent': UserAgent().random
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def main():
    # 爬取页数
    index = 0
    # 爬取次数
    crawling_time = 5
    # 返回列表
    list_response = []
    while True:
        # 地址
        url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags={}&start={}'\
            .format(quote(tags), index * 20)
        # 请求并获取返回值
        info = get_html(url)
        data = json.loads(info.decode())['data']
        # 将内容加入到返回列表中
        list_response.extend(data)
        for item in data:
            print('电影：{}，评分：{}'.format(item['title'], item['rate']))
        # 判断次数达到或者全部爬取完之后返回
        if len(data) < 20 or index == crawling_time:
            print('爬取完成,共爬取{}条数据,爬取{}次'.format(len(list_response), index))
            return list_response
        index += 1
        # 爬取之后随便等待秒数，防止被程序识别。爬取次数多时请使用
        # time.sleep(random.randint(0, 2))


def save_file(data):
    # 保存数据集
    pd.DataFrame(data).to_csv(tags + '.csv')


if __name__ == '__main__':
    data = main()
    save_file(data)
