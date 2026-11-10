# -*- coding: utf-8 -*-

from application import create_app
from application.extensions import db
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Запускаем встроенный сервер Flask напрямую, без Flask-Script
    app.run(host='127.0.0.1', port=7345)