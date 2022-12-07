from flask import Blueprint, request, jsonify, session
from src.database import db
from src.models import Admin
from sqlalchemy.orm import sessionmaker
import json

accounts = Blueprint('accounts', __name__)


@accounts.route("/signup", methods=["POST"])
def sign_up():
    db_session = sessionmaker(bind=db)()

    account_data = json.loads(request.get_data())
    name = account_data['name']
    email = account_data['email']
    password = account_data['password']

    if name is None or password is None:
        return jsonify({'error': '缺少必要信息'})

    query = db_session.execute(
        'select * from admin where admin_name = %s' % name
    ).all()
    if query:
        return jsonify({'error': '用户名已存在'})

    db_session.execute(
        'insert into admin(admin_pwd, admin_name, admin_email) values("%s", "%s", "%s")'
        % (password, name, email)
    )
    db_session.commit()
    db_session.close()

    return jsonify({'OK': '注册成功'})


@accounts.route("/login", methods=["POST"])
def log_in():
    db_session = sessionmaker(bind=db)()

    account_data = json.loads(request.get_data())
    name = account_data['name']
    password = account_data['password']
    print(name, password)

    if name is None or password is None:
        return jsonify({'error': '缺少必要信息'})

    query = db_session.query(Admin).filter(Admin.admin_name == name).filter(Admin.admin_pwd == password).all()

    if query:
        return jsonify({'OK': '登录成功'})
    else:
        return jsonify({'error': '用户名或密码错误'})
