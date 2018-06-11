# @Time    : 2018/6/3 12:35
# @Author  : Scorpion

from matplotlib import pyplot as plt
import pickle
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def plot_line_chart():
    salary = pickle.load(open('salary', 'rb'))
    # del salary['四川省']
    # print(salary)
    cities = []
    max_salary = []
    min_salary = []
    average_salary = []
    for city in salary:
        cities.append(city)
        min_salary.append(salary[city][0])
        max_salary.append(salary[city][1])
        average_salary.append(salary[city][2])
    # print(min_salary, max_salary, average_salary)
    # print(cities, max_salary, average_salary)

    plt.figure(figsize=(20, 8))
    plt.style.use('ggplot')
    plt.title('全国部分城市区块链工程师月薪统计图')
    plt.xlabel('城市名称')
    plt.ylabel('月薪(单位：千)')
    # plt.yticks([3, 4, 5, 6, 7, 8, 9, 10], ['$3k$', '$4k$', '$5k$', '$6k$', '$7k$', '$8k$', '$9k$', '$10k$'])
    plt.yticks([5, 10, 15, 20, 25, 30, 35, 40], ['$5k$', '$10k$', '$15k$', '$20k$', '$25k$', '$30k$', '$35k$', '$40k$'])
    # plt.plot(cities, max_salary, color='r', label='jkjk')
    # plt.plot(cities, min_salary, color='b')
    plt.plot(cities, average_salary, 'b', lw=2, label='月薪')
    plt.legend()
    plt.savefig('salary.png')
    plt.show()

def get_pie_chart():
    """
    ('本科', 2394)
('大专', 5137)
('', 1634)
('中专', 321)
('中技', 62)
('招若干人', 491)
('高中', 130)
('硕士', 19)
('初中及以下', 10)
('本科及以上', 217)
('大专及以上', 190)
('学历不限', 33)
('硕士及以上', 1)
    :return:
    """
    # qf = pickle.load(open('edu_requirment', 'rb'))
    # qf['本科'] += qf['本科及以上']
    # qf['大专'] += qf['大专及以上']
    # qf['不限'] = qf['初中及以下'] + qf['学历不限']
    # qf['硕士以上'] = qf['硕士'] + qf['硕士及以上']
    # qf['中专'] = qf['中专'] + qf['中技']
    # del qf['本科及以上']
    # del qf['大专及以上']
    # del qf['招若干人']
    # del qf['']
    # del qf['初中及以下']
    # del qf['学历不限']
    # del qf['硕士']
    # del qf['硕士及以上']
    # del qf['中技']
    # print(qf)
    # q_type = []
    # q_number = []
    # t= 0
    # for k, v in qf.items():
    #     q_type.append(k)
    #     q_number.append(v)
    #     t += v
    # q_percent = [round(i/t, 3) for i in q_number]
    # # print(q_type, q_number)
    # plt.figure(figsize=(10,6))
    # print(plt.style.available)
    # plt.style.use('bmh')
    # plt.ylim(0, 1, 5)
    # # plt.title('全国热门城市职位需求数(网络工程师)')
    # ax = plt.gca()
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.yticks(q_percent, ['$30.7%$', '$62.6%$', '$4.5%$', '$1.5%$', '$0.5%$', '$0.2%$'])
    # # plt.xlabel('城市名称')
    # # plt.ylabel('需求数职位数')
    # plt.bar(q_type, q_percent, color="#87CEFA")
    # for x, y in zip(q_type, q_number):
    #     plt.text(x, y+120, '%s' % y, ha='center', va='top')
    # # plt.savefig('position.svg')
    # plt.show()
    plt.style.use('ggplot')
    labels = ['本科', '大专', '中专', '其它']
    sizes = [2611, 5327, 383, 193]
    explode = (0, 0, 0, 0.5)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # explode=explode,

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.title('学历概况')
    ax1.axis('equal', title='kjk')

    plt.savefig('edu_exp')
    plt.show()
def get_pie_chart1():
    we = pickle.load(open('experience', 'rb'))
    print(we)
    labels = ['本科', '大专', '中专', '高中', '不限', '硕士以上']
    sizes = [2611, 5327, 383, 130, 43, 20]
    explode = (0, 0, 0, 1, 1, 1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # explode=explode,
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

def get_worke_char():
    # s = pickle.load(open('experience', 'rb'))
    # print(s)
    # [(2,2166),(1,2239),(34,2000),(wu,4183),(wushang,364)]
    a = plt.style.available
    print(a)
    # plt.style.use('ggplot')
    labels = ['1年经验', '2年经验', '3-4年经验', '实习', '4年以上']
    sizes = [2239, 2166, 2000, 4183, 364]
    explode = (0, 0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # explode=explode,
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('工作经验概况')
    plt.savefig('experience.png')
    plt.show()

def sperate_words():
    pass


if __name__ == '__main__':
    plot_line_chart()
    # get_pie_chart()
    # get_worke_char()

