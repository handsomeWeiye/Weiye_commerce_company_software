import pyodbc
import faker

# create_table_sql = '''\
# create table user
# (
#   id        autoincrement primary key,
#   username  varchar(255) unique,
#   nickname  varchar(255) not null,
#   password  varchar(20)  not null,
#   address   varchar(255),
#   birthday  date,
#   company   varchar(30),
#   job       varchar(20),
#   telephone varchar(14)
# )
# '''
#
# insert_table_sql = '''\
# insert into user(username, nickname, password, address, birthday, company, job, telephone)
# values (?, ?, ?, ?, ?, ?, ?, ?)
# '''
#
# select_public_servant_sql = '''\
# select *
# from user
# where job = '公务员'
#  '''

# 准备模拟数据
fake = faker.Faker('zh_CN')
# 设置种子值，不设的话每次随机的都不一样

db_file_location = r"C:\Users\Administrator\Documents\Database4.accdb"
# 这里用的是Python3.5的语法，如果是低版本Python的话需要改成普通方式
connection = pyodbc.connect(
    rf'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_file_location};')

connection.autocommit = True

# 第一次创建表，将其设置为False
# table_exists = True
# if not table_exists:
#     with connection.cursor() as cursor:
#         cursor.execute(create_table_sql)
#
# # 添加数据
# with connection.cursor() as cursor:
#     for _ in range(3000):
#         cursor.execute(insert_table_sql, (fake.pystr(min_chars=6, max_chars=10),
#                                           fake.name(),
#                                           fake.password(length=10),
#                                           fake.address(),
#                                           fake.date_of_birth(minimum_age=0, maximum_age=120),
#                                           fake.company(),
#                                           fake.job(),
#                                           fake.phone_number()))
#
#     # 查询一下所有公务员
#     cursor.execute(select_public_servant_sql)
#     results = cursor.fetchall()
#     for row in results:
#         print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], sep='\t')


#
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

    table_exists = True
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(200):
            cursor.execute(insert_table_sql, (
                                              fake.company(unique=True),
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
     name  varchar(255) unique ,
     address   varchar(255)  ,
     phone varchar(14)

    )
    '''


    insert_table_sql = '''\
    insert into commodities(name,  address, phone)
    values (?, ?, ?)
    '''

    select_table_sql = '''\
    select *
    from commodities
     '''

    table_exists = True
    if not table_exists:
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)

    with connection.cursor() as cursor:
        for _ in range(200):
            cursor.execute(insert_table_sql, (
                                              fake.company(unique=True),
                                              fake.address(),
                                              fake.phone_number()))

    cursor.execute(select_table_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], sep='\t')
