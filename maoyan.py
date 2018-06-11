# -*- coding:utf-8 -*-
# @Time    : 2018/6/9 10:30
# @Author  : Scorpion


import requests
# import re
from lxml import etree
import xlwt
from config import USER_AGENT

headers = {
'Host': 'maoyan.com',
'Pragma': 'no-cache',
'Referer': 'http://maoyan.com/board/4?offset=10',
'User-Agent': USER_AGENT
}

def get_html(offset):
    url = 'http://maoyan.com/board/4?offset={}'.format(offset)
    response = requests.get(url, headers=headers)
    # print(response.text)
    response.encoding = 'utf-8'
    return response.text

def parse_html(html):
    selector = etree.HTML(html)
    dds = selector.xpath('//dl[@class="board-wrapper"]//dd')
    # print(dds)
    for d in dds:
        d= etree.HTML(etree.tostring(d))
        title = d.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a')[0].text
        actors = d.xpath('//p[@class="star"]')[0].text
        time = d.xpath('//p[@class="releasetime"]')[0].text
        yield {
            'title': title.strip(),
            'actors': actors.strip(),
            'releasetime': time.strip(),
        }
if __name__ == '__main__':
    colunms = ['title', 'actors', 'releasetime']
    book = xlwt.Workbook(encoding='utf-8')
    table = book.add_sheet('电影top100')
    for i, v in enumerate(colunms):
        table.write(0, i, v)
    count = 1
    for offset in range(0, 101, 10):
        html = get_html(offset)
        for item in parse_html(html):
            for i, k in enumerate(item.values()):
                table.write(count, i, k)
            count += 1
    book.save('movietop.xls')
