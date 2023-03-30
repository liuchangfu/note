https://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart

https://www.cnblogs.com/zhumengke/articles/11390478.html

[数据迁移--https://developer.aliyun.com/article/973651](https://developer.aliyun.com/article/973651)

https://www.jb51.net/article/222794.html

https://www.yingsoo.com/news/devops/44523.html

# Peewee模型说明

## Meta 类属性

Meta 类属性详解如下：

| Option             | Meaning                      | 是否可继承? |
| ------------------ | ---------------------------- | ------ |
| database           | 指定表创建依附的数据库                  | yes    |
| table_name         | 表名                           | no     |
| table_function     | 生成表名的函数                      | yes    |
| indexes            | 多行索引                         | yes    |
| primary_key        | 主键                           | yes    |
| constraints        | 表约束的列表                       | yes    |
| schema             | 模型的数据库架构                     | yes    |
| only_save_dirty    | 调用model.save（）时，仅保存脏字段，指定字段？ | yes    |
| options            | 创建表扩展的选项字典                   | yes    |
| table_settings     | 在右括号后设置字符串的列表                | yes    |
| temporary          | 指示临时表                        | yes    |
| legacy_table_names | 使用旧表名生成（默认情况下启用）             | yes    |
| depends_on         | 指示此表依赖于另一个表进行创建              | no     |
| without_rowid      | 指示表不应具有rowid（仅限SQLite）       | no     |
| strict_tables      | 指示严格的数据类型（仅限SQLite，3.37+）    | yes    |

## ``peewee`中关于增删改查的基本操作方法如下：

![](https://www.yingsoo.com/static/upload/3392_0104072010_zd533wmi5d5.png)

### `增 ：`

- create()：最常用创建，返回创建实例
- save()：第一次执行的save是插入，第二次是修改
- insert: 插入数据，不创建数据库实例。返回id
- insert_many: 批量插入
- bulk_create：批量插入，类似于insert_many。可指定单次插入的数量
- batch_commit: 自动添加了一个事务，然后一条条的插入
- insert_from: 从另一个表中查询的数据作为插入的数据

`删除 ：`

- delete().where().execute()
- delete_instance() 直接执行删除了，不用调用execute() 方法

`修改 ：`

- save()： 第一次执行的save是插入，第二次是修改
- update() 用于多字段更新

`查询 ：`

- Model.get()： 检索与给定查询匹配的单个实例。报 Model.DoesNotExist 异常。如果有多条记录满足条件，则返回第一条
- get_or_none() :与get使用方法相同。区别是找不到结果时不会报错
- get_by_id() :通过主键查找，是一种快捷方式
- Model['id_num']: 和上面的get_by_id一样是通过主键查找。
- get_or_create(): 首先查询，如果查不到将创建一个新的记录
- select() 查询多条数据

### 字段类型表

| 字段类型              | Sqlite        | Postgresql       | MySQL            |
| ----------------- | ------------- | ---------------- | ---------------- |
| AutoField         | integer       | serial           | integer          |
| BigAutoField      | integer       | bigserial        | bigint           |
| IntegerField      | integer       | integer          | integer          |
| BigIntegerField   | integer       | bigint           | bigint           |
| SmallIntegerField | integer       | smallint         | smallint         |
| IdentityField     | not supported | int identity     | not supported    |
| FloatField        | real          | real             | real             |
| DoubleField       | real          | double precision | double precision |
| DecimalField      | decimal       | numeric          | numeric          |
| CharField         | varchar       | varchar          | varchar          |
| FixedCharField    | char          | char             | char             |
| TextField         | text          | text             | text             |
| BlobField         | blob          | bytea            | blob             |
| BitField          | integer       | bigint           | bigint           |
| BigBitField       | blob          | bytea            | blob             |
| UUIDField         | text          | uuid             | varchar(40)      |
| BinaryUUIDField   | blob          | bytea            | varbinary(16)    |
| DateTimeField     | datetime      | timestamp        | datetime         |
| DateField         | date          | date             | date             |
| TimeField         | time          | time             | time             |
| TimestampField    | integer       | integer          | integer          |
| IPField           | integer       | bigint           | bigint           |
| BooleanField      | integer       | boolean          | bool             |
| BareField         | untyped       | not supported    | not supported    |
| ForeignKeyField   | integer       | integer          | integer          |

### 字段初始化参数

所有字段类型接受的参数及其默认值

- `null = False` 允许空值
- `index = False` 创建索引
- `unique = False` 创建唯一索引
- `column_name = None` 显式指定数据库中的列名
- `default = None` 默认值，可以使任意值或可调用对象
- `primary_key = False` 指明主键
- `constraints = None` 约束条件
- `sequence = None` 序列名字（如果数据库支持）
- `collation = None` 排序字段
- `unindexed = False` 虚表上的字段不应该被索引
- `choices = None` 两种可选项`：value display`
- `help_text = None` 帮助说明字段。表示此字段的任何有用文本的字符串
- `verbose_name = None` 表示此字段的用户友好名称的字符串
- `index_type = None` 索引类型

### 字段特有参数

在一些字段中有些自己特有的参数，如下：

| 字段类型            | 特有参数                                                              |
| --------------- | ----------------------------------------------------------------- |
| CharField       | max_length                                                        |
| FixedCharField  | max_length                                                        |
| DateTimeField   | formats                                                           |
| DateField       | formats                                                           |
| TimeField       | formats                                                           |
| TimestampField  | resolution, utc                                                   |
| DecimalField    | max_digits, decimal_places, auto_round, rounding                  |
| ForeignKeyField | model, field, backref, on_delete, on_update, deferrable lazy_load |
| BareField       | adapt                                                             |

示例代码如下：

```python
# coding=utf-8
"""
    @project: fastApiProject
    @Author：Liuchangfu
    @file： test09.py
    @date：2023/2/10 14:13
 """
import peewee
from peewee import *
from peewee import Model
from pendulum import date

settings = {'host': 'localhost', 'password': 'lcfwku', 'port': 3306, 'user': 'root'}
db = peewee.MySQLDatabase("test", **settings)


class Person(Model):
    name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
    passwd = CharField(verbose_name='密码', max_length=20, null=False, default='123456')
    email = CharField(verbose_name='邮件', max_length=50, null=True, unique=True)
    gender = IntegerField(verbose_name='姓别', null=False, default=1)
    birthday = DateField(verbose_name='生日', null=True, default=None)
    is_admin = BooleanField(verbose_name='是否是管理员', default=True)

    class Meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类


# 创建表
# Person.create_table()

# 创建表也可以这样, 可以创建多个
# db.create_tables([Person])

# 添加一条数据
# p1 = Person(name='test01', passwd='123456', email='test01@admin.com', gender=1, birthday=date(1990, 12, 20),
#             is_admin=True)
# p1.save()

# p2 = Person(name='test02', passwd='123456', email='test02@admin.com', gender=2, birthday=date(1990, 12, 20),
#             is_admin=True)
#
# p2.save()

# 查询单条数据
# p1 = Person.get(Person.name == 'test01')
# print(p1.email, p1.is_admin)
#
# # 使用where().get()查询
# p2 = Person.select().where(Person.name == 'test02').get()
# print(p2.email, p2.is_admin)
#
# # 查询多条数据
# persons = Person.select().where(Person.is_admin == True)
# for p in persons:
#     print(p.name, p.email)

# # 删除姓名为perter的数据
# Person.delete().where(Person.name == 'test').execute()
# 删除
#   host = Host.get(Host.id == id)
#   host.delete_instance()
#
# # 已经实例化的数据, 使用delete_instance
# p = Person(name='test', birthday=date(1990, 12, 20), is_admin=False)
# p.id = 1
# p.save()
# p.delete_instance()

# 已经实例化的数据,指定了id这个primary key,则此时保存就是更新数据
# p = Person(name='admin', birthday=date(1990, 12, 20))
# p.id = 5
# p.save()

# # 更新birthday数据
# q = Person.update({Person.birthday: date(1983, 12, 21)}).where(Person.name == 'admin')
# q.execute()

# 批量插入数据
# data = [
#     {'name': 'user01', 'passwd': 123456, 'email': 'user01@admin.com', 'gender': 1},
#     {'name': 'user02', 'passwd': 123456, 'email': 'user02@admin.com', 'gender': 2},
#     {'name': 'user03', 'passwd': 123456, 'email': 'user03@admin.com', 'gender': 1},
# ]
# Person.insert_many(data).execute()


# # 查询整张表的数据条数
# total_num = Person.select().count()
# print(total_num)
#
# # 查询is_admin为1的Person数量, 返回数量为1
# num = Person.select().where(Person.is_admin == 1).count()
# print(num)

# # 按照创建时间降序排序
# persons = Person.select().order_by(Person.create_time.desc())
#
# # 按照创建时间升序排序
# persons = Person.select().order_by(Person.create_time.asc())

# # 查询湖南和湖北的, 注意需要用()将Person.province == '湖南'包一层
# persons = Person.select().where((Person.province == '湖南') | (Person.province == '湖北'))
#
# # 查询湖南和身高1.75
# persons = Person.select().where((Person.province == '湖南') & (Person.height == 1.75))

# # <<使用，查询省份属于湖北和湖南的，对应sql语句：select * from person where province in ('湖南', '湖北')
# persons = Person.select().where(Person.province << ['湖南', '湖北'])
#
# # >>使用，查询省份为空的，sql语句: select * from person where province is Null
# persons = Person.select().where(Person.province >> None)
#
# # %使用，查询省份中含有 湖 字，sql语句：select * from person where province like '%湖%'
# persons = Person.select().where(Person.province % '%湖%')

# 联表查询例子
# query = (Tweet.select(Tweet.content, Tweet.timestamp, User.username).join(User, on=(User.id == Tweet.user_id)).order_by(Tweet.timestamp.desc()))

# 事务
# from xModels import XUser, database
#
# with database.atomic() as transaction:
#     XUser.create(phone='184738373833', password='123456')
#     XUser.create(phone='184738373833332323232', password='123456')






# coding=utf-8
"""
@IDE：
@project: fastApiProject
@Author：Liuchangfu
@file： test10.py
@date：2023/2/10 15:28
 """
# 用于创建数据表模型

import peewee
from peewee import *
from peewee import Model
from datetime import datetime


# 创建基类：减少重复代码
class BaseModel(Model):
    create_time = DateTimeField(default=datetime.now)

    # 创建函数，用于返回用户的信息位字典形式
    def to_json(self) -> dict:
        r = {}
        for k in self.__data__.keys():
            # 判断数据是否是create_time(时间不是字符串)
            if k == 'create_time':
                r[k] = str(getattr(self, k))
            else:
                r[k] = getattr(self, k)
        return r

    class Meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类


# 创建用户表
class UserModel(BaseModel):
    id = CharField(primary_key=True)
    email = CharField(max_length=32, verbose_name='账号')
    nick_name = CharField(max_length=32, verbose_name='昵称', null=True)
    password = CharField(max_length=128, verbose_name='密码')
    gender = CharField(verbose_name='性别', null=True)
    signatrue = CharField(max_length=32, verbose_name='签名', null=True)
    pic = CharField(max_length=512, verbose_name='头像', null=True)
    status = CharField(verbose_name='账号状态', default=1)

    class Meta:
        table_name = 't_user'


# 创建帖子表
class TopicModel(BaseModel):
    id = CharField(primary_key=True)
    title = CharField(verbose_name='标题')
    imgs = CharField(verbose_name='图片', max_length=2000)
    content = CharField(verbose_name='内容', max_length=2000)
    chick_num = CharField(verbose_name='点击数')
    type_ = CharField(verbose_name='类型')
    # 关联主表
    user = ForeignKeyField(UserModel, backref='topics')

    class Meta:
        table_name = 't_topic'


# 创建收藏表——帖子表与用户表的关联表
class CollectionModel(BaseModel):
    topic = ForeignKeyField(TopicModel, backref='collections')
    user = ForeignKeyField(UserModel, backref='collections')

    class Meta:
        table_name = 't_collection'
        primary_key = CompositeKey('topic', 'user')  # 设置唯一主键
```

FastAPI

```python
from fastapi import FastAPI
from peewee import *

db = SqliteDatabase('my_app.db')
app = FastAPI()

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.on_event("startup")
def startup():
    db.connect()


# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()
```

官方示例

```python
import datetime
from peewee import *

db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
```

# 主键和约束

```python
class Person(Model):
    first = CharField()
    last = CharField()

    class Meta:
        primary_key = CompositeKey('first', 'last')

class Pet(Model):
    owner_first = CharField()
    owner_last = CharField()
    pet_name = CharField()

    class Meta:
        constraints = [SQL('FOREIGN KEY(owner_first, owner_last) REFERENCES person(first, last)')]


# 复合主键
class BlogToTag(Model):
    """A simple "through" table for many-to-many relationship."""
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')

# 关闭主键自增
User._meta.auto_increment = False # turn off auto incrementing IDs 
```

# 外键

### 一对多

```python
class Pet(peewee.Model):
    name = peewee.CharField()
    owner = peewee.ForeignKeyField(Person,related_name="pets",backref="petties")   
　　# backref是反查的字段，如果有related_name用related_name反查，如果没有直接用petties反查 e.g. [i.name for i in Person.get(name="aaa").petties] 

    class Meta: 
        database = db

class Category(Model):
    name = CharField()
    parent = ForeignKeyField('self', null=True, backref='children')
   # 注意自关联永远是null = True
```

### 多对多

```python
from peewee import *
from playhouse.fields import ManyToManyField

db = SqliteDatabase('school.db')

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    name = CharField()

class Course(BaseModel):
    name = CharField()
    students = ManyToManyField(Student, related_name='courses')

StudentCourse = Course.students.get_through_model()

db.create_tables([
    Student,
    Course,
    StudentCourse])
```