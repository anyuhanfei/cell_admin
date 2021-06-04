from flask import render_template

from . import admin


@admin.route('resource/表格')
def 表格():
    return render_template('admin/resource/表格.html')


@admin.route('resource/基本表单')
def 基本表单():
    return render_template('admin/resource/基本表单.html')


@admin.route('resource/高级表单')
def 高级表单():
    return render_template('admin/resource/高级表单.html')


@admin.route('resource/表单向导')
def 表单向导():
    return render_template('admin/resource/表单向导.html')


@admin.route('resource/文件上传')
def 文件上传():
    return render_template('admin/resource/文件上传.html')


@admin.route('resource/编辑器')
def 编辑器():
    return render_template('admin/resource/编辑器.html')


@admin.route('resource/活动流')
def 活动流():
    return render_template('admin/resource/活动流.html')


@admin.route('resource/博客列表')
def 博客列表():
    return render_template('admin/resource/博客列表.html')


@admin.route('resource/博客列表2')
def 博客列表2():
    return render_template('admin/resource/博客列表2.html')


@admin.route('resource/博客详情')
def 博客详情():
    return render_template('admin/resource/博客详情.html')


@admin.route('resource/提示框')
def 提示框():
    return render_template('admin/resource/提示框.html')


@admin.route('resource/提示框2')
def 提示框2():
    return render_template('admin/resource/提示框2.html')


@admin.route('resource/加载按钮')
def 加载按钮():
    return render_template('admin/resource/加载按钮.html')


@admin.route('resource/聊天室')
def 聊天室():
    return render_template('admin/resource/聊天室.html')


@admin.route('resource/排版')
def 排版():
    return render_template('admin/resource/排版.html')


@admin.route('resource/图标')
def 图标():
    return render_template('admin/resource/图标.html')


@admin.route('resource/标签')
def 标签():
    return render_template('admin/resource/标签.html')


@admin.route('resource/面板')
def 面板():
    return render_template('admin/resource/面板.html')


@admin.route('resource/徽章')
def 徽章():
    return render_template('admin/resource/徽章.html')


@admin.route('resource/栅格')
def 栅格():
    return render_template('admin/resource/栅格.html')


@admin.route('resource/css辅助')
def css辅助():
    return render_template('admin/resource/css辅助.html')
