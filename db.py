# @Time    : 2018/5/26 10:31
# @Author  : Scorpion
#coding:utf-8
import pymysql
import re
import pickle

class MysqlOperator(object):
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', charset='utf8')
        self.cursor = self.db.cursor()
        self.cursor.execute('use jobinfo')

    # `ID` INT UNSIGNED AUTO_INCREMENT,primary key (`COMPANY`)
    def create_table(self):
        sql = '''
                CREATE TABLE if not exists  `blockchain`(
                `id` int not null auto_increment,
                `POSITIONTYPE` VARCHAR(100) ,
                `COMPANY` VARCHAR(100) ,
                `ADVANGAGE` VARCHAR(200) ,
                `SALARY` varchar(100) ,
                `WORKCITY` varchar(100) ,
                `WORKEXPERIENCE` varchar(100) ,
                `QUALIFICATION` varchar(100) ,
                `DETAILEDADDRESS` varchar(100) ,
                `DESCRIPTION` VARCHAR(1000) ,
                `DETAILEDURL` varchar(100),
                primary key (`id`)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        '''
        test = """
            CREATE TABLE `runoob_tbl`(
            `runoob_id` INT UNSIGNED AUTO_INCREMENT,
            `runoob_title` VARCHAR(100) NOT NULL,
            `runoob_author` VARCHAR(40) NOT NULL,
            `submission_date` DATE,
             PRIMARY KEY ( `runoob_id` )
              )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        # self.cursor.execute('use jobinfo')
        self.cursor.execute(sql)
        # self.db.close()

    def insert_table(self, position, company, advantage, salary, workcity, workexperience, qualification, detailed_addr, description, url):
        sql = """
                INSERT INTO blockchain(POSITIONTYPE, COMPANY, ADVANGAGE, SALARY, WORKCITY, WORKEXPERIENCE, QUALIFICATION, DETAILEDADDRESS, DESCRIPTION, DETAILEDURL
                ) VALUES  ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')on DUPLICATE key  UPDATE COMPANY=company""" % (position, company, advantage, salary, workcity, workexperience, qualification, detailed_addr, description, url)
#on DUPLICATE key  UPDATE COMPANY='2'
        try:
            # self.cursor.execute('use jobinfo')
            self.cursor.execute(sql)
            self.db.commit()
            print('success to insert')
        # self.db.close()
        except Exception as e:
            # print(e)
            print('Repeat !failed to insert')
            pass

    def delete_table(self):
        # self.cursor.execute('use jobinfo')
        sql = "DROP TABLE 51NEINFO"
        self.cursor.execute(sql)
    def query(self):
        self.cursor.execute('select * from 51NEINFO')


class QueryCount(MysqlOperator):
    def __init__(self):
        super().__init__()

    def get_city_number(self):
        unified_position = {}
        sql = """
                select workcity from NETWORRPOSITION group by workcity having count(*)>=1
        """
        self.cursor.execute(sql)
        cities = self.cursor.fetchall()
        cities = [city[0] for city in cities]
        print(cities)
        # self.cursor.execute("select workcity from 51neinfo where workcity='广州'")
        # print(self.cursor.rowcount)
        total_number = 0
        for city in cities:
            # print(city)
            sql_query = "select * from NETWORRPOSITION where workcity='%s'" % city
            self.cursor.execute(sql_query)
            counts = self.cursor.rowcount
            unified_position[city] = counts
            total_number += counts
            print(city, counts)
        pickle.dump(unified_position, open('position_number', 'wb'))
        print(unified_position)

    def unified_workcity(self):
        # reg = '(.*?)-(.*)'
        cities_query = """
                    select workcity from NETWORRPOSITION where workcity regexp '(.*?)-(.*)'
        """
        self.cursor.execute(cities_query)
        cities = [city[0] for city in self.cursor.fetchall()]
        print(cities)
        for city in cities:
            # matter = re.match(reg, city)
            # if matter:
            #     self.cursor.execute(update_sql % city )
            self.cursor.execute("update NETWORRPOSITION set workcity='%s' where workcity='%s'" % (city.split('-')[0], city))
            self.db.commit()

    def workexperience_require(self):
        sql = """
                SELECT workexperience FROM jobinfo.networrposition group by workexperience having count(workexperience)>=1
        """
        wq = {}
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        print(tmp)
        for i in tmp:
            self.cursor.execute("select count(*) from networrposition where workexperience='%s'" % (i[0]))
            number = self.cursor.fetchall()[0][0]
            wq[i[0]] = number
            print(number, i)
        print(wq)
        pickle.dump(wq, open('experience', 'wb'))

    def edu_requirment(self):
        sql = """
                        SELECT QUALIFICATION FROM jobinfo.networrposition group by QUALIFICATION having count(QUALIFICATION)>=1
                """
        wq = {}
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        print(tmp)
        for i in tmp:
            self.cursor.execute("select count(*) from networrposition where QUALIFICATION='%s'" % (i[0]))
            number = self.cursor.fetchall()[0][0]
            wq[i[0]] = number
            print(number, i)
        print(wq)
        pickle.dump(wq, open('edu_requirment', 'wb'))

    def filter_salary(self):
        reg = '(.*?)-(.*?)千/月'
        sql = """
                    select salary from networrposition where salary like '%千/月%'
        """
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        tmp = [s[0] for s in tmp]
        print(tmp)
        # a = ['1.5-2万/月', '1.5-2万/月']
        for s in tmp:
            lower = eval(re.match(reg, s).group(1))
            higher = eval(re.match(reg, s).group(2))
            new = ''.join((str(lower),'k','-',str(higher),'k'))
            print(new)
            self.cursor.execute("update networrposition set salary='%s' where salary='%s'" %(new, s))
            self.db.commit()

    def calculate_salary(self):
        salary_d = {}
        city_query = """
                select workcity from networrposition group by workcity having count(workcity)>20
        """
        salary_sql = """
                select salary from networrposition where salary not in (select salary from networrposition where salary regexp '[万/年天]') and workcity='%s'
        """
        self.cursor.execute(city_query)
        cities = self.cursor.fetchall()
        cities = [city[0] for city in cities]
        print(cities)
        for city in cities:
            self.cursor.execute(salary_sql % city)
            s= self.cursor.fetchall()
            s = [singl_s[0] for singl_s in s]
            # print(s)
            for i, p in enumerate(s):
                # print(i, type(i))
                if p == '':
                    s.remove('')
                if not re.match('(.*?)k-(.*?)k', p):
                    del s[i]
                if '-' not in p:
                    del s[i]
            # print(city, s)
            min_salary, max_salary = 0, 0
            for i, salary in enumerate(s):
                try:
                    min, max = salary.split('-')
                except Exception:
                    continue
                min_salary += eval(min[:-1])
                max_salary += eval(max[:-1])
                # print(len(salary))
            # if salary == 0:
            #     continue
            #     if i == len(salary):
            #         try:
            #             print(city, min_salary/len(salary), max_salary/len(salary), )
            #         except Exception:
            #             pass
            # print(city, min_salary / len(salary), max_salary / len(salary), )
            max_average = round(max_salary/len(s), 2)
            min_average = round(min_salary/len(s), 2)
            average = round((max_average+min_average)/2, 2)
            salary_d[city] = [min_average, max_average, average]
            print(city, min_average, max_average,average)
        pickle.dump(salary_d, open('salary', 'wb'))

    def calculate_lagou_salary(self):
        salary_d = {}
        city_query = """
                        select workcity from blockchain group by workcity having count(workcity)>=1
                """
        salary_sql = """
                        select salary from blockchain where workcity='%s'
                """
        self.cursor.execute(city_query)
        cities = self.cursor.fetchall()
        cities = [city[0] for city in cities]
        print(cities)
        for city in cities:
            self.cursor.execute(salary_sql % city)
            s = self.cursor.fetchall()
            s = [singl_s[0] for singl_s in s]
            # print(s)
            for i, p in enumerate(s):
                # print(i, type(i))
                if p == '':
                    s.remove('')
                if not re.match('(.*?)k-(.*?)k', p):
                    del s[i]
                if '-' not in p:
                    del s[i]
            # print(city, s)
            min_salary, max_salary = 0, 0
            for i, salary in enumerate(s):
                try:
                    min, max = salary.split('-')
                except Exception:
                    continue
                min_salary += eval(min[:-1])
                max_salary += eval(max[:-1])
            max_average = round(max_salary / len(s), 2)
            min_average = round(min_salary / len(s), 2)
            average = round((max_average + min_average) / 2, 2)
            salary_d[city] = [min_average, max_average, average]
            print(city, min_average, max_average, average)
        pickle.dump(salary_d, open('salary', 'wb'))

    def requird_descriment(self):
        sql = """
                select description from net 
        """

        self.cursor.execute(sql)
        des = self.cursor.fetchall()
        des = [i[0] for i in des]
        # for d in des:
        #     print(d)
        #     d.encode()
        import json
        a = json.dumps(des, ensure_ascii=False)
        # print(a)
        with open('description.txt', 'a', encoding='utf-8') as f:
            f.write(a)
    def get_table(self):
        sql = """
                select * from blockchain
        """
        self.cursor.execute(sql)
        info = self.cursor.fetchall()
        for i in info:
            yield i

if __name__ == '__main__':
    mysql = MysqlOperator()
    # mysql.create_table()
    # mysql.delete_table()
    # mysql.insert_table('1', '1', '1', '1', '1', '1', '1', '1', '4', '1')
    # mysql.query()
    q = QueryCount()
    # q.get_city_number()
    # q.unified_workcity()
    # q.workexperience_require()
    # q.edu_requirment()
    # q.salary_requirment()
    # q.calculate_salary()
    # q.requird_descriment()
    # print(type(q.get_table()))
    q.calculate_lagou_salary()