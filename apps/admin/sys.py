from flask import render_template, request, redirect, url_for

from . import admin, check_admin_login, reading_data
from run import db
from configs.common import return_data

from models.SysCatalog import SysCatalog
from models.SysModule import SysModule


@admin.route('sys/目录')
@check_admin_login
def 目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/目录.html', 一级目录=一级目录, 二级目录=二级目录)


@admin.route('sys/添加一级目录')
@check_admin_login
def 添加一级目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/添加一级目录.html', 一级目录=一级目录)


@admin.route('sys/添加一级目录提交', methods=['POST'])
@check_admin_login
def 添加一级目录提交():
    名称 = request.form.get('名称')
    图标 = request.form.get('图标')
    排序 = request.form.get('排序')

    catalog = SysCatalog(名称=名称, 图标=图标, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    reading_data()
    return return_data(1, '', '添加成功')


@admin.route('sys/添加二级目录')
@check_admin_login
def 添加二级目录():
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/添加二级目录.html', 一级目录=一级目录, 二级目录=二级目录)


@admin.route('sys/添加二级目录提交', methods=['POST'])
@check_admin_login
def 添加二级目录提交():
    名称 = request.form.get('名称')
    上级id = request.form.get('上级id')
    路由 = request.form.get('路由')
    排序 = request.form.get('排序')

    catalog = SysCatalog(名称=名称, 上级id=上级id, 路由=路由, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    reading_data()
    return return_data(1, '', '添加成功')


@admin.route('sys/修改一级目录/<int:id>')
@check_admin_login
def 修改一级目录(id):
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/修改一级目录.html', data=data, 一级目录=一级目录, id=id)


@admin.route('sys/修改一级目录提交/<int:id>', methods=['POST'])
@check_admin_login
def 修改一级目录提交(id):
    名称 = request.form.get('名称')
    图标 = request.form.get('图标')
    排序 = request.form.get('排序')

    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称 = 名称
    data.图标 = 图标
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, '', '修改成功')


@admin.route('sys/修改二级目录/<int:id>')
@check_admin_login
def 修改二级目录(id):
    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    一级目录 = SysCatalog.query.filter(SysCatalog.上级id == 0).order_by(SysCatalog.排序.asc()).all()
    二级目录 = SysCatalog.query.filter(SysCatalog.上级id != 0).order_by(SysCatalog.排序.asc()).all()
    return render_template('admin/sys/修改二级目录.html', data=data, 一级目录=一级目录, 二级目录=二级目录, id=id)


@admin.route('sys/修改二级目录提交/<int:id>', methods=['POST'])
@check_admin_login
def 修改二级目录提交(id):
    名称 = request.form.get('名称')
    上级id = request.form.get('上级id')
    路由 = request.form.get('路由')
    排序 = request.form.get('排序')

    data = SysCatalog.query.filter(SysCatalog.catalog_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称 = 名称
    data.上级id = 上级id
    data.路由 = 路由
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    reading_data()
    return return_data(1, dict(), '修改成功')


@admin.route('sys/删除目录提交/<int:id>', methods=['POST'])
@check_admin_login
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
def 模块():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/模块.html', 模块=模块, 方法=方法)


@admin.route('sys/添加模块')
@check_admin_login
def 添加模块():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/添加模块.html', 模块=模块)


@admin.route('sys/添加模块提交', methods=['POST'])
@check_admin_login
def 添加模块提交():
    名称 = request.form.get('名称')
    排序 = request.form.get('排序')

    catalog = SysModule(名称=名称, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('sys/添加方法')
@check_admin_login
def 添加方法():
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/添加方法.html', 模块=模块, 方法=方法)


@admin.route('sys/添加方法提交', methods=['POST'])
@check_admin_login
def 添加方法提交():
    名称 = request.form.get('名称')
    上级id = request.form.get('上级id')
    路由 = request.form.get('路由')
    排序 = request.form.get('排序')

    catalog = SysModule(名称=名称, 上级id=上级id, 路由=路由, 排序=排序)
    db.session.add(catalog)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('sys/修改模块/<int:id>')
@check_admin_login
def 修改模块(id):
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/修改模块.html', data=data, 模块=模块, id=id)


@admin.route('sys/修改模块提交/<int:id>', methods=['POST'])
@check_admin_login
def 修改模块提交(id):
    名称 = request.form.get('名称')
    排序 = request.form.get('排序')

    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称 = 名称
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('sys/修改方法/<int:id>')
@check_admin_login
def 修改方法(id):
    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    模块 = SysModule.query.filter(SysModule.上级id == 0).order_by(SysModule.排序.asc()).all()
    方法 = SysModule.query.filter(SysModule.上级id != 0).order_by(SysModule.排序.asc()).all()
    return render_template('admin/sys/修改方法.html', data=data, 模块=模块, 方法=方法, id=id)


@admin.route('sys/修改方法提交/<int:id>', methods=['POST'])
@check_admin_login
def 修改方法提交(id):
    名称 = request.form.get('名称')
    上级id = request.form.get('上级id')
    路由 = request.form.get('路由')
    排序 = request.form.get('排序')

    data = SysModule.query.filter(SysModule.module_id == id).first()
    if data is None:
        return redirect(url_for('admin.error'))
    data.名称 = 名称
    data.上级id = 上级id
    data.路由 = 路由
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, dict(), '修改成功')


@admin.route('sys/删除模块提交/<int:id>', methods=['POST'])
@check_admin_login
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
