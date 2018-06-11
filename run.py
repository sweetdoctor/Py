# @Time    : 2018/5/30 7:52
# @Author  : Scorpion

from jobspider51 import main

from db import MysqlOperator


def setup():
    try:
        mysql = MysqlOperator()
        for i in range(174, 230):
            print('正在抓取第%s页' % i)
            for item in main(i):
                try:
                    position = item['position']
                    company = item['company']
                    salary = item['salary']
                    workcity = item['workcity']
                    work_experience = item['work-experience']
                    qualification = item['qualification']
                    advantage = item['advantage']
                    detailed_addr = item['detailed-adddress']
                    description = item['description']
                    url = item['link_url']
                    mysql.insert_table(position, company, advantage, salary, workcity, work_experience, qualification, detailed_addr, description, url)
                except Exception:
                    pass
    except Exception:
        pass
if __name__ == '__main__':
    setup()