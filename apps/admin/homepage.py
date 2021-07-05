'''
登录模块, 首页模块
'''

from flask import render_template, request, session, redirect, url_for

from . import admin, reading_data, check_admin_login
from configs.common import return_data, 保存图片

from models.SysAdmin import SysAdmin


@admin.route('/')
@check_admin_login
def homepage():
    return render_template('admin/homepage.html')


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


@admin.route('uploadphoto', methods=['GET', 'POST'])
def uploadphoto():
    photo = request.files.get('file')
    file_path = 保存图片(photo, 'editor')

    return 'http://' + request.host + '/' + file_path


@admin.route('/admin/error')
def error():
    return render_template('admin/error/error_operation.html')


@admin.route('/admin/error/admin_power')
def error_admin_power():
    return render_template('admin/error/error_admin_power.html')


@admin.route('/admin/error/developer')
def error_developer():
    return render_template('admin/error/error_developer.html')
