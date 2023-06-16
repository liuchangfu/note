[Intro, Installation, and First Steps - SQLModel](https://sqlmodel.tiangolo.com/tutorial/)

代码结构如下

![](C:\Users\SL-COM-254\AppData\Roaming\marktext\images\2023-06-16-16-42-04-image.png)

crud.py

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: sqlmodel_project
@Author：Liuchangfu
@file： crud.py
@date：2023/6/16 15:47
 """
from typing import Optional

from sqlmodel import Session, select
from Api_Pro.model import Hero, HeroCreate, HeroUpdate


# 新增
def create_hero_db(session: Session, hero: HeroCreate):
    db_hero = Hero.from_orm(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


def get_all_heroes(session: Session, offset: int, limit: int):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


def get_one_hero(session: Session, hero_id: int):
    hero = session.get(Hero, hero_id)
    return hero


def update_hero(session: Session, hero_id: int, hero: HeroUpdate):
    db_hero = session.get(Hero, hero_id)
    if db_hero:
        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


def delete_hero(session: Session, hero_id: int):
    hero = session.get(Hero, hero_id)
    if hero:
        session.delete(hero)
        session.commit()
```

db.py

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: sqlmodel_project
@Author：Liuchangfu
@file： db.py
@date：2023/6/16 15:47
 """
from sqlmodel import create_engine, SQLModel, Session
# sqlite_db
sqlite_file_name = "HeroInfo.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

# mysql
username = "root"
pwd = "lcfwku"
host = "localhost"
port = "3306"
db_name = "share_system"

url = f"mysql+pymysql://{username}:{pwd}@{host}:{port}/{db_name}?charset=utf8"

Engin = create_engine(url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
```

main.py

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: sqlmodel_project
@Author：Liuchangfu
@file： main.py
@date：2023/6/16 15:51
 """
from typing import List
from fastapi import FastAPI, Depends, Query, HTTPException
import uvicorn
from sqlmodel import Session
from Api_Pro.db import create_db_and_tables, get_session
from Api_Pro.model import Hero, HeroCreate, HeroRead, HeroUpdate
from Api_Pro.crud import create_hero_db, get_all_heroes, get_one_hero, update_hero, delete_hero
from main03 import HeroReadWithTeam

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/", response_model=HeroRead)
def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = create_hero_db(session, hero)
    return db_hero


@app.get("/heroes/", response_model=List[HeroRead])
def read_heroes(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    heroes = get_all_heroes(session, offset, limit)
    return heroes


@app.get("/heroes/{hero_id}", response_model=HeroReadWithTeam)
def read_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = get_one_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.patch("/heroes/{hero_id}", response_model=HeroRead)
def update_hero(
        *, session: Session = Depends(get_session), hero_id: int, hero: HeroUpdate
):
    db_hero = update_hero(session, hero_id, hero)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero


@app.delete("/heroes/{hero_id}")
def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = delete_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"ok": True}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
```

model.py

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: sqlmodel_project
@Author：Liuchangfu
@file： model.py
@date：2023/6/16 15:47
 """

from typing import Optional, List
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
```

如创建数据库报如下错：`sqlalchemy.exc.InvalidRequestError: Table 'heroinfo' is already defined for this MetaData instance.`

在模型中添加这一句`__table_args__ = {'extend_existing': True}`


