from flask import Blueprint, request, jsonify, session
from src.database import db
from sqlalchemy.orm import sessionmaker
import json

tables = Blueprint('tables', __name__)


@tables.route('/get_table_list', methods=["POST"])
def get_table_list():
    db_session = sessionmaker(bind=db)()

    tables = db_session.execute(
        "show tables from sem like '%_bl'"
    ).all()
    table_list = []
    for table in tables:
        table_list_item = {}
        table_list_item['table_name'] = table[0]

        table_columns = db_session.execute(
            "select COLUMN_NAME from information_schema.COLUMNS "
            "where table_name = '%s'"
            % table[0]
        ).all()

        table_list_item['table_columns'] = []
        for column in table_columns:
            table_list_item['table_columns'].append(column[0])

        table_list.append(table_list_item)

    return jsonify({
        'OK': 'success',
        'table_list': table_list
    })


@tables.route('/get_table_data', methods=["POST"])
def get_table_data():
    db_session = sessionmaker(bind=db)()

    table_name = request.get_data().decode()
    table_data = db_session.execute(
        'select * from %s' % table_name
    ).all()

    return_table_data = []
    for row in table_data:
        table_row = []
        for item in row:
            table_row.append(item)
        return_table_data.append(table_row)

    return jsonify({
        'OK': 'success',
        'table_data': return_table_data
    })