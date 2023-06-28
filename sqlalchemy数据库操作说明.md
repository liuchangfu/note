# 1.更新数据，先查询出数据，再更新相关字段

```python
# 启用停用
def active(db: Session, id: int, state: int):
    user = db.query(User).filter(User.id == id).first()
    user.state = state
    db.commit()
    db.flush()
```

# 2.删除数据，先查询出数据，再删除

```python
# 根据用户id删除用户
def delete_user_by_id(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    db.flush()
```

# 3.添加数据，直接操作模型

```python
# 添加
def add_user(db: Session, username: str, pwd: str, avatar: str, department_name: str, addr: str, state: int):
    department = db.query(Department).filter(Department.name == department_name).first()
    user = User(username=username, pwd=pwd, avatar="/" + avatar, addr=addr, state=state, dep_id=department.id)
    db.add(user)
    db.commit()
    db.flush()
```

# 4.查询数据

```python
# 获取用户信息，获取用户id,用户头像等信息
def get_user_by_username_and_pwd(db: Session, username: str, md5_pwd: str) -> User:
    user = db.query(User.id, User.username, User.avatar, User.ip, User.last_login_date, User.state).filter(
        User.username == username, User.pwd == md5_pwd).first()
    return user
```

# 5.创建模型

```python
from sqlalchemy import Column, ForeignKey, Integer, String

from .db import Base

class User(Base):  # 必须继承declaraive_base得到的那个基类
     __tablename__ = "user"

     id = Column(Integer, primary_key=True, index=True)
```

# 6.说明

     # filter和filter_by
            filter中可以有多个条件，使用==
            filter_by中只有一个，使用=    注意：不能使用模型.字段名，直接使用字段名即可
        #first()   返回查询到的第一个
        # .all()     返回查询到的所有
        # .one()     有且只有一个元素时才正确返回
    
     # 排序：.order_by(Student.age.desc()) 
            # desc：降序
            # aes：升序
    
    
     # and：
            .filter(Student.age >= 10, Student.sex == 'female').all()
        # or：
            from sqlalchemy import or_
            .filter(or_(Student.age >= 20, Student.sex == 'female')).all()
    
        # eq：.filter(Student.age == 18).all()
        # ne：.filter(Student.age != 18).all()
        # like：.filter(Student.name.like('%To%')).all()
        # in： .filter(Student.age.in_([16, 20])).all()
        # count：db.query(Student).count()

# 7 字段说明

    Integer                         整型
    String(255)                     字符串，长度最大为255
    Text                            长文本
    DateTime                        时间
    Date                            日期
    primary_key=True                主键
    autoincrement=True              自增长
    nullable=False                  运行为空
    unique=True                     唯一
    index=True                      索引
    ForeignKey('users.id')          外键
    relationship('Article', backref='author')     关系，反向查询

# 8 一对一

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(20), nullable=False)
    
        addresses = relationship('Address', bac

kref='users', uselist=False)

    class Address(Base):
        __tablename__ = 'address'
        id = Column(Integer, primary_key=True)
        address = Column(String(20), nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))

# 9 一对多

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    addresses = relationship('Address', backref='users')

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

> 一对多和一对一的区别就是uselist，为false就是一对一

# 10 多对多

```python
class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    class_teacher = relationship('ClassTeacher', backref='class')


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    teacher_class = relationship('ClassTeacher', backref='teacher')


class ClassTeacher(Base):
    __tablename__ = 'class_teacher'  # 这就是所谓的一张视图表,没有实际存在数据，但是凭借关系型数据库的特点可以体现出一些数据关系
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.class_id'), primary_key=True)
    # 这张第三表中有两个主键，表示不能有class_id和teacher_id都相同的两项
```

判断记录是否存在，可以用count(),如果大于0则不插入，如果等于0，正常插入，程序调用时，如果没有记录存在，则会返None
https://blog.csdn.net/qq_27371025/article/details/127862190