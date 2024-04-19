官方文档----[Tortoise ORM - Tortoise ORM v0.20.0 Documentation](https://tortoise.github.io/index.html)

数据迁移---- [GitHub - tortoise/aerich: A database migrations tool for TortoiseORM, ready to production.](https://github.com/tortoise/aerich)

示例说明-----[Examples - Tortoise ORM v0.20.0 Documentation](https://tortoise.github.io/examples.html)

[fastapi配合tortoise-orm实现jwt以及rbac的教程_fastapi rbac-CSDN博客](https://blog.csdn.net/2201_75632987/article/details/136105946)



一、ForeignKeyField：外键关系字段，此字段表示与另一个模型的外键关系

1、model_name: str 已定义的模型的名称，必传  
2、related_name: 外键关系名称  
3、on_delete: str 默认"CASCADE"  
　　field.CASCADE：表示如果相关模型被删除，模型应该被级联删除。  
　　field.RESTRICT：表示只要有外键指向，就会限制相关模型的删除。  
　　field.SET_NULL：将字段重置为 NULL，以防相关模型被删除。仅当字段已null=True设置时才能设置。  
　　field.SET_DEFAULT：将字段重置为default值，以防相关模型被删除。只能设置是字段有default设置。

4、to_field：相关模型上的属性名称，用于建立外键关系。如果未设置，则使用 pk  
5、db_constraint: bool 控制是否应在数据库中为此外键创建约束。默认值为 True，将此设置为 False 可能对数据完整性非常不利。



二、ManyToManyField：多对多关系字段，此字段表示此模型与另一个模型之间的多对多

1、through: 表示直通表的DB表。默认值通常是安全的  
2、forward_key: 直通表上的正向查找键。默认值通常是安全的。  
3、backward_key: 直通表上的向后查找键。默认值通常是安全的  
4、related_name:用于反向解析多对多的相关模型上的属性名称。  
5、db_constraint: 控制是否应在数据库中为此外键创建约束，默认值为True，将此设置为False可能对数据完整性非常不利。  
6、on_delete: str 默认"CASCADE"  
　　field.CASCADE：表示如果相关模型被删除，模型应该被级联删除。  
　　field.RESTRICT：表示只要有外键指向，就会限制相关模型的删除。  
　　field.SET_NULL：将字段重置为 NULL，以防相关模型被删除。仅当字段已null=True设置时才能设置。  
　　field.SET_DEFAULT：将字段重置为default值，以防相关模型被删除。只能设置是字段有default设置。



三、OneToOneField：一对一

1、model_name: str 已定义的模型的名称，必传  
2、related_name: 外键关系名称  
3、on_delete: str 默认"CASCADE"  
　　field.CASCADE：表示如果相关模型被删除，模型应该被级联删除。  
　　field.RESTRICT：表示只要有外键指向，就会限制相关模型的删除。  
　　field.SET_NULL：将字段重置为 NULL，以防相关模型被删除。仅当字段已null=True设置时才能设置。  
　　field.SET_DEFAULT：将字段重置为default值，以防相关模型被删除。只能设置是字段有default设置。  
4、to_field：相关模型上的属性名称，用于建立外键关系。如果未设置，则使用 pk  
5、db_constraint: bool 控制是否应在数据库中为此外键创建约束。默认值为 True，将此设置为 False 可能对数据完整性非常不利。



### Relations

```python
"""
This example shows how relations between models work.

Key points in this example are use of ForeignKeyField and ManyToManyField
to declare relations and use of .prefetch_related() and .fetch_related()
to get this related objects
"""
from tortoise import Tortoise, fields, run_async
from tortoise.exceptions import NoValuesFetched
from tortoise.models import Model


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )

    def __str__(self):
        return self.name


class Address(Model):
    city = fields.CharField(max_length=64)
    street = fields.CharField(max_length=128)

    event: fields.OneToOneRelation[Event] = fields.OneToOneField(
        "models.Event", on_delete=fields.OnDelete.CASCADE, related_name="address", pk=True
    )

    def __str__(self):
        return f"Address({self.city}, {self.street})"


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return self.name


async def run():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    tournament = Tournament(name="New Tournament")
    await tournament.save()
    await Event(name="Without participants", tournament_id=tournament.id).save()
    event = Event(name="Test", tournament_id=tournament.id)
    await event.save()

    await Address.create(city="Santa Monica", street="Ocean", event=event)

    participants = []
    for i in range(2):
        team = Team(name=f"Team {(i + 1)}")
        await team.save()
        participants.append(team)
    await event.participants.add(participants[0], participants[1])
    await event.participants.add(participants[0], participants[1])

    try:
        for team in event.participants:
            print(team.id)
    except NoValuesFetched:
        pass

    async for team in event.participants:
        print(team.id)

    for team in event.participants:
        print(team.id)

    print(
        await Event.filter(participants=participants[0].id).prefetch_related(
            "participants", "tournament"
        )
    )
    print(await participants[0].fetch_related("events"))

    print(await Team.fetch_for_list(participants, "events"))

    print(await Team.filter(events__tournament__id=tournament.id))

    print(await Event.filter(tournament=tournament))

    print(
        await Tournament.filter(events__name__in=["Test", "Prod"])
        .order_by("-events__participants__name")
        .distinct()
    )

    print(await Event.filter(id=event.id).values("id", "name", tournament="tournament__name"))

    print(await Event.filter(id=event.id).values_list("id", "participants__name"))

    print(await Address.filter(event=event).first())

    event_reload1 = await Event.filter(id=event.id).first()
    print(await event_reload1.address)

    event_reload2 = await Event.filter(id=event.id).prefetch_related("address").first()
    print(event_reload2.address)


if __name__ == "__main__":
    run_async(run())
```

## Relations with Unique field

```python
"""
This example shows how relations between models especially unique field work.

Key points in this example are use of ForeignKeyField and OneToOneField has to_field.
For other basic parts, it is the same as relation example.
"""
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model
from tortoise.query_utils import Prefetch


class School(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    id = fields.IntField(unique=True)

    students: fields.ReverseRelation["Student"]
    principal: fields.ReverseRelation["Principal"]


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    school: fields.ForeignKeyRelation[School] = fields.ForeignKeyField(
        "models.School", related_name="students", to_field="id"
    )


class Principal(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    school: fields.OneToOneRelation[School] = fields.OneToOneField(
        "models.School", on_delete=fields.OnDelete.CASCADE, related_name="principal", to_field="id"
    )


async def run():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    school1 = await School.create(id=1024, name="School1")
    student1 = await Student.create(name="Sang-Heon Jeon1", school_id=school1.id)

    student_schools = await Student.filter(name="Sang-Heon Jeon1").values("name", "school__name")
    print(student_schools[0])

    await Student.create(name="Sang-Heon Jeon2", school=school1)
    school_with_filtered = (
        await School.all()
        .prefetch_related(Prefetch("students", queryset=Student.filter(name="Sang-Heon Jeon1")))
        .first()
    )
    school_without_filtered = await School.first().prefetch_related("students")
    print(len(school_with_filtered.students))
    print(len(school_without_filtered.students))

    school2 = await School.create(id=2048, name="School2")
    await Student.all().update(school=school2)
    student = await Student.first()
    print(student.school_id)

    await Student.filter(id=student1.id).update(school=school1)
    schools = await School.all().order_by("students__name")
    print([school.name for school in schools])

    fetched_principal = await Principal.create(name="Sang-Heon Jeon3", school=school1)
    print(fetched_principal.name)
    fetched_school = await School.filter(name="School1").prefetch_related("principal").first()
    print(fetched_school.name)


if __name__ == "__main__":
    run_async(run())
```

 [Pydantic Examples - Tortoise ORM v0.20.0 Documentation](https://tortoise.github.io/examples/pydantic.html)

# FastAPI Examples

### models.py

```python
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default="misc")
    password_hash = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["password_hash"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
```

### main.py

```python
# pylint: disable=E0611,E0401
from typing import List

from fastapi import FastAPI
from models import User_Pydantic, UserIn_Pydantic, Users
from pydantic import BaseModel
from starlette.exceptions import HTTPException

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")


class Status(BaseModel):
    message: str


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())


@app.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.get("/user/{user_id}", response_model=User_Pydantic)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@app.put("/user/{user_id}", response_model=User_Pydantic)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@app.delete("/user/{user_id}", response_model=Status)
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")


register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
```

数据模型例子

```python
class Post(models.Model):
    """岗位表"""
    id = fields.CharField(max_length=50, pk=True)
    name = fields.CharField(max_length=32, null=False, default="")

class Department(AbstractDefaultColumn):
    """部门表"""
    id = fields.CharField(max_length=50, pk=True)
    name = fields.CharField(max_length=64, help_text='部门名')

class User(models.Model):
    """用户表"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, index=True)
    phone_no = fields.CharField(max_length=32, unique=True)
    email = fields.CharField(max_length=32, null=True)
    department = fields.ForeignKeyField("cp_model.Department", on_delete=fields.SET_NULL, null=True,
                                        related_name="depart_users", help_text='所属部门')
    post = fields.ForeignKeyField("cp_model.Post", on_delete=fields.SET_NULL, null=True, related_name="post_users",
                                  help_text='岗位')

class ForumArticle(AbstractDefaultColumn):
    """文章"""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("cp_model.User", on_delete=fields.CASCADE)
    title = fields.CharField(max_length=32, default='', null=True)  # 文章标题
    content = fields.TextField(default='', null=True, blank=True)  # 文章正文
    tags = fields.ManyToManyField('cp_model.ArticleTag', related_name='tags_article',
                                  through="cp_forum_article_tags",
                                  forward_key="cp_tag_id",
                                  backward_key="cp_forum_article_id"
                                  )  # 标签

    posters = fields.ManyToManyField("cp_model.CPImage", related_name="posters_article",
                                     through="cp_forum_article_posters",
                                     forward_key="cp_image_id",
                                     backward_key="cp_forum_article_id"
                                     )

class ArticleComment(AbstractDefaultColumn):
    """评论"""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("cp_model.User", related_name="user_comments", on_delete=fields.CASCADE)
    to_user_id = fields.IntField(default=0)  # 回复用户的id
    to_user_name = fields.CharField(max_length=32, default="", null=True, blank=True)  # 回复用户的name
    article = fields.ForeignKeyField("cp_model.ForumArticle", on_delete=fields.SET_NULL, null=True,
                                     related_name="article_comments")

class ArticleUpvoteRecord(AbstractDefaultColumn):
    """用户论坛文章的点赞记录"""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("cp_model.User", related_name="user_article_upvotes", on_delete=fields.CASCADE)
    article = fields.ForeignKeyField("cp_model.ForumArticle", related_name="article_upvotes", on_delete=fields.CASCADE)
```

```python
# 角色表
class Role(TimestampMixin):
    role_name = fields.CharField(max_length=15, description="角色名称")
    user: fields.ManyToManyRelation["User"] = fields.ManyToManyField("base.User", related_name="role",
                                                                     on_delete=fields.CASCADE)
    access: fields.ManyToManyRelation["Access"] = fields.ManyToManyField("base.Access", related_name="role",
                                                                         on_delete=fields.CASCADE)
    role_status = fields.BooleanField(default=False, description="True:启用 False:禁用")
    role_desc = fields.CharField(null=True, max_length=255, description='角色描述')

    class Meta:
        table_description = "角色表"
        table = "role"
# 用户表
class User(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    username = fields.CharField(unique=True, null=False, min_length=5, max_length=32, description="用户名")
    password = fields.CharField(null=False,min_length=8,max_length=255)
    mobile_phone = fields.CharField(unique=True, null=False, description="手机号", max_length=11)
    email = fields.CharField(unique=True, null=False, description='邮箱', max_length=32)
    full_name = fields.CharField(null=True, description='姓名', max_length=15)
    is_activate = fields.BooleanField(default=0, description='0未激活 1正常 2禁用')
    is_staff = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
    header_img = fields.CharField(null=True, max_length=255, description='用户头像')
    sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
    login_host = fields.CharField(null=True, max_length=15, description="访问IP")

    # 返回用户名默认
    def __str__(self):
        return self.username

    class Meta:
        table_description = "用户表"
        table = "user"

# 权限表
class Access(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    access_name = fields.CharField(max_length=15, description="权限名称")
    parent_id = fields.IntField(default=0, description='父id')
    scopes = fields.CharField(unique=True, max_length=255, description='权限范围标识')
    access_desc = fields.CharField(null=True, max_length=255, description='权限描述')
    menu_icon = fields.CharField(null=True, max_length=255, description='菜单图标')
    is_check = fields.BooleanField(default=False, description='是否验证权限 True为验证 False不验证')
    is_menu = fields.BooleanField(default=False, description='是否为菜单 True菜单 False不是菜单')

    def __str__(self):
        return self

    class Meta:
        table_description = "权限表"
        table = "access"
```

例子2--多对多关系

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Article_Api
@Author：Sam Lau
@file： models3.py
@date：2023/8/4 11:28
 """
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class User(Model):
    """用户表"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, index=True)
    phone_no = fields.CharField(max_length=32, unique=True)
    email = fields.CharField(max_length=32, null=True)


class Tags(Model):
    """标签表"""
    article: fields.ManyToManyRelation["Article"]
    id = fields.CharField(max_length=50, pk=True)
    tag = fields.CharField(max_length=32, null=False, default="")


class Category(Model):
    """分类表"""
    article: fields.ManyToManyRelation["Article"]
    id = fields.CharField(max_length=50, pk=True)
    category = fields.CharField(max_length=32, null=False, default="")


class Article(Model):
    """文章表"""
    id = fields.CharField(max_length=50, pk=True)
    user = fields.ForeignKeyField("models5.User", on_delete=fields.CASCADE, null=True,
                                  help_text='所属用户')
    title = fields.CharField(max_length=64, null=False, default="", help_text='文章标题')
    # 多对多关系定义在多的一方，通过 related_name="article"关联到Category表中的article字段
    category: fields.ManyToManyRelation["Category"] = fields.ManyToManyField("models5.Category",
                                                                             related_name="article",
                                                                             help_text='所属分类')
    # 多对多关系定义在多的一方，通过 related_name="article"关联到Tags表中的article字段
    tags: fields.ManyToManyRelation["Tags"] = fields.ManyToManyField("models5.Tags",
                                                                     related_name="article",
                                                                     help_text='所属标签')
    content = fields.TextField(null=False, default="")


async def run():
    await Tortoise.init(db_url="sqlite://models5.db", modules={"models5": ["__main__"]})
    await Tortoise.generate_schemas()
    user1 = User(name="Sam", phone_no="13551111111", email="Sam@qq.com")
    await user1.save()
    user2 = User(name="Alex", phone_no="1352144123333", email="Alex@qq.com")
    await user2.save()


if __name__ == '__main__':
    run_async(run())
```

<<<<<<< HEAD

# # 例子3-参照Django写法

## 一对一

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: tortoise_orm_ex
@Author：Sam Lau
@file： one_to_one.py
@date：2023/8/24 17:46
 """
from tortoise import fields, run_async, Tortoise
from tortoise.models import Model


class Place(Model):
    name = fields.CharField(max_length=50)
    address = fields.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(Model):
    place = fields.OneToOneField(
        'models.Place',
        on_delete=fields.CASCADE,
    )
    serves_hot_dogs = fields.BooleanField(default=False)
    serves_pizza = fields.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(Model):
    restaurant = fields.ForeignKeyField('models.Restaurant', on_delete=fields.CASCADE)
    name = fields.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


async def run():
    await Tortoise.init(db_url="sqlite://one_to_one.db", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    p1 = await Place.create(name="Demon Dogs", address="944 W. Fullerton")
    p2 = await Place.create(name="Ace Hardware", address="1013 N. Ashland")

    r1 = await Restaurant.create(place=p1, serves_hot_dogs=True, serves_pizza=False)
    r2 = await Restaurant.create(place=p2, serves_hot_dogs=True, serves_pizza=False)

    w1 = await Waiter.create(restaurant=r1, name="Bob")
    w2 = await Waiter.create(restaurant=r2, name="Alice")


if __name__ == '__main__':
    run_async(run())
```

=======

# # 例子3-参照Django写法

## 一对多

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: tortoise_orm_ex
@Author：Sam Lau
@file： test02.py
@date：2023/8/22 11:53
 """
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class Reporter(Model):
    first_name = fields.CharFieldmax_length=30)
    last_name = fields.CharField(max_length=30)
    email = fields.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(Model):
    headline = fields.CharField(max_length=100)
    pub_date = fields.DateField()
    reporter = fields.ForeignKeyField('models.Reporter', on_delete=fields.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]


async def run():
    await Tortoise.init(db_url="sqlite://test002.db", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    r1 = await Reporter.create(first_name="John", last_name="Smith", email="john@example.com")

    r2 = await Reporter.create(first_name="Paul", last_name="Jones", email="paul@example.com")

    a1 = await Article.create(headline="Article 1", pub_date="2023-01-01", reporter=r1)

    a2 = await Article.create(headline="Article 2", pub_date="2023-01-02", reporter=r2)


if __name__ == '__main__':
    run_async(run())
```

## 例子4-多对多

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: tortoise_orm_ex
@Author：Sam Lau
@file： test03.py
@date：2023/8/22 14:30
 """
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class Publication(Model):
    title = felds.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(Model):
    headline = (fields.CharField(max_length=100))
    publications = fields.ManyToManyField('models.Publication')

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline


async def run():
    await Tortoise.init(db_url="sqlite://test003.db", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    p1 = await Publication.create(title="Python")
    p2 = await Publication.create(title="Django")
    p3 = await Publication.create(title="Flask")

    a1 = await Article.create(headline="Article 1")
    await a1.publications.add(p1)

    a2 = await  Article.create(headline="Article 2")

    await  a2.publications.add(p2, p3)


if __name__ == '__main__':
    run_async(run())
```

# Tortoise ORM 拓展

###### [tortoise-orm 之Field的参数、属性、方法](https://www.cnblogs.com/zhongyehai/p/15182408.html)

[tortoise-orm 之常用字段类型和参数](https://www.cnblogs.com/zhongyehai/p/15187199.html)

[tortoise-orm 之Model、QuerySet提供的查询方法](https://www.cnblogs.com/zhongyehai/p/15202038.html)

[tortoise-orm 之Q对象 ](https://www.cnblogs.com/zhongyehai/p/15208048.html)

[tortoise-orm 之Model、QuerySet提供的数据操作方法 ](https://www.cnblogs.com/zhongyehai/p/15208134.html)

# aerich操作说明

[tortoise/aerich: A database migrations tool for TortoiseORM, ready to production. (github.com)](https://github.com/tortoise/aerich)

[Sanic二十二：Sanic + tortoise-orm 之使用aerich执行数据库迁移 - 向前走。 - 博客园](https://www.cnblogs.com/zhongyehai/p/15178096.html)

1.准备好配置：setting.py

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829163712666-1586939295.png)

```python
TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456@localhost:3306/test?charset=utf8mb4"},  # MySQL
    # "connections": {"default": "sqlite://db.sqlite3"},  # sqlite
    "apps": {
        # 模型分组名字，当需要使用此app下的模型的时候，需使用 此名字.模型名称
        "test_models": {
            # 须添加"aerich.models", 此时，会在数据库中生成一个名为aerich的表用于存模型信息，以便以后做脚本迁移
            "models": ["aerich.models", "user", "project"],  # 模型所在的py文件
            "default_connection": "default"
        }
    }
}
```

2.执行aerich初始化：aerich init -t 指定配置  
`aerich init -t settings.TORTOISE_ORM`

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210823223535147-787775520.png)

将会在目录下生成空的` migrations` 文件夹和 `aerich.ini` 文件

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210823223640463-2008743184.png)

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210823223655845-1436917880.png)

3.将模型映射到数据库中：`aerich init-db`

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210823223809686-787803568.png)

此时数据库中就会生成对应的表

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829163806004-232248718.png)

migrations 下将会生成SQL语句

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829164127783-2048884581.png)

4.如果修改了模型则需要重新生成SQL语句，并推送到数据库,重新生成SQL语句：`aerich migrate`

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829164306799-495825022.png)

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829164349201-1343456082.png)

5.新生成的SQL推送到数据库：`aerich upgrade`

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829164413334-1830469606.png)

6.如果要回到上一个版本：`aerich downgrade`

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210829164543159-548261616.png)

7.查看历史迁移记录：`aerich history`

8.查看形成当前版本的迁移记录文件：`aerich heads`

9.aerich 除了提供命令行之外，还提供了代码内执行的办法，从aerich引入 Command类即可，提供的方法与命令行一样

![](https://img2020.cnblogs.com/blog/1406024/202108/1406024-20210823224957414-1007760820.png)

```python
from aerich import Command

command = Command(tortoise_config=config, app='models')
await command.init()
await command.migrate('test')
```

# [tortoise ORM 使用经验](https://www.cnblogs.com/pearlcity/p/17829736.html)

```python
1.Tortoise ORM 在项目中的配置
1.配置TORTOISE_ORM，参见：https://www.cnblogs.com/puffer/p/16428100.html
2.main.py主程序中进行注册
from tortoise.contrib.fastapi import register_tortoise
app = FastAPI()
@app.on_event("startup")
async def startup_event():
    # generate_schemas=True 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True 生产环境不要开，会泄露调试信息
    register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False, add_exception_handlers=False)
3.创建模型
from tortoise import Model
from tortoise import fields


class UserModel(DateTimeModel):
    """用户表"""
    uuid = fields.UUIDField(source_field="uuid", pk=True, unique=True, description="用户唯一标识")
    name = fields.CharField(source_field="name", max_length=30, description="用户名称")
    age = fields.IntField(source_field="age", description="用户年龄")
    password = fields.CharField(source_field="password", max_length=50, description="用户密码")

    class Meta:
        table = "user"  # 表名
        # abstract=True  # 是否为抽象模型，用于继承，且不会在数据库中生成数据表
        unique_together=(("name", "password"), )  #  联合约束
        table_description = "用户表"  # 数据库对该表的注释
        indexes=(("name", "password"),)  #  联合索引
        ordering = ["xxx", "-xxx"]  # 设置默认查询结果的顺序，-代表降序
2.Tortoise ORM 增删改查
1.查询
1.使用 await 和 不使用 await 的区别

1.使用 await 查询时，得到的结果是Model对象，可以直接获取其属性
objs = await UserModel.filter(uuid__in=apps_uuid)
# {VirtualAppModel} <VirtualAppModel>
print(objs[0].name)
2.不适用 await 查询时，得到的是tortoise.queryset.QuerySet对象，无法通过循环遍历获取每一个对象的具体属性，但是支持链式查询，适合在进行分页时使用。
objs = UserModel.filter(uuid__in=apps_uuid)
# obj: <tortoise.queryset.QuerySet object at 0x00000132C4EBF160>
objs = objs.filter(name=xxx)
objs = objs.filter(xxx=xxxx)
2.判断对象是否存在
result = await UserModel.exists(uuid=xxx)
3.获取单条数据
user = await UserModel.get(uuid=xxx)  # <UserModel>
# 1.如果查询到多条数据，则抛出异常：tortoise.exceptions.MultipleObjectsReturned
# 2.如果没找到数据，则抛出异常：tortoise.exceptions.DoesNotExist
user = await UserModel.get_or_none(uuid=xxx)  # <UserModel> or None
# 1.如果没找到数据，返回：None
# 2.如果查询到多条数据，则抛出异常：tortoise.exceptions.MultipleObjectsReturned
3.获取多条数据

users = await UserModel.filter(name=xxx)  # [<UserModel>]
4.获取所有数据

users = await UserModel.all()  # [<UserModel>, <UserModel>, ...]
5.获取第一条数据

data = await UserModel.first()  # [<UserModel>]
6.仅获取模型中部分的字段

data_dict = await UserModel.first().values("name", "uuid")
# 如果查询结果是单条数据：{'name': '222224', 'uuid': '35f01c8a57aa44008c99682f0eece37a'}
# 如果查询结果是多条数据：[{'name': 'xxx', 'uuid': 'xxx'}, {'name': 'xxx', 'uuid': 'xxx'}]

data_tuple = await UserModel.first().values_list("name", "uuid")  
# 元组形式，只返回值：('222224', '35f01c8a57aa44008c99682f0eece37a')
# 多条数据：[('222224', '35f01c8a57aa44008c99682f0eece37a'), ('xxx', 'xxx')]

# 如果相获取多条数据中的某一个字段，比如uuid，正常情况下返回：[('xxx',), ('xxx'),...]
# 但如果想要的结果为：['xxx', 'xxx', 'xxx', ...]，就需要另一个参数了
uuid_list = await UserModel.filter(name__startswith='xxx').values_list("uuid", flat=True) 

# 如果想获取部分字段，但是以object对象形式返回
data = await VirtualAppModel.first().only("name") 
# 如果查询结果是单条数据：<UserModel>，不过这个模型对象中只有name属性，强行获取其他属性，则会报错
# 如果查询结果是多条数据：[<UserModel>]
7.select_related、prefetch_related，常用于关联模型查询中，减少数据库访问频次，提高查询性能，此处不多做演示，具体可以查看django orm中的示例https://blog.csdn.net/qq_42517220/article/details/93381250

8.不等于：exclude，比如查询name不等于111的用户

data = await UserModel.exclude(name='111')
9.数据去重

data = await UserModel.filter(name='111').distinct()
10.统计条数

num = await UserModel.filter(name='test').count()
# 或者
queryset = UserModel.filter(name='test')
num = await queryset.count()
data = await queryset.all()
11.聚合查询

from tortoise.functions import Count, Trim, Lower, Upper, Coalesce

await Tournament.annotate(events_count=Count('events')).filter(events_count__gte=10)
await Tournament.annotate(clean_name=Trim('name')).filter(clean_name='tournament')
await Tournament.annotate(name_upper=Upper('name')).filter(name_upper='TOURNAMENT')
await Tournament.annotate(name_lower=Lower('name')).filter(name_lower='tournament')
await Tournament.annotate(desc_clean=Coalesce('desc', '')).filter(desc_clean='')
12.双下划线查询：根据字段值进行过滤

关键字    意义    使用方法
not    不等于    name__not='xxx'
in    范围内    name__in=['xxx', 'xxx']
not_in    范围外    name__not_in=['xxx', 'xxx']
gte    大于或等于    age__gte=22
gt    大于    age__gt=22
lte    小于等于    age__lte=45
lte    小于    age__lt=45
range    范围查询    age__range=(18,45)
isnull    null查询    desc__isnull=True
not_isnull    非null查询    desc__not_isnull=True
contains    包含查询    name__contains="test"
icontains    不区分大小写包含查询    name__icontains="test"
startswith    开头查询    name__startswith="test"
istartswith    不区分大小写开头查询    name__istartswith="test"
endswith    结尾查询    name__endswith="test"
iendswith    不区分大小写结尾查询    name__iendswith="test"
iexact    不区分大小写的等于    name__iexact="test"
search    全文检索（测试报错）    name__search="test"
year    年份查询    created_at__year=2020
month    月份查询    created_at__month=7
day    日查询    created_at__day=24
13.JSON类型数据查询

# 1.列表形式
# extra字段值：["text", 3, {"msg": "msg2"}]
obj = await UserModel.filter(extra__contains=[{"msg": "msg2"}]).first()

# 2.字典形式
# extra字段值：{"breed": "labrador", owner": {"name": "Boby", "last": None, other_pets": [{"name": "Fishy"}]}}
# 2.1根据字段进行精确匹配（可以使用上述双下划线查询，比如：name__not进行不等于查询）
obj1 = await UserModel.filter(extra__filter={"breed": "labrador"}).first()
# 2.2嵌套字典数据获取
obj2 = await UserModel.filter(extra__filter={"owner__name": "Boby"}).first()
# 2.3获取嵌套数据中的列表数据
obj3 = await UserModel.filter(data__filter={"owner__other_pets__0__name": "Fishy"}).first()
14.Q查询

from tortoise.expressions import Q

users = await UserModel.filter(Q(name='a') | Q(name='b'))
# 等效于：如果省略join_type，则为AND
users = await UserModel.filter(Q(Q(name='a'), Q(name='b'), join_type="OR"))

# ~Q：不等于
users = await UserModel.filter(~Q(name='a'))
15.F表达式

from tortoise.expressions import F

await UserModel.filter(uuid='xxx').update(age=F('age')-10)
2.创建
1.单条数据创建
user = await UserModel.create(uuid="xxx", name="xxx")  # <UserModel>
# 或者
user = User(uuid="xxx", name="xxx")
await user.save()
2.批量创建
bulk_data = list()
    for uuid in users_uuid:
    bulk_data.append(await UserModel(uuid=uuid, name="xxx"))
await UserModel.bulk_create(bulk_data)
3.查询或创建（如果查询得到，则返回该对象，否则直接创建）
# 根据名称查询，查询不到，则创建一条数据：name:xxx，age: 12
user = await UserModel.get_or_create(name='xxx', defaults={'age': 12})
3.更新
1.根据条件更新
# 返回更新的数目：int
num = await UserModel.filter(uuid='xxx').update(age=24)

# 或者
user = await UserModel.get(uuid='xxx')
user.age = F('age') + 10
await user.save(update_fields=['balance'])
2.更新还是创建
# 根据name=111查询，如果有数据，则更新age=26，password=password；否则，创建一条数据，name='11111'、age=26、password=password
# 返回结果为元组，第一个元素为Model对象，第二个元素为是否新创建的数据
data, is_create = await UserModel.update_or_create(name="11111", defaults={"age": 26, "password": "password"})
4.删除
1.删除全部
# 删除的条目数
num = await UserModel.all().delete()
2.根据条件删除
# 删除的条目数
num = await UserModel.filter(uuid='xxx').delete()
```
