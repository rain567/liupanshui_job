from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import pandas as pd
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': UserAgent().random
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def main():
    # 返回列表
    list_response = []
    # 地址
    url = 'https://movie.douban.com/chart'
    # 请求并获取返回值
    info = get_html(url).decode()
    soup = BeautifulSoup(info, 'lxml')
    for sibling in soup.find_all('div', class_='pl2'):
        data = {}
        title = ""
        for string in sibling.a.stripped_strings:
            string = string.replace(' ', '')
            string = string.replace('\n', '')
            title += string
        print('电影标题：' + title, end='')
        data['标题'] = title
        for span in sibling.find_all('span', class_='rating_nums'):
            data['评分'] = span.string
        for p in sibling.find_all('p', class_='pl'):
            data['详情'] = p.string
        list_response.append(data)
    return list_response


def save_file(data):
    # 保存数据集
    pd.DataFrame(data).to_csv('豆瓣新片排行榜1.csv')


if __name__ == '__main__':
    data = main()
    save_file(data)
