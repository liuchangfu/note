# Mysql与Fastapi代码示例

## 数据库配置

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

# 数据库连接Session

    from .db import LocalSession
    
    
    def get_db():
        try:
            db = LocalSession()
            yield db
        finally:
            db.close()

# 数据库模型

    from extend.db import Base
    from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
    import datetime
    from sqlalchemy.orm import relationship
    
    
    class Department(Base):
        __tablename__ = "department"
        id = Column(Integer, primary_key=True, autoincrement=True)
        # 部门名称
        name = Column(String(255), unique=True)
        # 部门主管
        leader = Column(String(255))
        # 部门职责
        desc = Column(String(255))
        # 用户表的反向关系
        user = relationship("User", backref="department")
        # 创建时间: 年月日 时分秒
        create_time = Column(DateTime, default=datetime.datetime.now)
        # 创建日期：年月日
        create_date = Column(Date, default=datetime.datetime.now)

# 数据库操作

    from sqlalchemy.orm import Session
    from models.user.user_model import User, Department, Docs, ShareItem
    from models.role.role_model import RoleUsers, Role
    import datetime
    
    
    # 获取用户信息，获取用户id,用户头像等信息
    def get_user_by_username_and_pwd(db: Session, username: str, md5_pwd: str) -> User:
        user = db.query(User.id, User.username, User.avatar, User.ip, User.last_login_date, User.state).filter(
            User.username == username, User.pwd == md5_pwd).first()
        return user
    
    
    # 获取用户登录时间
    def update_time_and_ip(db: Session, user_id: int, login_date: datetime.datetime, ip: str):
        user = db.query(User).filter(User.id == user_id).first()
        user.last_login_date = login_date
        user.ip = ip
        db.commit()
        db.flush()

## 接口代码

    @router.get("/user_list", tags=["用户模块"])
    def get_user_list(page_size: int, current_page: int, id: str = Depends(token.parse_token),
                      db: Session = Depends(get_db)):
        users = get_user_pagenation(db, page_size, current_page)
        total = get_user_total(db)
        departments = get_departments(db)
        content = {
            "departments": departments,
            "users": users,
            "pageSize": page_size,
            "pageTotal": total,
            "currentPage": current_page
        }
        return content