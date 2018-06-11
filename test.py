# import requests
# from lxml import etree

# r = requests.get('https://www.lagou.com/jobs/4628466.html', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})
# # with open('test.html', 'w', encoding='utf-8') as f:
# #     f.write(r.text)
#
#
# selector = etree.HTML(r.text)
# # selector = etree.HTML(open('test.html', 'r', encoding='utf-8').read())
#
# position = selector.xpath('//div[@class="job-name"]/@title')[0]
# print(position)
# company_name = selector.xpath('//div[@class="company"]/text()')[0]
# print(company_name)
# job_request = selector.xpath('//dd[@class="job_request"]/p//span/text()')
# print(job_request)
#
#
# job_advantage = selector.xpath('//dd[@class="job-advantage"]/p/text()')[0]
# print(job_advantage)
#
# work_city = selector.xpath('//div[@class="work_addr"]/a[1]/text()')[0]
# print(work_city)
#
# work_addr = ''.join(selector.xpath('//div[@class="work_addr"]//a/text()')[:-1])+selector.xpath('//div[@class="work_addr"]/text()')[-2].strip()[1:]
# print(work_addr)
#
# description = selector.xpath('//dd/div[1]//p/text()')
# description = ''.join(description)
# print(description)

# post_data = {
#     'first': 'false',
#     'pn': 10,
#     'kd': '网络工程师',
# }
#
# headers = {
#     'Host': 'www.lagou.com',
#     'Origin': 'https://www.lagou.com',
#     'Referer': 'https://www.lagou.com/jobs/list_%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
#     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12'
# }
#
# # session = requests.Session()
# response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', data=post_data, headers=headers)
# print(response.text)


# a = '12345'
# i = a.index('5')
# print(i)

# if 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25BD%2591%25E7%25BB%259C%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,11.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.startswith('https://search.51job.com/list'):
#     print('jkjklj')
# print(list(set({2,3,4,5})))
# w = ''.join(('http://', 'jjjjj'))
# print(w)

# import requests
# from config import USER_AGENT
# # from ipproxy import valid_ip
# valid_ip = ['114.217.98.235:24960', '115.221.127.49:39831', '106.111.45.69:61234', '118.212.137.135:31288', '183.132.115.100:49862', '106.110.241.147:61234', '123.171.27.36:808', '1.198.13.174:36140', '114.215.95.188:3128', '140.250.162.136:24366', '118.81.67.244:9797', '117.36.103.170:8118', '183.135.250.68:21377', '118.81.70.49:9797', '123.163.161.240:24841', '218.28.58.150:53281', '115.215.57.24:22898']
#
# print(requests.get('http://httpbin.org/ip', headers={'User-Agent': USER_AGENT}, proxies={'http': valid_ip[2]}).text)


import aiohttp

# import pickle
# from config import USER_AGENT
#
# x = pickle.load(open('ip_proxies', 'rb'))
# proxy = {
#
#     'http': x[1],
#     'https': x[1]
# }
#
# response = requests.get('http://httpbin.org/ip', headers={'User-Agent': USER_AGENT}, proxies=proxy)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(response.status_code)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
#
# driver.get('https://www.lagou.com/jobs/4437758.html')
# # position = driver.find_element_by_xpath('//div[@class="job-name"]').get_attribute('title')
# # companyname = driver.find_element_by_xpath('//div[@class="company"]').text
# # salary = driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[1]').text
# work_city = driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[2]').text.replace('/', '').strip()
# work_experience = driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[3]').text.replace('/', '').strip()
# qualifications = driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[4]').text.replace('/', '').strip()
# nature_of_job = driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[5]').text
# job_advantage = driver.find_element_by_xpath('//dd[@class="job-advantage"]/p').text
# description = driver.find_elements(By.XPATH, '//dd/div[1]//p')
# description = ''.join([i.text for i in description])
# # work_addr = driver.find_elements(By.XPATH, '//div[@class="work_addr"]//a')
# # work_addr = [i.text for i in work_addr][:-1]
# work_addr = driver.find_element_by_xpath('//div[@class="work_addr"]').text[:-4]
# # print(work_addr)
# print(work_city, work_experience, qualifications, nature_of_job, job_advantage, description, work_addr)
# # print(description)

# class A():
#     def __init__(self):
#         # print('aaaaaa')
#         self.a = 2
# class B(A):
#     def __init__(self):
#         # super().__init__()
#         pass
# b = B()
# print(b.a)
#
# from fake_useragent import UserAgent
# ua = UserAgent()
#
# code = requests.get('https://www.baidu.com', headers={'User-Agent': ua.random})

# import re
# s = '北京-朝阳区'
#
# reg = '(.*?)-(.*)'
# matter = re.match(reg, s)
# if matter:
#     print(matter.group(1), matter.group(2))
#     print('successful')

#
#
# s = [4,3,2,1]
# print()  #升序， 不改变
# print(s)
# for i in (2,3,4,5):
#     print(i)
# print((2,3,4,5)[0])

# from matplotlib import pyplot as plt
# import pickle
# # print(sorted({'a':2, 'b':5}))
# from pylab import mpl
#
# mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# cities = []
# position_number = []
# dic = pickle.load(open('position_number', 'rb'))
# print(dic['太原'])
# uni_list = sorted(zip(dic.values(), dic.keys()))[-19:]
# print(type(uni_list))
# print(uni_list)
# for p in uni_list:
#     # print(type(p))
#     # break
#     cities.append(p[1])
#     position_number.append(p[0])
# cities.insert(0, '太原')
# position_number.insert(0, dic['太原'])
# print(cities)
# print(position_number)
#
#
# plt.figure(figsize=(10,6))
# # fig.tight_layout()  # 调整整体空白
# # plt.subplots_adjust(wspace=20, hspace=0)  # 调整子图间距
# plt.style.use('ggplot')
# plt.title('全国热门城市职位需求数(网络工程师)')
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.xlabel('城市名称')
# plt.ylabel('需求数职位数')
# # plt.xticks(range(len(cities)), cities)
# plt.bar(cities, position_number, color="#87CEFA")
# for x, y in zip(cities, position_number):
#     plt.text(x, y+60,'%s' % y, ha='center', va='top')
# plt.savefig('position.svg')
# plt.show()
import re
# if __name__ == '__main__':
#
#    s = '1-2万/月'
#    ma = re.match('(.*?)-(.*?)万/月', s)
#    print(ma.group(2))
#     if re.match('(.*?)k-(.*?)k', '3232k-343k'):
#         print('jkjk')
#     s = '22k-22.0'.split('-')
#     print(s)
# [2,3,4].append(2.33)
import pickle
#
# s = open('description', 'r', encoding='utf-8')
# print(lens.read())
# import sys
# print(sys.getdefaultencoding())

#
# s = [1,2,3,4, 4,5]
#
# s.remove(4)
# print(s)

for i in range(0, 101, 10):
    print(i)