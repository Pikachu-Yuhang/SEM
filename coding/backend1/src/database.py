from sqlalchemy import create_engine
# 进行数据库配置 mysql+pymysql://用户名:密码@服务器:端口号/数据库名称
DB_URI = 'mysql+pymysql://root:0322@localhost:3306/sem'

db = create_engine(DB_URI)