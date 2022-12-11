from flask import Flask
from src.accounts import accounts
from src.tables import tables
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "test"
CORS(app, supports_credentials=True)

app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(tables, url_prefix='/tables')

@app.route('/')
def hello():
    return "Link OK"


if __name__ == '__main__':
    # 可以在这里改端口号，但是要用 python app.py 运行
    app.run(debug=True, host="0.0.0.0", port=5000)
