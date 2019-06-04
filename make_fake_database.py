import pyodbc
import faker
from faker.providers import BaseProvider
import random
import os
import re




# 准备模拟数据
fake = faker.Faker('zh_CN')


db_file_location = r"C:\Users\Administrator\Documents\Database4.accdb"

connection = pyodbc.connect(
    rf'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_file_location};')

connection.autocommit = True






def make_fake_commoditiersProvider():
    lines = open(rf'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\商品名.txt','r',encoding='gbk').read().splitlines()

    class CommoditiesProvider(BaseProvider):
        def ordered_commodities(self):
            return lines.pop()
        def random_commodities(self):
            return random.choice(lines)


    fake.add_provider(CommoditiesProvider)




def make_fake_suppiersProvider():
    lines = open(rf'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\供应商乱序版.txt','r',encoding='gbk').read().splitlines()


    class SuppiersProvider(BaseProvider):
        def ordered_suppiers(self):
            return lines.pop()

        def rendom_suppiers(self):
            return random.choice(lines)


    fake.add_provider(SuppiersProvider)

def make_fake_clint_Provider():
    lines = open(rf'C:\Users\Administrator\PycharmProjects\Weiye commerce company software\客户姓名.txt','r',encoding='gbk').read().splitlines()


    class ClintProvider(BaseProvider):
        def ordered_clints(self):
            return lines.pop()

        def rendom_clints(self):
            return random.choice(lines)


    fake.add_provider(ClintProvider)


def make_myprovider():
    make_fake_suppiersProvider()
    make_fake_commoditiersProvider()
    make_fake_clint_Provider()
    # for _ in range(6000):
    #
    #     print(fake.random_commodities())
    #     print(fake.ordered_suppiers())



def make_suppliers():
    create_table_sql = '''
    create table suppliers
    (
     id  autoincrement primary key,
     name  varchar(255) unique ,
     address   varchar(255)  ,
     phone varchar(14)

    )
    '''


    insert_table_sql = '''\
    insert into suppliers(name,  address, phone)
    values (?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from suppliers
     '''

    table_exists = False
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(200):
            cursor.execute(insert_table_sql, (
                                              fake.ordered_suppiers(),
                                              fake.address(),
                                              fake.phone_number()))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], sep='\t')


def make_commodities():
    create_table_sql = '''
    create table commodities
    (
     id  autoincrement primary key,
     commodities_name  varchar(255),
     Purchase_price  varchar(30),
     sellinga_price  varchar(30),
     suppiers_id   varchar(255)

    )
    '''


    insert_table_sql = '''\
    insert into commodities(     commodities_name
    ,Purchase_price,sellinga_price,suppiers_id)
    values (?,?,?,?)
    '''

    select_table_sql = '''\
    select *
    from commodities
     '''
    table_exists = False
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)


    with connection.cursor() as cursor:
        for _ in range(400):
            cursor.execute(insert_table_sql, (
                                              fake.ordered_commodities(),
                                              float(fake.random_int(min=1, max=500)),
                                              float(fake.random_int(min=500, max=2000)),
                                              float(fake.random_int(min=1, max=200))))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], row[4], sep='\t')

def make_clients():
    create_table_sql = '''
    create table clients
    (
     id  autoincrement primary key,
     name  varchar(255) unique ,
     conpany   varchar(255)  ,
     address varchar(255),
     phone varchar(14)

    )
    '''


    insert_table_sql = '''\
    insert into clients(name, conpany, address, phone)
    values (?, ?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from clients
     '''

    table_exists = False
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(50):
            cursor.execute(insert_table_sql, (
                                              fake.ordered_clints(),
                                              fake.company(),
                                              fake.address(),
                                              fake.phone_number()))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3],row[4], sep='\t')


def make_Staffs():
    create_table_sql = '''
    create table Staffs
    (
     id  autoincrement primary key,
     name  varchar(255) unique ,
     email   varchar(255)  ,
     address varchar(255),
     phone varchar(14),
     entrytime datetime
    )
    '''


    insert_table_sql = '''\
    insert into Staffs(name, email, address, phone, entrytime)
     values ( ?, ?, ?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from Staffs
     '''

    table_exists = False
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(20):
            cursor.execute(insert_table_sql, (
                                              fake.name(),
                                              fake.email(),
                                              fake.address(),
                                              fake.phone_number(),
                                              fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3],row[4],row[5] ,sep='\t')

def make_purchaseorders():
    create_table_sql = '''
    create table purchaseorders
    (
     id  autoincrement primary key,
     commodity_id  varchar(255)  ,
     suppier_id   varchar(255)  ,
     purchase_number varchar(255),
     purchase_order_time datetime
    )
    '''


    insert_table_sql = '''\
    insert into purchaseorders(commodity_id, cient_id, purchase_number, purchase_order_time)
     values ( ?, ?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from purchaseorders
     '''

    table_exists = False
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(2000):
            cursor.execute(insert_table_sql, (
                                              float(fake.random_int(min=1, max=400)),
                                              float(fake.random_int(min=1, max=50)),
                                              float(fake.random_int(min=1000, max=2000)),
                                              fake.date_time_between(start_date="-2y", end_date="-1y", tzinfo=None)))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3],row[4], sep='\t')


def make_Sales_order():
    create_table_sql = '''
    create table Sales_order
    (
     id  autoincrement primary key,
     commodity_id  varchar(255)  ,
     cient_id   varchar(255)  ,
     sales_number varchar(255),
     sale_order_time datetime,
     salesman integer
    )
    '''


    insert_table_sql = '''\
    insert into Sales_order(commodity_id, cient_id, sales_number, sale_order_time, salesman)
     values ( ?, ?, ?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from Sales_order
     '''

    table_exists = True
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(2000):
            cursor.execute(insert_table_sql, (
                                              float(fake.random_int(min=1, max=400)),
                                              float(fake.random_int(min=1, max=50)),
                                              float(fake.random_int(min=1000, max=2000)),
                                              fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                                              float(fake.random_int(min=1000, max=2000))))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3],row[4], row[5] ,sep='\t')





def make_fake_database():

    make_fake_suppiersProvider()
    make_fake_commoditiersProvider()
    make_fake_clint_Provider()



    make_Sales_order()
    make_Staffs()
    make_suppliers()
    make_commodities()
    make_cients()
    make_purchaseorders()




if __name__ == '__main__':
    make_fake_database()