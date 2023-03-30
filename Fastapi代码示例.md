# sqlalchemy代码说明

## 1.先定义数据库连接

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = "root"
pwd = "lcfwku"
host = "localhost"
port = "3306"
db_name = "share_system"

url = f"mysql+pymysql://{username}:{pwd}@{host}:{port}/{db_name}?charset=utf8"

Engin = create_engine(url)

LocalSession = sessionmaker(bind=Engin)

Base = declarative_base()
```

## 2.生成全局Session

    from .db import LocalSession
    
    def get_db():
        try:
            db = LocalSession()
            yield db
        finally:
            db.close()

## 3.导入数据库相关配置

```python
from extend.db import Engin, LocalSession, Base
from sqlalchemy.orm import Session
from extend.get_db import get_db

# 创建数据库表结构
Base.metadata.create_all(bind=Engin)

#注入数据库相关配置
@app.get("/get_user", tags=["首页模块"])
def get_user(id: str = Depends(token.parse_token), db: Session = Depends(get_db)):
    user = get_user_by_id(db, int(id))
    return {"code": 200, "msg": "查询成功", "user": user}
```

接口开发步骤：

1.前台发起接口请求，并确定好是GET还是POST请求，发送请求时，是否需要传入参数

2.后台定义好接口，并接收前台发送过来的请求，处理相关逻辑，如存入数据库、接口字段校验等相关操作，并把数据返回到前端

3.前端收到后端返回的接口数据时，提取相应的数据，并渲染相关数据到网页上

# Body参数

主要作用：可以将单类型的参数成为 Request Body 的一部分，即从查询参数变成请求体参数
