## 创建迁移文件夹

- 项目第一次运行, 生成migrations文件夹

`alembic init -t async migrations`

## 修改配置文件

- env文件路径: `backend/migrations/env.py`

```py
# 导入SQLModel

from sqlmodel import SQLModel  

# 导入模型数据

from app.models import *  

# 设置metadata

target_metadata = SQLModel.metadata
```

- ini文件路径: `backend/alembic.ini`

```py
# 修改成项目的异步数据库连接

sqlalchemy.url = sqlite+aiosqlite:///amisadmin.db`
```

## 生成迁移文件

- 执行命令, 生成sqlModel 初始化迁移文件

`alembic revision --autogenerate`

## 更新数据库

`- 执行命令, 更新数据库: alembic_version alembic upgrade head`

## 迁移

- 以下命令在每次修改完模型后执行一次.
  
  - `执行命令, 生成sqlModel 更新迁移文件 
  
  - `alembic revision --autogenerate `
  
  - `执行命令, 更新数据库: alembic_version 
  
  - `alembic upgrade head`


