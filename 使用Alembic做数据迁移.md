# 包安装及初始化项目

1、安装包

	pip3 install alembic

2、在进入项目文件夹下初始化项目
	
	alembic init alembic

3、初始化后项目文件夹下会新增alembic文件夹和alembic.ini的文件

# 创建数据模型

1、在`alembic.ini`文件中找到改为你的数据库的连接信息

	sqlalchemy.url = driver://user:pass@localhost/dbname

改写后

	sqlalchemy.url = mysql+pymysql://root:root@localhost/sqlalchemy_data

2、修改`alembic/env.py`文件

	target_metadata = None

改为

	import sys
	from os.path import abspath, dirname
	
	sys.path.append(dirname(dirname(abspath(__file__))))
	# 注意这个地方是要引入模型里面的Base,不是connect里面的
	from sqlalchemy_demo.modules.user_module import Base
	target_metadata = Base.metadata

# 基本命令

1.创建迁移文件

	alembic revision --autogenerate -m "描述"

2.更新到最新的版本

	alembic upgrade head