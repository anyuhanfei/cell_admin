'''
会员模块
'''
from flask import render_template, redirect, url_for

from . import admin, check_admin_login, check_admin_power, search, return_data, get_request
from run import db
from configs.config import USER

from models.IdxUser import IdxUser
from models.IdxUserFund import IdxUserFund
from models.IdxUserData import IdxUserData


@admin.route('/user/会员/<int:page>')
@check_admin_login
@check_admin_power
def 会员(page):
    parameters = search('会员', ['account', 'is_freeze'])
    obj = IdxUser.query
    obj = obj.filter(IdxUser.account == parameters['account']) if parameters['account'] != '' else obj
    obj = obj.filter(IdxUser.is_freeze == parameters['is_freeze']) if parameters['is_freeze'] != '' else obj
    models = obj.order_by(IdxUser.user_id.desc()).paginate(page=page, per_page=30)
    return render_template('/admin/user/会员.html', user=USER, models=models, parameters=parameters)


@admin.route('/user/添加会员')
@check_admin_login
@check_admin_power
def 添加会员():
    return render_template('/admin/user/添加会员.html', user=USER)


@admin.route('/user/添加会员提交', methods=['POST'])
@check_admin_login
@check_admin_power
def 添加会员提交():
    nickname, account, password, level_password, top_account = get_request('nickname', 'account', 'password', 'level_password', 'top_account')
    identity_text = USER['USER_IDENTITY_TEXT']
    if account == '':
        return return_data(2, '', '请输入' + identity_text)
    top_id = 0
    if top_account != '':
        top_user = IdxUser.query.filter(IdxUser.account == top_account).first()
        if top_user:
            top_id = top_user.user_id
        else:
            return return_data(2, '', '上级' + identity_text + '输入错误')
    IdxUser.create_data(nickname, account, password, level_password, top_id)
    return return_data(1, '', '添加成功', '添加会员:' + account)


@admin.route('/user/会员编辑/<int:id>')
@check_admin_login
@check_admin_power
def 会员编辑(id):
    user = IdxUser.query.filter(IdxUser.user_id == id).first()
    if user is None:
        return redirect(url_for('admin.error'))
    return render_template('/admin/user/会员编辑.html', user=user, id=id, USER=USER)


@admin.route('/user/会员编辑提交/<int:id>/<int:code>', methods=["POST"])
@check_admin_login
@check_admin_power
def 会员编辑提交(id, code):
    obj = IdxUser.query.filter(IdxUser.user_id == id).first()
    if obj is None:
        return return_data(2, '', '非法操作')
    if code == 4:
        标签 = get_request('标签')
        obj = IdxUserData.query.filter(IdxUserData.user_id == id, IdxUserData.key == '标签').first()
        if obj is None:
            return return_data(2, '', '非法操作')
        obj.value = 标签
    elif code == 3:
        level_password = get_request('level_password')
        if level_password == '':
            return return_data(2, '', '请输入新二级密码')
        obj.level_password = level_password
    elif code == 2:
        password = get_request('password')
        if password == '':
            return return_data(2, '', '请输入新二级密码')
        obj.password = IdxUser.get_encryption_password(password, obj.password_salt)
    elif code == 1:
        nickname, account = get_request('nickname', 'account')
        if nickname == '' or account == '':
            return return_data(2, '', '有未填写信息')
        obj.nickname = nickname
        obj.account = account
    else:
        return return_data(2, '', '非法操作')
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '编辑成功', '编辑会员' + obj.account + '的' + ['其他', '昵称或账号', '登录密码', '二级密码', '标记'][code])


@admin.route('/user/会员详情')
@check_admin_login
@check_admin_power
def 会员详情():
    user = IdxUser.query.filter(IdxUser.user_id == id).first()
    if user is None:
        return redirect(url_for('admin.error'))
    return render_template('/admin/user/会员详情.html', user=user, id=id)


@admin.route('/user/会员充值/<int:id>')
@check_admin_login
@check_admin_power
def 会员充值(id):
    user = IdxUser.query.filter(IdxUser.user_id == id).first()
    if user is None:
        return redirect(url_for('admin.error'))
    return render_template('/admin/user/会员充值.html', user=user, funds=user.fund(), id=id)


@admin.route('/user/会员充值提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 会员充值提交(id):
    fund_type, radio_number, input_number = get_request('fund_type', 'radio_number', 'input_number')
    if fund_type == '':
        return return_data(2, '', '请选择充值币种')
    try:
        number = int(radio_number if (input_number == '') else input_number)
    except BaseException:
        return return_data(2, '', '请选择或填写正确的充值金额')
    if number <= 0:
        return return_data(2, '', '请选择或填写充值金额')
    user = IdxUser.query.filter(IdxUser.user_id == id).first()
    if user is None:
        return return_data(2, '', '非法操作')
    res = IdxUserFund.update_amount(id, fund_type, number, '后台充值')
    if res is True:
        return return_data(1, '', '充值成功', '给会员' + user.account + '充值' + str(number) + fund_type)
    else:
        return return_data(2, '', '充值失败')


@admin.route('/user/冻结会员提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 冻结会员提交(id):
    obj = IdxUser.query.filter(IdxUser.user_id == id).first()
    if obj is None:
        return return_data(2, '', '非法操作')
    obj.is_freeze = 1 if obj.is_freeze == 0 else 0
    db.session.add(obj)
    db.session.commit()
    if obj.is_freeze == 0:
        return return_data(1, obj.is_freeze, '解冻成功', '解冻会员' + obj.account)
    else:
        return return_data(1, obj.is_freeze, '冻结成功', '冻结会员' + obj.account)


@admin.route('/user/删除会员提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 删除会员提交(id):
    if USER['UESR_DELETE'] is False:
        return return_data(2, '', '禁止删除会员')
    obj = IdxUser.query.filter(IdxUser.user_id == id).first()
    if obj is None:
        return return_data(2, '', '非法操作')
    obj.is_delete = 1
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '删除成功', '删除会员' + obj.account)
