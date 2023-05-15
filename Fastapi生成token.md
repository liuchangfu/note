# 代码示例:生成token与校验token

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# 密码加密对象
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 可以导入secrets模块，调用secrets.token_urlsafe(32)方法生成，其中32是指的SECRET_KEY的长度
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

# 加密方式
ALGORITHM = "HS256"


# 明文密码加密
def get_hash_pwd(pwd: str):
    return crypt_context.hash(pwd)


def verify_password(password: str, hashed_password: str) -> bool:
    """ 验证明文密码 与 加密后的密码 是否一致 """
    return crypt_context.verify(password, hashed_password)


# 生成token:用户数据，token过期时间
def create_token(data: dict, expire_time):
    if expire_time:
        expire = datetime.utcnow() + expire_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    data.update({"exp": expire})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


# post请求，相对  /login
oauth_scame = OAuth2PasswordBearer(tokenUrl="login")  


# token校验
def parse_token(token: str = Depends(oauth_scame)):
    token_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token不正确或已过期",
                                    headers={"WWW-Authenticate": "Beater"})
    try:
        jwt_data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id = jwt_data.get("sub")
        if id is None or id == "":
            raise token_exception
    except JWTError:
        raise token_exception
    return id
```

# 密码加密

```python
import hashlib


# 密码md5加密
def get_md5_pwd(pwd: str):
    m = hashlib.md5()
    m.update(pwd.encode('utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    print(get_md5_pwd('123456'))
```

# #  接口调用

```python
@app.post("/login", tags=["登录模块"])
def Login(request: Request, user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1.用户信息获取
    username = user.username
    pwd = user.password
    # 密码加密
    md5_pwd = get_md5_pwd(pwd)
    # 2.数据库校验
    user = get_user_by_username_and_pwd(db, username, md5_pwd)

    if user:
        # 停用的不让登录
        if user.state == 2:
            content = {"code": 500, "msg": "该用户已停用,请联系管理员!"}
            return JSONResponse(content=content)
        # 启用的正常执行
        # 3.token生成
        expire_time = timedelta(minutes=EXPIRE_MINUTE)
        ret_token = token.create_token({"sub": str(user.id)}, expire_time)

        # 4.返回token及用户信息
        # 日期格式需要转成字符串
        ret_user = {"username": user.username, "avatar": user.avatar, "ip": user.ip,
                    "last_login_date": user.last_login_date.strftime("%Y-%m-%d")}
        login_date = datetime.datetime.now()
        ip = request.client.host
        update_time_and_ip(db, user.id, login_date, ip)
        content = {"code": 200, "msg": "登录成功", "token": ret_token, "user": ret_user}
        return JSONResponse(content=content)
    else:
        content = {"code": 500, "msg": "用户名或密码错误"}
        return JSONResponse(content=content)

@app.get("/get_user", tags=["首页模块"])
def get_user(id: str = Depends(token.parse_token), db: Session = Depends(get_db)):
    user = get_user_by_id(db, int(id))
    return {"code": 200, "msg": "查询成功", "user": user}
```

[token认证登陆](https://www.cnblogs.com/CharmCode/p/14191112.htmlJWT)
