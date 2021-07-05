'''
文章模块
'''
import time

from flask import render_template, request, redirect, url_for

from . import admin, check_admin_login, check_admin_power
from run import db
from configs.common import return_data, 保存图片

from models.SysArticleTag import SysArticleTag
from models.SysArticle import SysArticle


@admin.route('/article/文章标签')
@check_admin_login
@check_admin_power
def 文章标签():
    data = SysArticleTag.query.filter(SysArticleTag.is_delete == 0).all()
    return render_template('/admin/article/文章标签.html', data=data)


@admin.route('/article/添加文章标签/<string:category>')
@check_admin_login
@check_admin_power
def 添加文章标签(category):
    category_text = '分类' if category == 'category' else '标签'
    return render_template('/admin/article/添加文章标签.html', category=category, category_text=category_text)


@admin.route('/article/添加文章标签提交/<string:category>', methods=["POST"])
@check_admin_login
@check_admin_power
def 添加文章标签提交(category):
    name = request.form.get('name')
    image = request.files.get('image')
    if category != 'category' and category != 'tag':
        return return_data(2, '', '非法操作')
    if name == '' or name is None or image is None:
        return return_data(2, '', '有信息未填写/上传')
    image_path = 保存图片(image, 'article')
    obj = SysArticleTag(name=name, image=image_path, type=category)
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('/article/修改文章标签/<int:id>')
@check_admin_login
@check_admin_power
def 修改文章标签(id):
    obj = SysArticleTag.query.filter(SysArticleTag.id == id).first()
    if obj is None or obj.is_delete == 1:
        return redirect(url_for('admin.error'))
    category_text = '分类' if obj.type == 'category' else '标签'
    return render_template('/admin/article/修改文章标签.html', data=obj, id=id, category_text=category_text)


@admin.route('/article/修改文章标签提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 修改文章标签提交(id):
    name = request.form.get('name')
    image = request.files.get('image')
    if name == '' or name is None:
        return return_data(2, '', '有信息未填写')
    obj = SysArticleTag.query.filter(SysArticleTag.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    obj.image = obj.image if image is None else 保存图片(image, 'article')
    obj.name = name
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('/article/删除文章标签提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 删除文章标签提交(id):
    obj = SysArticleTag.query.filter(SysArticleTag.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    obj.is_delete = 1
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('/article/文章')
@check_admin_login
@check_admin_power
def 文章():
    data = SysArticle.query.filter(SysArticle.is_delete == 0).all()
    tags = SysArticleTag.query.filter(SysArticleTag.is_delete == 0, SysArticleTag.type == 'tag').all()
    for i in range(0, len(data)):
        data[i].tag_texts = ''
        article_tags = data[i].tag_ids.split(',')
        for tag in tags:
            if str(tag.id) in article_tags:
                data[i].tag_texts += tag.name + ' '

    return render_template('/admin/article/文章.html', data=data)


@admin.route('/article/添加文章')
@check_admin_login
@check_admin_power
def 添加文章():
    tags = SysArticleTag.query.filter(SysArticleTag.is_delete == 0).all()
    return render_template('/admin/article/添加文章.html', tags=tags)


@admin.route('/article/添加文章提交', methods=["POST"])
@check_admin_login
@check_admin_power
def 添加文章提交():
    title = request.form.get('title')
    category_id = request.form.get('category_id')
    tag_ids = request.form.get('tag_ids')
    intro = request.form.get('intro')
    keyword = request.form.get('keyword')
    author = request.form.get('author')
    content = request.form.get('content')
    image = request.files.get('image')
    image_path = 保存图片(image, 'article')
    obj = SysArticle(title=title, category_id=category_id, tag_ids=tag_ids, intro=intro, keyword=keyword, author=author, content=content, image=image_path, insert_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '添加成功')


@admin.route('/article/修改文章/<int:id>')
@check_admin_login
@check_admin_power
def 修改文章(id):
    obj = SysArticle.query.filter(SysArticle.id == id).first()
    if obj is None or obj.is_delete == 1:
        return redirect(url_for('admin.error'))
    tag_ids = obj.tag_ids.split(',')
    tags = SysArticleTag.query.filter(SysArticleTag.is_delete == 0).all()
    for i in range(0, len(tags)):
        if str(tags[i].id) in tag_ids:
            tags[i].是否选中 = True
        else:
            tags[i].是否选中 = False
    return render_template('/admin/article/修改文章.html', data=obj, id=id, tags=tags)


@admin.route('/article/修改文章提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 修改文章提交(id):
    title = request.form.get('title')
    category_id = request.form.get('category_id')
    tag_ids = request.form.get('tag_ids')
    intro = request.form.get('intro')
    keyword = request.form.get('keyword')
    author = request.form.get('author')
    content = request.form.get('content')
    image = request.files.get('image')
    obj = SysArticle.query.filter(SysArticle.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    obj.image = obj.image if image is None else 保存图片(image, 'article')
    obj.title = title
    obj.category_id = category_id
    obj.tag_ids = tag_ids
    obj.intro = intro
    obj.keyword = keyword
    obj.author = author
    obj.content = content
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功')


@admin.route('/article/删除文章提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 删除文章提交(id):
    obj = SysArticle.query.filter(SysArticle.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    obj.is_delete = 1
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功')
