Github地址如下

**[GitHub - MushroomMaula/fastapi_login: FastAPI-Login tries to provide similar functionality as Flask-Login does.](https://github.com/MushroomMaula/fastapi_login)**

示例代码如下，详细代码在如下地址[fastapi_login/examples/sqlalchemy at master · MushroomMaula/fastapi_login · GitHub](https://github.com/MushroomMaula/fastapi_login/tree/master/examples/sqlalchemy)

# security.py

```py
from config import DEFAULT_SETTINGS
from fastapi_login import LoginManager
from datetime import timedelta

manager = LoginManager(DEFAULT_SETTINGS.secret, DEFAULT_SETTINGS.token_url,
                       default_expiry=timedelta(minutes=30))  # 默认过期时间为15分钟


def hash_password(plaintext_password: str):
    """ Return the hash of a password """
    return manager.pwd_context.hash(plaintext_password)


def verify_password(password_input: str, hashed_password: str):
    """ Check if the provided password matches """
    return manager.pwd_context.verify(password_input, hashed_password)
```

# config.py

```python
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str  # automatically taken from environment variable
    database_uri: str = "sqlite:///app.db"
    token_url: str = "/auth/token"


DEFAULT_SETTINGS = Settings(_env_file=".env")
```

# db_action.py

```python
from typing import Optional

from sqlalchemy.orm import Session

from crud_models import UserCreate
from db import DBContext
from db_models import User
from security import hash_password, manager

# 获取用户，如没有查询到则返回None
@manager.user_loader
def get_user(email: str, db: Session = None) -> Optional[User]:
    """ Return the user with the corresponding email """
    if db is None:
        # No db session was provided so we have to manually create a new one
        # Closing of the connection is handled inside of DBContext.__exit__
        with DBContext() as db:
            return db.query(User).filter(User.email == email).first()
    else:
        return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """ Create a new entry in the database user table """
    user_data = user.dict()
    user_data["password"] = hash_password(user.password)
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

# app.py

```python
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from config import DEFAULT_SETTINGS
from crud_models import UserCreate, UserResponse
from db import get_db, Base, engine
from db_actions import get_user, create_user
from fastapi_login.exceptions import InvalidCredentialsException
from security import manager, verify_password

app = FastAPI()


@app.on_event("startup")
def setup():
    print("Creating db tables...")
    Base.metadata.create_all(bind=engine)
    print(f"Created {len(engine.table_names())} tables: {engine.table_names()}")


@app.post("/auth/register")
def register(user: UserCreate, db=Depends(get_db)):
    if get_user(user.email) is not None:
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    else:
        db_user = create_user(db, user)
        return UserResponse(id=db_user.id, email=db_user.email, is_admin=db_user.is_admin)


@app.post(DEFAULT_SETTINGS.token_url)  # /auth/token
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = get_user(email)  # we are using the same function to retrieve the user
    if user is None:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif not verify_password(password, user.password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data=dict(sub=user.email))
    return {'access_token': access_token, 'token_type': 'Bearer'}


@app.get("/private")
def private_route(user=Depends(manager)):
    return {"detail": f"Welcome {user.email}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app")
```
