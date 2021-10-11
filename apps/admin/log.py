'''
日志模块
'''
from flask import render_template

from . import admin, check_admin_login, search, check_admin_power
from configs.config import USER

from models.IdxUser import IdxUser
from models.SysAdmin import SysAdmin
from models.LogAdmin import LogAdmin
from models.LogUser import LogUser
from models.LogUserFund import LogUserFund


@admin.route('log/会员资金流水日志/<int:page>')
@check_admin_login
@check_admin_power
def 会员资金流水日志(page):
    parameters = search('会员资金流水日志', ['会员账号', '类型', '资金类型'])
    obj = LogUserFund.query
    if parameters['会员账号'] != '':
        user = IdxUser.query.filter(IdxUser.account == parameters['会员账号']).first()
        user_id = user.user_id if user is not None else 0
        obj = obj.filter(LogUserFund.user_id == user_id)
    obj = obj.filter(LogUserFund.说明 == parameters['类型']) if parameters['类型'] != '' else obj
    obj = obj.filter(LogUserFund.币种 == parameters['资金类型']) if parameters['资金类型'] != '' else obj
    models = obj.order_by(LogUserFund.id.desc()).paginate(page=page, per_page=50, error_out=False)
    资金类型 = USER['USER_FUND_TYPE']
    流水类型 = ['后台充值']
    return render_template('/admin/log/会员资金流水日志.html', models=models, parameters=parameters, 资金类型=资金类型, 流水类型=流水类型)


@admin.route('log/会员操作日志/<int:page>')
@check_admin_login
@check_admin_power
def 会员操作日志(page):
    parameters = search('会员操作日志', ['会员账号'])
    obj = LogUser.query
    if parameters['会员账号'] != '':
        user = IdxUser.query.filter(IdxUser.account == parameters['会员账号']).first()
        user_id = user.user_id if user is not None else 0
        obj = obj.filter(LogUser.user_id == user_id)
    models = obj.order_by(LogUser.id.desc()).paginate(page=page, per_page=50, error_out=False)
    return render_template('/admin/log/会员操作日志.html', models=models, parameters=parameters)


@admin.route('log/管理员操作日志/<int:page>')
@check_admin_login
@check_admin_power
def 管理员操作日志(page):
    parameters = search('管理员操作日志', ['管理员账号'])
    obj = LogAdmin.query
    if parameters['管理员账号'] != '':
        admin = SysAdmin.query.filter(SysAdmin.account == parameters['管理员账号']).first()
        admin_id = admin.admin_id if admin is not None else 0
        obj = obj.filter(LogAdmin.admin_id == admin_id)
    models = obj.order_by(LogAdmin.id.desc()).paginate(page=page, per_page=50, error_out=False)
    return render_template('/admin/log/管理员操作日志.html', models=models, parameters=parameters)
