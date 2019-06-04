import faker
from faker.providers import BaseProvider
import random
import re
from fuzzywuzzy import fuzz


fake = faker.Faker('zh_CN')












def remove_repeat():


    lines = open(rf'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\供应商.txt',encoding='utf-8').read().splitlines()

    b = sorted(set(lines))

    with open(r'供应商去重版.txt','w+',encoding='utf8') as f:
        for i in b:
            f.write(i+"\n")


print(type(fake.name()))

def break_rank():
    lines = open(rf'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\供应商去重版.txt', 'r',
                 encoding='gbk').read().splitlines()

    a = list(set(lines))

    with open(r'供应商乱序版.txt','w+',encoding='gbk') as f:
        for i in a:
            f.write(i+"\n")

    print(a)

def make_client_name_norepeat():
    l = []
    for _ in range(50):
        a = fake.name()
        l.append(a)


    b = list(set(l))

    with open(r'客户姓名.txt','w+',encoding='gbk') as f:
        for i in b:
            f.write(i+"\n")



make_client_name_norepeat()


def checkout_similarity():

    lines = open(r'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\供应商去重版.txt',encoding='gbk').read().splitlines()

    for a in lines:
        for b in lines:
            print(fuzz.ratio(a,b))




print(fake.random_int(min=10, max=100))


def table_exists(cursor, table_name):


    sql = 'select name from MSysObjects where type=1 and flags=0'
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    print(tables)
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return 1
    else:
        return 0



    if (table_exists(con, table_name) != 1):
        print("表不存在，可以添加一张")

print(                                       fake.date_time_between(start_date="-2y", end_date="-1y", tzinfo=None))