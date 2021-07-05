'''
广告模块, 参数设置模块
'''

from flask import render_template, request, redirect, url_for

from . import admin, check_admin_login, check_developer, check_admin_power, check_admin_developer
from run import db
from configs.common import return_data, 保存图片, 删除图片

from models.SysAd import SysAd
from models.SysSetting import SysSetting


@admin.route('set/广告')
@check_admin_login
@check_admin_power
def 广告():
    广告位 = SysAd.query.filter(SysAd.广告位 == 0).all()
    广告 = SysAd.query.filter(SysAd.广告位 != 0).all()
    return render_template('/admin/set/广告.html', 广告位=广告位, 广告=广告)


@admin.route('set/添加广告位')
@check_admin_login
@check_admin_developer
@check_developer
def 添加广告位():
    return render_template('/admin/set/添加广告位.html')


@admin.route('set/添加广告位提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加广告位提交():
    标题 = request.form.get('标题')
    if 标题 == '':
        return return_data(2, '', '请填写广告位标题')
    广告位 = SysAd(标题=标题)
    db.session.add(广告位)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('set/添加广告')
@check_admin_login
@check_admin_developer
@check_developer
def 添加广告():
    广告位 = SysAd.query.filter(SysAd.广告位 == 0).all()
    return render_template('/admin/set/添加广告.html', 广告位=广告位)


@admin.route('set/添加广告提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加广告提交():
    标题 = request.form.get('标题')
    广告位 = request.form.get('广告位')
    图片 = request.files.get('图片')
    值 = request.form.get('值')
    富文本 = request.form.get('富文本')
    if 标题 == '' or 标题 is None or 广告位 == 0 or 广告位 is None:
        return return_data(2, '', '有必填项未填写')
    if 值 != '' and 值 is not None:
        富文本, image_path = '', ''
    elif 图片 is not None:
        值, 富文本, image_path = '', '', 保存图片(图片, 'ad')
    elif 富文本 != '' and 富文本 is not None:
        值, image_path = '', ''
    else:
        return return_data(2, '', '选填三项中必须填写一项')

    广告 = SysAd(标题=标题, 广告位=广告位, 值=值, 图片=image_path, 富文本=富文本)
    db.session.add(广告)
    db.session.commit()

    return return_data(1, '', '添加成功')


@admin.route('set/修改广告位/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改广告位(id):
    data = SysAd.query.filter(SysAd.ad_id == id).first()
    if data is None or data.广告位 != 0:
        return redirect(url_for('admin.error'))
    return render_template('/admin/set/修改广告位.html', data=data, id=id)


@admin.route('set/修改广告位提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改广告位提交(id):
    标题 = request.form.get('标题')
    if 标题 == '' or 标题 is None:
        return return_data(2, '', '有必填项未填写')
    data = SysAd.query.filter(SysAd.ad_id == id).first()
    data.标题 = 标题
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('set/修改广告/<int:id>')
@check_admin_login
@check_admin_power
def 修改广告(id):
    data = SysAd.query.filter(SysAd.ad_id == id).first()
    if data is None or data.广告位 == 0:
        return redirect(url_for('admin.error'))
    value_type = '值' if data.值 else ('图片' if data.图片 else '富文本')
    广告位 = SysAd.query.filter(SysAd.广告位 == 0).all()
    return render_template('/admin/set/修改广告.html', data=data, id=id, value_type=value_type, 广告位=广告位)


@admin.route('set/修改广告提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_power
def 修改广告提交(id):
    标题 = request.form.get('标题')
    广告位 = request.form.get('广告位')
    value_type = request.form.get('value_type')
    if 标题 == '' or 标题 is None or 广告位 == 0 or 广告位 is None:
        return return_data(2, '', '有必填项未填写')
    if value_type not in ['图片', '值', '富文本']:
        return return_data(2, '', '非法操作')
    data = SysAd.query.filter(SysAd.ad_id == id).first()
    if data is None:
        return return_data(2, '', '不存在的广告位')
    data.标题 = 标题
    data.广告位 = 广告位
    if value_type == '图片':
        图片 = request.files.get('图片')
        if 图片 is not None:
            data.图片 = 保存图片(图片, 'ad')
    elif value_type == '值':
        值 = request.form.get('值')
        if 值 == '' or 值 is None:
            return return_data(2, '', '请填写值')
        data.值 = request.form.get('值')
    else:
        富文本 = request.form.get('富文本')
        if 富文本 == '' or 富文本 is None:
            return return_data(2, '', '请填写富文本')
        data.富文本 = request.form.get('富文本')
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('set/删除广告提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 删除广告提交(id):
    data = SysAd.query.filter(SysAd.ad_id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    image_path = data.图片 if data.图片 != '' else ''
    db.session.delete(data)
    db.session.commit()
    删除图片(image_path)
    return return_data(1, '', '删除成功')


@admin.route('set/参数')
@check_admin_login
@check_admin_power
def 参数():
    分组 = SysSetting.query.filter(SysSetting.上级id == 0).all()
    参数 = SysSetting.query.filter(SysSetting.上级id != 0).all()
    return render_template('/admin/set/参数.html', 分组=分组, 参数=参数)


@admin.route('set/添加参数分组')
@check_admin_login
@check_admin_developer
@check_developer
def 添加参数分组():
    分组 = SysSetting.query.filter(SysSetting.上级id == 0).order_by(SysSetting.排序.asc()).all()
    return render_template('/admin/set/添加参数分组.html', 分组=分组)


@admin.route('set/添加参数分组提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加参数分组提交():
    标题 = request.form.get('标题')
    排序 = request.form.get('排序')

    data = SysSetting(标题=标题, 排序=排序)
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('set/添加参数')
@check_admin_login
@check_admin_developer
@check_developer
def 添加参数():
    分组 = SysSetting.query.filter(SysSetting.上级id == 0).order_by(SysSetting.排序.asc()).all()
    参数 = SysSetting.query.filter(SysSetting.上级id != 0).order_by(SysSetting.排序.asc()).all()
    return render_template('admin/set/添加参数.html', 分组=分组, 参数=参数)


@admin.route('set/添加参数提交', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 添加参数提交():
    标题 = request.form.get('标题')
    上级id = request.form.get('上级id')
    类型 = request.form.get('类型')
    备注 = request.form.get('备注')
    排序 = request.form.get('排序')
    if 上级id == 0 or 上级id is None:
        return return_data(2, '', '请选择分组')

    data = SysSetting(标题=标题, 上级id=上级id, 类型=类型, 排序=排序, 备注=备注)
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('set/修改参数分组/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改参数分组(id):
    data = SysSetting.query.filter(SysSetting.id == id).first()
    if data is None or data.上级id != 0:
        return redirect(url_for('admin.error'))
    分组 = SysSetting.query.filter(SysSetting.上级id == 0).order_by(SysSetting.排序.asc()).all()
    return render_template('admin/set/修改参数分组.html', 分组=分组, data=data, id=id)


@admin.route('set/修改参数分组提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改参数分组提交(id):
    标题 = request.form.get('标题')
    排序 = request.form.get('排序')

    data = SysSetting.query.filter(SysSetting.id == id).first()
    if data is None or data.上级id != 0:
        return return_data(2, '', '非法操作')
    data.标题 = 标题
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('set/修改参数/<int:id>')
@check_admin_login
@check_admin_developer
@check_developer
def 修改参数(id):
    data = SysSetting.query.filter(SysSetting.id == id).first()
    if data is None or data.上级id == 0:
        return redirect(url_for('admin.error'))
    分组 = SysSetting.query.filter(SysSetting.上级id == 0).order_by(SysSetting.排序.asc()).all()
    参数 = SysSetting.query.filter(SysSetting.上级id != 0).order_by(SysSetting.排序.asc()).all()
    return render_template('admin/set/修改参数.html', 分组=分组, data=data, 参数=参数, id=id)


@admin.route('set/修改参数提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 修改参数提交(id):
    标题 = request.form.get('标题')
    上级id = request.form.get('上级id')
    类型 = request.form.get('类型')
    备注 = request.form.get('备注')
    排序 = request.form.get('排序')

    data = SysSetting.query.filter(SysSetting.id == id).first()
    if data is None or data.上级id == 0:
        return return_data(2, '', '非法操作')
    data.标题 = 标题
    data.上级id = 上级id
    data.类型 = 类型
    data.备注 = 备注
    data.排序 = 排序
    db.session.add(data)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('set/参数值提交', methods=['POST'])
@check_admin_login
@check_admin_power
def 参数值提交():
    data = request.form
    for key, value in data.items():
        data = SysSetting.query.filter(SysSetting.id == key).first()
        if data:
            data.值 = value
            db.session.add(data)
            db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('set/删除参数提交/<int:id>', methods=['POST'])
@check_admin_login
@check_admin_developer
@check_developer
def 删除参数提交(id):
    data = SysSetting.query.filter(SysSetting.id == id).first()
    if data is None:
        return return_data(2, '', '非法操作')
    db.session.delete(data)
    db.session.commit()
    return return_data(1, '', '删除成功')
