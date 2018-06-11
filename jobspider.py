import requests
import json
import re
from lxml import etree
from config import USER_AGENT
import random
import time
import pickle
import redis
#, proxies={'http': 'https://'+get_proxy_ip()}
headers = {
    'Host': 'www.lagou.com',
    # 'Origin': 'https://www.lagou.com',
    # 'Referer': 'https://www.lagou.com/jobs/list_%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
    'User-Agent': USER_AGENT
}


# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# def get_proxy_ip():
#     global r
#     proxies = r.sunion('http', 'https')
#     return list(proxies)[random.randint(0, len(proxies)-1)]
# valid_ip = pickle.load(open('ip_proxies', 'wb'))
# ip= valid_ip[random.randint(0, len(valid_ip))]
# proxy = {
#     # 'http': valid_ip[random.randint(0, len(valid_ip)-1)]
#     'http': ip,
#     'https': ip
# }

def get_page_source(url):

    try:
        session = requests.Session()
        response = session.get(url, headers=headers, allow_redirects=False)
        time.sleep(random.random())
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('failed')
    except Exception:
        time.sleep(random.randint(3, 6))
        get_page_source(url)


def get_html():
    for i in range(1, 31):
        url = 'https://www.lagou.com/zhaopin/wangluogongchengshi/{}/?filterOption=3'.format(i)
        time.sleep(random.random())
        yield get_page_source(url)

def get_detail_url(html):
    try:
        selector = etree.HTML(html)
    except Exception:
        pass

    urls = selector.xpath('//*[@id="s_position_list"]//a[@class="position_link"]/@href')
    # for url in urls:
    #     yield url
    return urls


def parse_detail_page(html):
    job_info = {}
    try:
        selector = etree.HTML(html)
    except Exception:
        pass

    try:
        job_info['position'] = selector.xpath('//div[@class="job-name"]/@title')[0]
        job_info['company_name'] = selector.xpath('//div[@class="company"]/text()')[0]
        job_info['job_request'] = selector.xpath('//dd[@class="job_request"]/p//span/text()')
        job_info['salary'] = job_info['job_request'][0].strip()
        job_info['work_city'] = job_info['job_request'][1].strip()
        job_info['work_experience'] = job_info['job_request'][2].strip()
        job_info['qualifications'] = job_info['job_request'][3].strip()
        job_info['nature_of_job'] = job_info['job_request'][4].strip()
        job_info['job_advantage'] = selector.xpath('//dd[@class="job-advantage"]/p/text()')[0]
        job_info['work_addr'] = ''.join(selector.xpath('//div[@class="work_addr"]//a/text()')[:-1]) + \
                    selector.xpath('//div[@class="work_addr"]/text()')[-2].strip()[1:]
        description = selector.xpath('//dd/div[1]//p/text()')
        job_info['description'] = ''.join(description)
    except Exception:
        pass

    # job_info = {
    #     'position': position,
    #     'company': company_name,
    #     'salary': salary,
    #     'workcity': work_city,
    #     'work-experience': work_experience,
    #     'qualification': qualifications,
    #     'full-time or part-time job': nature_of_job,
    #     'advantage': job_advantage,
    #     'detailed-adddress': work_addr,
    #     'description': description,
    # }
    print(job_info)
    return job_info


def main():
    for html in get_html():
        for url in get_detail_url(html):
            parse_detail_page(get_page_source(url))


if __name__ == '__main__':

    # main()
    for html in get_html():
        url = get_detail_url(html)
        print(url)