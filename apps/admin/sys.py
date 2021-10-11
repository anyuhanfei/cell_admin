'''
角色模块, 管理员模块, 目录模块, 方法管理模块, 静态资源模块
'''
from flask import render_template, redirect, url_for

from . import admin, check_admin_login, reading_data, check_developer, check_admin_power, check_admin_developer, return_data, get_request
from run import db
from configs.common import 随机字符串

from models.SysCatalog import SysCatalog
from models.SysModule import SysModule
from models.SysRole import SysRole
from models.SysAdmin import SysAdmin


@admin.route('/adm/角色')
@check_admin_login
@check_admin_power
def 角色():
    data = SysRole.query.filter().all()
    return render_template('/admin/adm/角色.html', data=data)


@admin.route('/adm/添加角色')
@check_admin_login
@check_admin_power
def 添加角色():
    return render_template('/admin/adm/添加角色.html')


@admin.route('/adm/添加角色提交', methods=['POST'])
@check_admin_login
@check_admin_power
def 添加角色提交():
    角色名, 备注 = get_request('角色名', '备注')
    if 角色名 == '':
        return return_data(2, '', '请填写角色名')
    role = SysRole(角色名=角色名, 备注=备注)
    db.session.add(role)
    db.session.commit()
    return return_data(1, '', '添加成功', '添加角色:' + 角色名)


@admin.route('/adm/修改角色/<int:id>')
@check_admin_login
@check_admin_power
def 修改角色(id):
    data = SysRole.query.filter(SysRole.role_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    return render_template('/admin/adm/修改角色.html', data=data, id=id)


@admin.route('/adm/修改角色提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 修改角色提交(id):
    角色名, 备注 = get_request('角色名', '备注')
    data = SysRole.query.filter(SysRole.role_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    data.角色名, data.备注 = 角色名, 备注
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功', '修改角色：' + data.角色名)


@admin.route('/adm/修改角色权限/<int:id>')
@check_admin_login
@check_admin_power
def 修改角色权限(id):
    if id == 1:
        return redirect(url_for('admin.error'))
    data = SysRole.query.filter(SysRole.role_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    权限 = data.权限.split(',')
    module = SysModule.query.filter().all()
    for i in range(0, len(module)):
        if str(module[i].module_id) in 权限:
            module[i].是否选中 = True
        else:
            module[i].是否选中 = False
    return render_template('/admin/adm/修改角色权限.html', 权限=权限, id=id, module=module)


@admin.route('/adm/修改角色权限提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 修改角色权限提交(id):
    if id == 1:
        return return_data(2, '', '不允许修改开发者角色的权限')
    action_ids = get_request('action_ids')
    data = SysRole.query.filter(SysRole.role_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    data.权限 = action_ids
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, '', '设置成功', '设置角色权限:' + data.角色名)


@admin.route('/adm/删除角色提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 删除角色提交(id):
    if id == 1:
        return return_data(2, '', '不允许删除开发者角色')
    data = SysRole.query.filter(SysRole.role_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    db.session.delete(data)
    db.session.commit()
    return return_data(1, '', '删除成功', '删除角色:' + data.角色名)


@admin.route('/adm/管理员')
@check_admin_login
@check_admin_power
def 管理员():
    data = SysAdmin.query.filter().all()
    角色 = SysRole.query.filter().all()
    return render_template('admin/adm/管理员.html', data=data, 角色=角色)


@admin.route('/adm/添加管理员')
@check_admin_login
@check_admin_power
def 添加管理员():
    角色 = SysRole.query.filter().all()
    return render_template('admin/adm/添加管理员.html', 角色=角色)


@admin.route('/adm/添加管理员提交', methods=['POST'])
@check_admin_login
@check_admin_power
def 添加管理员提交():
    account, nickname, role_id, password = get_request('account', 'nickname', 'role_id', 'password')
    if account == '' or nickname == '' or password == '' or role_id == '':
        return return_data(2, '', '请完善信息')
    role = SysRole.query.filter(SysRole.role_id == role_id).first()
    if role is None:
        return return_data(2, '', '请选择正确的角色')
    password_salt = 随机字符串(6, '数字+小写字母')
    admin = SysAdmin(
        account=account,
        nickname=nickname,
        role_id=role_id,
        password=SysAdmin.get_encryption_password(password, password_salt),
        password_salt=password_salt
    )
    db.session.add(admin)
    db.session.commit()
    return return_data(1, '', '添加成功', '添加管理员:' + account)


@admin.route('/adm/修改管理员/<int:id>')
@check_admin_login
@check_admin_power
def 修改管理员(id):
    if id == 1:
        return redirect(url_for('admin.error'))
    data = SysAdmin.query.filter(SysAdmin.admin_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    角色 = SysRole.query.filter().all()
    return render_template('admin/adm/修改管理员.html', data=data, id=id, 角色=角色)


@admin.route('/adm/修改管理员提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 修改管理员提交(id):
    account, nickname, role_id, password = get_request('account', 'nickname', 'role_id', 'password')
    if account == '' or nickname == '' or role_id == '':
        return return_data(2, '', '请完善信息')
    role = SysRole.query.filter(SysRole.role_id == role_id).first()
    if role is None:
        return return_data(2, '', '请选择正确的角色')
    data = SysAdmin.query.filter(SysAdmin.admin_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    if password != '':
        data.password = SysAdmin.get_encryption_password(password, data.password_salt)
    data.account, data.nickname, data.role_id = account, nickname, role_id
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功', '修改管理员信息:' + data.account)


@admin.route('/adm/管理员角色设置/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 管理员角色设置(id):
    role_id = get_request('role_id')
    role = SysRole.query.filter(SysRole.role_id == role_id).first()
    if role is None:
        return return_data(2, '', '请选择正确的角色')
    data = SysAdmin.query.filter(SysAdmin.admin_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    data.role_id = role_id
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, '', '设置成功', '设置管理员' + data.account + '角色为' + role.角色名)


@admin.route('/adm/删除管理员提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 删除管理员提交(id):
    data = SysAdmin.query.filter(SysAdmin.admin_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    data.is_delete = 1
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '删除成功', '删除管理员' + data.account)


@admin.route('sys/目录')
@check_admin_login
@check_admin_developer
@check_developer
def 目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/目录.html', 一级目录=一级目录, 二级目录=二级目录)


@admin.route('sys/添加一级目录')
@check_admin_login
@check_admin_developer
@check_developer
def 添加一级目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/添加一级目录.html', 一级目录=一级目录)


@admin.route('sys/添加一级目录提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加一级目录提交():
    名称, 图标, 排序 = get_request('名称', '图标', '排序')
    catalog = SysCatalog(名称=名称, 图标=图标, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    reading_data()
    return return_data(1, '', '添加成功')


@admin.route('sys/添加二级目录')
@check_admin_login
@check_admin_developer
@check_developer
def 添加二级目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/添加二级目录.html', 一级目录=一级目录, 二级目录=二级目录)


@admin.route('sys/添加二级目录提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加二级目录提交():
    名称, 上级id, 路由, 排序 = get_request('名称', '上级id', '路由', '排序')
    catalog = SysCatalog(名称=名称, 上级id=上级id, 路由=路由, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    reading_data()
    return return_data(1, '', '添加成功')


@admin.route('sys/修改一级目录/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改一级目录(id):
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/修改一级目录.html', data=data, 一级目录=一级目录, id=id)


@admin.route('sys/修改一级目录提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改一级目录提交(id):
    名称, 图标, 排序 = get_request('名称', '图标', '排序')
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称, data.图标, data.排序 = 名称, 图标, 排序
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, '', '修改成功')


@admin.route('sys/修改二级目录/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改二级目录(id):
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/修改二级目录.html', data=data, 一级目录=一级目录, 二级目录=二级目录, id=id)


@admin.route('sys/修改二级目录提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改二级目录提交(id):
    名称, 上级id, 路由, 排序 = get_request('名称', '上级id', '路由', '排序')
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称, data.上级id, data.路由, data.排序 = 名称, 上级id, 路由, 排序
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, dict(), '修改成功')


@admin.route('sys/删除目录提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 删除目录提交(id):
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    if data.上级id == 0:  # 是一级目录, 删下级
        二级data = SysCatalog.query.filter(SysCatalog.上级id == id).all()
        for i in 二级data:
            db.session.delete(i)
    db.session.delete(data)
    db.session.commit()
    reading_data()
    return return_data(1, dict(), '删除成功')


@admin.route('sys/模块')
@check_admin_login
@check_admin_developer
@check_developer
def 模块():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/模块.html', 模块=模块, 方法=方法)


@admin.route('sys/添加模块')
@check_admin_login
@check_admin_developer
@check_developer
def 添加模块():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/添加模块.html', 模块=模块)


@admin.route('sys/添加模块提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加模块提交():
    名称, 排序 = get_request('名称', '排序')
    catalog = SysModule(名称=名称, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('sys/添加方法')
@check_admin_login
@check_admin_developer
@check_developer
def 添加方法():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/添加方法.html', 模块=模块, 方法=方法)


@admin.route('sys/添加方法提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加方法提交():
    名称, 上级id, 路由, 排序 = get_request('名称', '上级id', '路由', '排序')
    catalog = SysModule(名称=名称, 上级id=上级id, 路由=路由, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('sys/修改模块/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改模块(id):
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/修改模块.html', data=data, 模块=模块, id=id)


@admin.route('sys/修改模块提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改模块提交(id):
    名称, 排序 = get_request('名称', '排序')
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称, data.排序 = 名称, 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('sys/修改方法/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改方法(id):
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/修改方法.html', data=data, 模块=模块, 方法=方法, id=id)


@admin.route('sys/修改方法提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改方法提交(id):
    名称, 上级id, 路由, 排序 = get_request('名称', '上级id', '路由', '排序')
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称, data.上级id, data.路由, data.排序 = 名称, 上级id, 路由, 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, dict(), '修改成功')


@admin.route('sys/删除模块提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 删除模块提交(id):
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    if data.上级id == 0:  # 是模块, 删下级
        方法 = SysModule.query.filter(SysModule.上级id == id).all()
        for i in 方法:
            db.session.delete(i)
    db.session.delete(data)
    db.session.commit()
    return return_data(1, dict(), '删除成功')


@admin.route('resource/表格')
@check_admin_login
@check_admin_developer
@check_developer
def 表格():
    return render_template('admin/resource/表格.html')


@admin.route('resource/表单')
@check_admin_login
@check_admin_developer
@check_developer
def 基本表单():
    return render_template('admin/resource/表单.html')


@admin.route('resource/提示框')
@check_admin_login
@check_admin_developer
@check_developer
def 提示框():
    return render_template('admin/resource/提示框.html')


@admin.route('resource/加载按钮')
@check_admin_login
@check_admin_developer
@check_developer
def 加载按钮():
    return render_template('admin/resource/加载按钮.html')


@admin.route('resource/图标')
@check_admin_login
@check_admin_developer
@check_developer
def 图标():
    return render_template('admin/resource/图标.html')


@admin.route('resource/徽章')
@check_admin_login
@check_admin_developer
@check_developer
def 徽章():
    return render_template('admin/resource/徽章.html')


@admin.route('resource/栅格')
@check_admin_login
@check_admin_developer
@check_developer
def 栅格():
    return render_template('admin/resource/栅格.html')


@admin.route('resource/css辅助')
@check_admin_login
@check_admin_developer
@check_developer
def css辅助():
    return render_template('admin/resource/css辅助.html')
