from flask import render_template, request

from . import admin, check_admin_login
from run import db
from configs.common import return_data

from models.SysAd import SysAd


@admin.route('set/广告')
@check_admin_login
def 广告():
    广告位 = SysAd.query.filter(SysAd.adv_id == 0).all()
    广告 = SysAd.query.filter(SysAd.adv_id != 0).all()
    return render_template('/admin/set/广告.html', 广告位=广告位, 广告=广告)


@admin.route('set/添加广告位')
@check_admin_login
def 添加广告位():
    return render_template('/admin/set/添加广告位.html')


@admin.route('set/添加广告位提交', methods=['POST'])
@check_admin_login
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
def 添加广告():
    广告位 = SysAd.query.filter(SysAd.adv_id == 0).all()
    return render_template('/admin/set/添加广告.html', 广告位=广告位)


@admin.route('set/添加广告提交', methods=['POST'])
@check_admin_login
def 添加广告提交():
    标题 = request.form.get('标题')
    adv_id = request.form.get('adv_id')
    图片 = request.files.get('图片')
    值 = request.form.get('值')
    富文本 = request.form.get('富文本')
    print(图片)



@admin.route('set/修改广告')
@check_admin_login
def 修改广告():
    pass


@admin.route('set/修改广告提交', methods=['POST'])
@check_admin_login
def 修改广告提交():
    pass


@admin.route('set/删除广告提交', methods=['POST'])
@check_admin_login
def 删除广告提交():
    pass
