官方文档----[Tortoise ORM - Tortoise ORM v0.20.0 Documentation](https://tortoise.github.io/index.html)

数据迁移---- [GitHub - tortoise/aerich: A database migrations tool for TortoiseORM, ready to production.](https://github.com/tortoise/aerich)

示例说明-----[Examples - Tortoise ORM v0.20.0 Documentation](https://tortoise.github.io/examples.html)

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
