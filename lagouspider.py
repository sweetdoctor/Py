
# @Time    : 2018/5/31 10:06
# @Author  : Scorpion

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from db import MysqlOperator
from multiprocessing import Process


class LagouSpider(object):
    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)chrome_options=chrome_options
        self.driver = webdriver.Chrome()
        self.mysql = MysqlOperator()

    def login(self, url):
        self.driver.get(url)

        username = self.driver.find_element_by_xpath('//input[@type="text"]')
        username.click()
        username.send_keys('13643551349')
        passwd = self.driver.find_element_by_xpath('//input[@type="password"]')
        passwd.click()
        passwd.send_keys('bendan12')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search_input"]')))[0]
        # input = self.driver.find_element_by_xpath('//*[@id="search_input"]')
        element.click()
        element.send_keys('区块链工程师')
        self.driver.find_element_by_xpath('//*[@id="search_button"]').click()
        # self.driver.close()

    def get_all_urls(self, page_counts):
        # for singl_page_number in range(1, 31):
        all_links = []
        for i in range(page_counts):
            time.sleep(1)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            detailed_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="s_position_list"]//a[@class="position_link"]')))
            detailed_links = [url.get_attribute('href') for url in detailed_links]
            all_links.extend(detailed_links)
            next = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@action="next"]')))[0]
            next.click()
        print(all_links)
        return all_links
        # for singl_link in detailed_links:
        #     singl_link.get_attribute('href')

    def parse_detail_page(self, url):
        job_info = {}
        self.driver.get(url)
        try:
            job_info['position'] = self.driver.find_element_by_xpath('//div[@class="job-name"]').get_attribute('title')
            job_info['company_name'] = self.driver.find_element_by_xpath('//div[@class="company"]').text
            job_info['salary'] = self.driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[1]').text
            work_city = self.driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[2]').text
            job_info['work_city'] = work_city.replace('/', '').strip()
            job_info['work_experience'] = self.driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[3]').text.replace('/', '').strip()
            job_info['qualifications'] = self.driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[4]').text.replace('/', '').strip()
            job_info['nature_of_job'] = self.driver.find_element_by_xpath('//dd[@class="job_request"]/p//span[5]').text
            job_info['job_advantage'] = self.driver.find_element_by_xpath('//dd[@class="job-advantage"]/p').text
            description = self.driver.find_elements(By.XPATH, '//dd/div[1]//p')
            job_info['description'] = ''.join([i.text for i in description])
            job_info['work_addr'] = self.driver.find_element_by_xpath('//div[@class="work_addr"]').text[:-4]
            job_info['current-url'] = url
        except Exception:
            pass
        # self.driver.close()
        print(job_info)
        return job_info
    def insert_to_mysql(self, job_info):
        # print(job_info)
        self.mysql.insert_table(job_info['position'], job_info['company_name'], job_info['job_advantage'], job_info['salary'], job_info['work_city'], job_info['work_experience'], job_info['qualifications'], job_info['work_addr'], job_info['description'], job_info['current-url'])
        print('succeful')

    def run(self, page_counts):
        self.login('https://passport.lagou.com/login/login.html?ts=1527763232761&serviceId=lagou&service=https%253A%252F%252Fwww.lagou.com%252F&action=login&signature=5885A25E094F23439B45E3603255B9AB')
        # for i in range(29):
        for url in self.get_all_urls(page_counts):
            self.insert_to_mysql(self.parse_detail_page(url))



if __name__ == '__main__':
    lagou = LagouSpider()
    # pool = Pool(processes=4)
    # pool.map(lagou.run(), [for ])
    # Process(target=lagou.run, args=(1,)).start()
    # Process(target=lagou.run, args=(1,)).start()

    lagou.run(30)
