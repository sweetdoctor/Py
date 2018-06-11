# @Time    : 2018/5/28 4:45
# @Author  : Scorpion
import requests
import re
from config import USER_AGENT
from urllib.parse import urlparse
import aiohttp
import asyncio
from asyncio import TimeoutError
import time
import pickle

valid_ip = []

def get_xici_proxies():
    url = 'http://www.xicidaili.com/'
    html = requests.get(url, headers={'User-Agent': USER_AGENT}, allow_redirects=False).text
    regular_regex = '<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td class="country">(.*?)</td>\s*<td>(.*?)</td>'
    pattern = re.compile(regular_regex, re.I)
    ip_proxies = pattern.findall(html)
    # print(ip_proxies)
    # ip_proxies = [ip for ip in ip_proxies if ip.startswith('http')]
    for ip_proxy in ip_proxies:
        ip = ip_proxy[0]
        port = ip_proxy[1]
        # protocal_type = ip_proxy[4].lower()
        # print(ip, port)
        yield ':'.join((ip, port))


async def ip_check(ip):
    global valid_ip
    if ip:
        print('检测当前%s' % ip)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.baidu.com/', proxy=''.join(('http://', ip)), headers={'User-Agent': USER_AGENT}, timeout=3) as response:
                    if response.status == 200:
                        if ip not in valid_ip:
                            valid_ip.append(ip)
                            print('代理有效', ip)
        except TimeoutError as e:
            print('无效代理')
            if ip in valid_ip:
                del valid_ip[ip]
                print('删除无效ip', ip)
        except Exception as e:
            print(e)

def test_ip(ips):
    try:
        loop = asyncio.get_event_loop()
        task = [asyncio.ensure_future(ip_check(ip)) for ip in ips]
        loop.run_until_complete(asyncio.wait(task))
    except Exception as e:
        pass

    pickle.dump(valid_ip, open('ip_proxies', 'wb'))

def main():
    while True:
        test_ip(get_xici_proxies())
        # print(valid_ip)
        # while True:
        #         if len(valid_ip) <= 5:
        #             break
        #             # test_ip(get_xici_proxies())
        #         time.sleep(60)
        #         test_ip(valid_ip)
        # print(valid_ip)
        time.sleep(60)


if __name__ == '__main__':
    # del valid_ip[:]
    main()
    # crawl_ip = [urlparse(ip)[1] for ip in get_xici_proxies()]
    # a = crawl_ip.index('')
    # print(a)
    # test_ip(get_xici_proxies())
    # print(valid_ip)
    # test_ip(('http://1.196.161.241:9999'))
    # for ip in get_xici_proxies():
    #     print(ip)