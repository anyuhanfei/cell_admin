from flask import render_template, request, session

from . import admin
from configs.common import return_data

from models.SysAdmin import SysAdmin


@admin.route('login')
def login():
    return render_template('admin/login.html')


@admin.route('login/submit', methods=['POST'])
def login_submit():
    account = request.form.get('account')
    password = request.form.get('password')
    if account is None or password is None:
        return return_data(2, '', '请填写账号或密码')
    admins = SysAdmin.query.filter(account == account)
    if admins.count() < 1:
        return return_data(2, '', '没有此管理员')
    admin = admins.first()
    if not admin.comparison_password(password):
        return return_data(2, '', '密码输入错误')
    session['admin_id'] = admin.admin_id
    return return_data(1, '', '登录成功')
