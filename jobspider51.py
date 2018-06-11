

import requests
from lxml import etree
from config import USER_AGENT
import random
import re
import multiprocessing


headers = {
    'User-Agent': USER_AGENT[random.randint(0, len(USER_AGENT)-1)]
}
base_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25BD%2591%25E7%25BB%259C%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?'
query_string = 'lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

failed_base_urls = []
failed_detail_urls = []

def get_detial_url(page_number):
    # for i in range(1, page_number):
    start_url = ''.join([base_url.format(page_number), query_string])
    # get_detial_url(start_url)
    # response = requests.get(start_url, headers=headers)
    # response.encoding = 'gb2312'
    selector = etree.HTML(get_page_source(start_url))
    detial_url = selector.xpath('//span//a[@target="_blank"]/@href')
    detial_url = [url for url in detial_url if url.endswith('s=01&t=0')]
    for single_url in detial_url:
        yield single_url


def get_page_source(url):
    while True:
        # try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.encoding = 'gb2312'
        # except Exception as e:
        #     print(e)
        #     if url.startswith('https://search.51job.com/list'):
        #         failed_base_urls.append(url)
        #         print(url)
        #     if url.endswith('s=01&t=0'):
        #         failed_detail_urls.append(url)
        #         print(url)
        #     pass
        if response.status_code == 200:
            break
    return response.text


def parse_detail_page(page_source, url):
    # res = requests.get(url, headers=headers)
    # res.encoding = 'gb2312'
    try:
        selector = etree.HTML(page_source)
        position = selector.xpath('//div[@class="cn"]/h1/text()')[0]
        work_city = selector.xpath('//div[@class="cn"]/span[1]/text()')[0]
        company = selector.xpath('//div[@class="cn"]/p/a/text()')[0]
        try:
            salary = selector.xpath('//div[@class="cn"]/strong/text()')[0]
        except Exception:
            salary = ''
        position_info = selector.xpath('//div[@class="t1"]/span[position()<6]/text()')
        work_experience = position_info[0]
        qualifications = '' if re.search('\d+', position_info[1]) else position_info[1]
        # qualifications = position_info[1]
        # recruit_person = position_info[2]
        # public_time = position_info[3]
    except Exception :
        pass
    try:
        job_advantage = selector.xpath('//p[@class="t2"]/span/text()')
        job_advantage = '、'.join(job_advantage)
        description = selector.xpath('//div[@class="bmsg job_msg inbox"]//text()')
        description = re.sub('\s+', '', ''.join(description))
        work_addr = selector.xpath('//div[@class="bmsg inbox"]/p/text()')[1].strip()
    except Exception:
        pass
    try:
        job_info = {
            'link_url': url,
            'position': position,
            'company': company,
            'salary': salary,
            'workcity': work_city,
            'work-experience': work_experience,
            'qualification': qualifications,
            #'full-time or part-time job': nature_of_job,
            'advantage': job_advantage,
            'detailed-adddress': work_addr,
            'description': description,
        }
    except Exception:
        return None
    # print(job_info)
    return job_info


def main(page_number):
    for detail_url in get_detial_url(page_number):
        yield parse_detail_page(get_page_source(detail_url), detail_url)
        # print(parse_detail_page(get_page_source(detail_url), detail_url))

# def muti_precess(process_number, page_numbers):
#     pool = multiprocessing.Pool(processes=process_number)
#     pool.map(main, [i for i in range(1, page_numbers)])

# if __name__ == '__main__':
    # muti_precess(2,2)
