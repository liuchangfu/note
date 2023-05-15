# peewee与Fastapi代码示例

## 数据库配置

```python
from contextvars import ContextVar

import peewee

# Mysql数据库名称
MYSQL_DATABASE_NAME = 'test_peewee'
# Mysql数据库配置
settings = {'host': 'localhost', 'password': 'lcfwku', 'port': 3306, 'user': 'root'}
# SQLite数据库名称
# DATABASE_NAME = "test_peewee.db"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


# Sqlite
# db = peewee.SqliteDatabase(DATABASE_NAME, check_same_thread=False)
# Mssql
db = peewee.MySQLDatabase(MYSQL_DATABASE_NAME, **settings)

db._state = PeeweeConnectionState()
```

# 数据库模型

```python
import peewee
from .database import db


class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    email = peewee.CharField(unique=True, index=True)
    hashed_password = peewee.CharField()
    is_active = peewee.BooleanField(default=True)



class Item(BaseModel):
    title = peewee.CharField(index=True)
    description = peewee.CharField(index=True)
    owner = peewee.ForeignKeyField(User, backref="items")
```

## 数据库操作代码

```python
from . import model, schemas


def get_user(user_id: int):
    return model.User.filter(model.User.id == user_id).first()


def get_user_by_email(email: str):
    return model.User.filter(model.User.email == email).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(model.User.select().offset(skip).limit(limit))


def create_user(user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.User(email=user.email, hashed_password=fake_hashed_password)
    db_user.save()
    return db_user


def get_items(skip: int = 0, limit: int = 100):
    return list(model.Item.select().offset(skip).limit(limit))


def create_user_item(item: schemas.ItemCreate, user_id: int):
    db_item = model.Item(**item.dict(), owner_id=user_id)
    db_item.save()
    return db_item

# 获取学生信息
def get_students(skip: int = 0, limit: int = 100):
    return list(model.Student.select().offset(skip).limit(limit))


# 添加学生信息
def create_student(name: str):
    student = model.Student(name=name)
    student.save()
    return student


# 修改学生信息
def edit_student(id: int, name: str):
    student = model.Student.filter(id=id).first()
    if student:
        student.name = name
        student.save()
    return student


# 删除学生信息
def delete_student(id: int):
    student = model.Student.filter(id=id).first()
    if student:
        student.delete()
```

## main.py代码

```python
import time
from typing import List
from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from sql_app import crud, database, model, schemas

from sql_app.database import db_state_default

# 数据表初始化
database.db.connect()
database.db.create_tables([model.User, model.Item])
database.db.close()

app = FastAPI()

sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()

# 接口导入依赖
@app.post("/users/", response_model=schemas.User, dependencies=[Depends(get_db)], description='创建用户',
          summary='创建用户', tags=['用户模块'])
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
```
