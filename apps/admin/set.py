from flask import render_template

from . import admin, check_admin_login

from models.SysAd import SysAd


@admin.route('set/广告')
@check_admin_login
def 广告():
    广告位 = SysAd.query.filter(SysAd.adv_id == 0).all()
    广告 = SysAd.query.filter(SysAd.adv_id != 0).all()
    return render_template('/admin/set/广告.html', 广告位=广告位, 广告=广告)


@admin.route('set/添加广告/<string:pattern>')
@check_admin_login
def 添加广告(pattern):
    广告位 = SysAd.query.filter(SysAd.adv_id == 0).all()
    return render_template('/admin/set/添加广告.html', 广告位=广告位, pattern=pattern)


@admin.route('set/添加广告提交')
@check_admin_login
def 添加广告提交():
    pass


@admin.route('set/修改广告')
@check_admin_login
def 修改广告():
    pass


@admin.route('set/修改广告提交')
@check_admin_login
def 修改广告提交():
    pass


@admin.route('set/删除广告提交')
@check_admin_login
def 删除广告提交():
    pass
