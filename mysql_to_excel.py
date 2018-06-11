# @Time    : 2018/6/5 11:41
# @Author  : Scorpion

# -*- coding:utf-8 -*-

import xlwt
from db import QueryCount
# b = xlwt.Workbook(encoding='utf-8')
# e = b.add_sheet('测试')
# e.write(0, 0, 'k')
# b.save('kk.xls')

data = QueryCount().get_table()
columns = ['序列', '职位', '公司名称', '优势', '月薪', '工作城市', '工作经验', '学历', '详细地址', '职位要求', '相关链接']
work_book = xlwt.Workbook(encoding='utf-8')
sheet = work_book.add_sheet('区块链工程师')
for i, v in enumerate(columns):
    sheet.write(0, i, v)
for k, item in enumerate(data):
    for m, n in enumerate(item):
        sheet.write(k+1, m, n)

work_book.save('blockchain.xls')