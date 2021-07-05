from flask import Blueprint, redirect, session, url_for, request
from functools import wraps

from configs.config import DEVELOPER, USER, ADMIN_POWER

admin = Blueprint('admin', __name__)


from models.SysModule import SysModule


def check_admin_login(function):
    '''装饰器: 判断管理员是否已登录'''
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # 登录判断
        if 'admin_id' not in session or session['admin_id'] is None:
            return redirect(url_for("admin.login"))
        return function(*args, **kwargs)
    return decorated_function


def check_admin_power(function):
    '''装饰器: 判断管理员权限'''
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # 权限判断
        print(session['admin']['power'])
        if session['admin']['power'] != 'all' and ADMIN_POWER is not False:
            当前路由 = request.path
            当前路由_obj = SysModule.query.filter(SysModule.路由 == 当前路由).first()
            print(当前路由)
            print(当前路由_obj)
            if 当前路由_obj is None:
                return redirect(url_for('admin.error'))
            if str(当前路由_obj.module_id) not in session['admin']['power']:
                return redirect(url_for('admin.error_admin_power'))
            
        return function(*args, **kwargs)
    return decorated_function


def check_admin_developer(function):
    '''装饰器: 判断管理员是否是开发者角色'''
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # 权限判断
        print(session['admin']['power'])
        if session['admin']['power'] != 'all':
            return redirect(url_for('admin.error_admin_power'))
        return function(*args, **kwargs)
    return decorated_function


def check_developer(function):
    '''装饰器: 判断开发者模式是否开启'''
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if session['DEVELOPER'] is False:
            return redirect(url_for("admin.error_developer"))
        return function(*args, **kwargs)
    return decorated_function


def reading_data():
    '''将公共数据保存到session中, 让所有方法都可使用'''
    from models.SysCatalog import SysCatalog
    from models.SysAdmin import SysAdmin

    # 后台目录
    目录 = SysCatalog.query.filter().order_by(SysCatalog.排序.asc()).all()
    session['目录'] = [value.json() for value in 目录]
    # 会员信息
    admin_data = SysAdmin.query.filter(SysAdmin.admin_id == session['admin_id']).first()
    admin_power = 'all' if admin_data.role_id == 1 else admin_data.role.权限.split(',')
    session['admin'] = {'admin_id': admin_data.admin_id, 'nickname': admin_data.nickname, 'power': admin_power}
    # 开发者模式
    session['DEVELOPER'] = DEVELOPER
    # 会员删除权限
    session['USER_DELETE'] = USER['USER_DELETE']

import apps.admin.homepage
import apps.admin.sys
import apps.admin.set
import apps.admin.user
import apps.admin.article
