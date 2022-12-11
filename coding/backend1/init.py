from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:662258@localhost:3306/test'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db = SQLAlchemy(app)


# admin 表
class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True)
    admin_pwd = Column(String(20), nullable=False)
    admin_name = Column(String(20), nullable=False)


# user 表
class User(db.Model):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)


# coverage 表
class Coverage(db.Model):
    __tablename__ = "coverage"

    cov_id = Column(Integer, primary_key=True)
    tab_id = Column(Integer, primary_key=True)
    cov_name = Column(String(50), nullable=False)


# data_table 表
class DataTable(db.Model):
    __tablename__ = "data_table"

    tab_id = Column(Integer, primary_key=True)
    cov_id = Column(Integer, primary_key=True)
    tab_name = Column(String(50), nullable=False)


# data_column 表
class DataColumn(db.Model):
    __tablename__ = "data_column"

    col_id = Column(Integer, primary_key=True)
    tab_id = Column(Integer, primary_key=True)
    col_name = Column(String(50), nullable=False)
    col_text = Column(String(100), nullable=False)


# tag 表
class Tag(db.Model):
    __tablename__ = "tag"

    tag_id = Column(Integer, primary_key=True)
    tab_id = Column(Integer, primary_key=True)
    tag_text = Column(String(100), nullable=False)


@app.route('/')
def hello():
    db.drop_all()
    db.create_all()
    return "Create Fin..."


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
