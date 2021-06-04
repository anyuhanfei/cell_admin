from flask import render_template, request, session, redirect, url_for

from . import admin, reading_data
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
    admin_data = SysAdmin.query.filter(SysAdmin.account == account).first()
    print(admin_data)
    if admin_data is None:
        return return_data(2, '', '没有此管理员')
    if not admin_data.comparison_password(password):
        return return_data(2, '', '密码输入错误')
    session['admin_id'] = admin_data.admin_id
    reading_data()
    return return_data(1, '', '登录成功')


@admin.route('loginout')
def loginout():
    session['admin_id'] = None
    return redirect(url_for('admin.login'))
