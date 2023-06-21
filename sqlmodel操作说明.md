[读取连接的数据 - SQLModel (tiangolo.com)](https://sqlmodel.tiangolo.com/tutorial/connect/read-connected-data/) 

https://sqlmodel.tiangolo.com/

[Relationship back_populates - SQLModel (tiangolo.com)](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/)

[Many to Many - Intro - SQLModel (tiangolo.com)](https://sqlmodel.tiangolo.com/tutorial/many-to-many/)

# 创建模型

```python
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select, or_

# 创建表模型类
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None



# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")

# 创建表
SQLModel.metadata.create_all(engine)
```

# # 新增数据

```python
# 创建模型实例
def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)
        session.commit()
        session.close()
```

# # 查询数据

```python
def select_heros():
    with Session(engine) as session:
        # statement = select(Hero).offset(3).limit(3)
        # statement = select(Hero).where(Hero.name == "Deadpond").where(Hero.age == 30)
        # statement = select(Hero).where(Hero.age >= 35, Hero.age < 40)
        statement = select(Hero).where(or_(Hero.age <= 35, Hero.age > 90))
        # statement = select(Hero).where(Hero.name == "Deadpond")
        # statement = select(Hero).where(Hero.name != "Deadpond")
        # statement = select(Hero).where(Hero.age > 35)
        # statement = select(Hero).where(Hero.age >= 35)
        # statement = select(Hero).where(Hero.age < 35)
        # statement = select(Hero).where(Hero.age <= 35)
        results = session.exec(statement)
        # 链式调用
        # results = session.exec(statement).all()
        # heros = results.all()
        # print(heros)
        # 循环访问结果
        #for hero in results:
        #    print(hero)
        # 读取一行
        # hero1 = results.first()
        # 正好一个
        # hero2 = results.one()

# 通过主键的 Id 列选择单行
# def select_heros():
#     with Session(engine) as session:
#         hero = session.get(Hero1, 1) # 如果查询不到，则为None
#         print("Hero:", hero)
# 联表查询
def select1_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


# 左链接
def select2_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


def select3_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team).where(Team.name == "Preventers")
        results = session.exec(statement)
        for hero, team in results:
            print("Preventer Hero:", hero, "Team:", team)


# 连接
def select4_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)
```

# 更新数据

```python
# 更新
def update_hero():
    with Session(engine) as session:
        # 先查询出要更新的数据
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)
        # 更新数据
        hero.age = 16
        session.add(hero)
        session.commit()
        session.refresh(hero)
        print("Updated hero:", hero)
```

# 删除数据

```python
# 删除
def delete_heroes():
    with Session(engine) as session:
       # 先查询出要删除的数据
       statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.one()
        print("Hero: ", hero)
        # 删除
        session.delete(hero)
        session.commit()

        print("Deleted hero:", hero)

        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.first()

        if hero is None:
            print("There's no hero named Spider-Youngster")
```

# 关系

![](https://sqlmodel.tiangolo.com/img/tutorial/relationships/attributes/back-populates.svg)

代码实例

```python
from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")
```

# 多对多关系

代码实例

```python
from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    teams: List[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
```

创建多对对关系数据

```python
def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Deadpond:", hero_deadpond)
        print("Deadpond teams:", hero_deadpond.teams)
        print("Rusty-Man:", hero_rusty_man)
        print("Rusty-Man Teams:", hero_rusty_man.teams)
        print("Spider-Boy:", hero_spider_boy)
        print("Spider-Boy Teams:", hero_spider_boy.teams)
```

更新和删除多对多数据

```python
def update_heroes():
    with Session(engine) as session:
        hero_spider_boy = session.exec(
            select(Hero).where(Hero.name == "Spider-Boy")
        ).one()
        team_z_force = session.exec(select(Team).where(Team.name == "Z-Force")).one()

        team_z_force.heroes.append(hero_spider_boy)
        session.add(team_z_force)
        session.commit()

        print("Updated Spider-Boy's Teams:", hero_spider_boy.teams)
        print("Z-Force heroes:", team_z_force.heroes)

        hero_spider_boy.teams.remove(team_z_force)
        session.add(team_z_force)
        session.commit()

        print("Reverted Z-Force's heroes:", team_z_force.heroes)
        print("Reverted Spider-Boy's teams:", hero_spider_boy.teams)
```

# 代码结构

.
├── project
 ├── __init__.py
 ├── app.py
 ├── database.py
 └── models.py

# models.py

```python
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")
```

# database.py

```python
from sqlmodel import SQLModel, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
```

# app.py

```python
from sqlmodel import Session

from .database import create_db_and_tables, engine
from .models import Hero, Team


def create_heroes():
    with Session(engine) as session:
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")

        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team=team_z_force
        )
        session.add(hero_deadpond)
        session.commit()

        session.refresh(hero_deadpond)

        print("Created hero:", hero_deadpond)
        print("Hero's team:", hero_deadpond.team)


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()e
```

Fastapi项目结构

![](C:\Users\SL-COM-254\AppData\Roaming\marktext\images\2023-06-19-17-09-33-image.png)

# db.py

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

sqlite_file_name = "HeroInfo.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
```

# model.py

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

# crud.py

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

# main.py

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

如创建pymysql数据库报如下错：`sqlalchemy.exc.InvalidRequestError: Table 'heroinfo' is already defined for this MetaData instance.`

在模型中添加这一句`__table_args__ = {'extend_existing': True}`

查询

```python
  # 查询name为"Rusty-Man"的记录
  statement = select(Hero).where(Hero.name == "Rusty-Man")
  # 查询name为"Rusty-Man"且age为48的记录
  statement = select(Hero).where(Hero.name == "Rusty-Man").where(Hero.age == 48)
   # 查询name为"Rusty-Man"且age为48的记录
  statement = select(Hero).where(and_(Hero.name == "Rusty-Man", Hero.age == 48))
  # 查询age大于等于35，或者大于90的
  statement = select(Hero).where(or_(Hero.age <= 35, Hero.age > 90))
  # 查询age大于等35且小于40的记录
  statement = select(Hero).where(Hero.age >= 35, Hero.age < 40)
  # 查询name不等于Deadpond的记录
  statement = select(Hero).where(Hero.name != "Deadpond")
  # 查询age大于35的记录，小于同理
  statement = select(Hero).where(Hero.age > 35)
  # 查询age大于等于35的记录，小于等于同理
  statement = select(Hero).where(Hero.age >= 35)
  # 正好一行
  statement = session.exec(select(Hero).where(Hero.name == "Deadpond")).one()
  # 读取一行
  session.exec(select(Hero).where(Hero.name == "Deadpond")).first()
  # 查询ID为1的记录，如果没有,则返回None
  statement = session.get(Hero1, 1)
  # offset,limit
  statement = select(Hero).where(Hero.age >= 35, Hero.age < 40).offset(10).limit(100)
  # 两个表查询
  statement = select(Hero, Team).where(Hero.team_id == Team.id)
  # 连接
  statement = select(Hero, Team).join(Team)
  statement = select(Hero).join(Team).where(Team.name == "Preventers")
  # 左连接
  statement = select(Hero, Team).join(Team, isouter=True)
```
