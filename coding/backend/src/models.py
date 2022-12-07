from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base

# 本文件对MySQL中已存在的数据表进行描述（每张表对应一个 Class）

Base = declarative_base()
metadata = Base.metadata


# admin 表
class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True)
    admin_pwd = Column(String(20), nullable=False)
    admin_name = Column(String(128), nullable=False)
    admin_email = Column(String(128), nullable=False)

#
# # user 表
# class User(Base):
#     __tablename__ = "user"
#
#     user_id = Column(Integer, primary_key=True)
#
#
# # coverage 表
# class Coverage(Base):
#     __tablename__ = "coverage"
#
#     cov_id = Column(Integer, primary_key=True)
#     tab_id = Column(Integer, primary_key=True)
#     cov_name = Column(String(50), nullable=False)
#
#
# # data_table 表
# class DataTable(Base):
#     __tablename__ = "data_table"
#
#     tab_id = Column(Integer, primary_key=True)
#     cov_id = Column(Integer, primary_key=True)
#     tab_name = Column(String(50), nullable=False)
#
#
# # data_column 表
# class DataColumn(Base):
#     __tablename__ = "data_column"
#
#     col_id = Column(Integer, primary_key=True)
#     tab_id = Column(Integer, primary_key=True)
#     col_name = Column(String(50), nullable=False)
#     col_text = Column(String(100), nullable=False)
#
#
# # tag 表
# class Tag(Base):
#     __tablename__ = "tag"
#
#     tag_id = Column(BigInteger, primary_key=True)
#     tab_id = Column(BigInteger, key=True, default=1)
#     tag_text = Column(String(100), nullable=False)
