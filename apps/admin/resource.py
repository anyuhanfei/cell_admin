from flask import render_template

from . import admin, check_admin_login


@admin.route('resource/表格')
@check_admin_login
def 表格():
    return render_template('admin/resource/表格.html')


@admin.route('resource/表单')
@check_admin_login
def 基本表单():
    return render_template('admin/resource/表单.html')


@admin.route('resource/提示框')
@check_admin_login
def 提示框():
    return render_template('admin/resource/提示框.html')


@admin.route('resource/加载按钮')
@check_admin_login
def 加载按钮():
    return render_template('admin/resource/加载按钮.html')


@admin.route('resource/图标')
@check_admin_login
def 图标():
    return render_template('admin/resource/图标.html')


@admin.route('resource/标签')
@check_admin_login
def 标签():
    return render_template('admin/resource/标签.html')


@admin.route('resource/徽章')
@check_admin_login
def 徽章():
    return render_template('admin/resource/徽章.html')


@admin.route('resource/栅格')
@check_admin_login
def 栅格():
    return render_template('admin/resource/栅格.html')


@admin.route('resource/css辅助')
@check_admin_login
def css辅助():
    return render_template('admin/resource/css辅助.html')
