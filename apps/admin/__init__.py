from flask import Blueprint, redirect, session, url_for, request
from functools import wraps

admin = Blueprint('admin', __name__)


def check_admin_login(function):
    '''装饰器: 判断会员是否登录'''
    @wraps(function)
    def decorated_function(*args, **kwargs):
        print(session)
        print(111)
        if 'admin_id' not in session or session['admin_id'] is None:
            return redirect(url_for("admin.login"))
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
    session['admin'] = {'admin_id': admin_data.admin_id, 'nickname': admin_data.nickname}

import apps.admin.login
import apps.admin.homepage
import apps.admin.resource
import apps.admin.sys
import apps.admin.adm
import apps.admin.set
