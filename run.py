import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from configs import config


app = Flask(__name__, template_folder='templates', static_folder='statics')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{HOSTPORT}/{DATABASE}'.format(
    USERNAME=config.DATABASE['USERNAME'],
    PASSWORD=config.DATABASE['PASSWORD'],
    HOSTNAME=config.DATABASE['HOSTNAME'],
    HOSTPORT=config.DATABASE['HOSTPORT'],
    DATABASE=config.DATABASE['DATABASE']
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

app.config['SESSION_TYPE'] = 'filesystem'  # session类型为filesystem
app.config['SESSION_FILE_DIR'] = '/logs/session'  # session类型为filesystem

app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密

db = SQLAlchemy(app)

from apps.admin import admin as admin_blueprint


app.register_blueprint(admin_blueprint, url_prefix='/admin')


if __name__ == "__main__":
    # 启动
    app.run(debug=config.APP_DEBUG)
