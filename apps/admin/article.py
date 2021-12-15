'''
文章模块
'''
import time

from flask import render_template, request, redirect, url_for

from configs.config import ARTICLE, ARTICLE_ATTRIBUTE, ARTICLE_CATEGORY, ARTICLE_TAG
from models.SysArticleData import SysArticleData

from . import admin, check_admin_login, check_admin_power, return_data, get_request, search
from run import db
from configs.common import 保存图片

from models.SysArticleTag import SysArticleTag
from models.SysArticle import SysArticle


@admin.route('/article/文章标签')
@check_admin_login
@check_admin_power
def 文章标签():
    data = SysArticleTag.query.filter(SysArticleTag.is_delete == 0).all()
    return render_template('/admin/article/文章标签.html', data=data, CATEGORY=ARTICLE_CATEGORY, TAG=ARTICLE_TAG, ATTRIBUTE=ARTICLE_ATTRIBUTE)


@admin.route('/article/添加文章标签/<string:category>')
@check_admin_login
@check_admin_power
def 添加文章标签(category):
    category_text = {'category': '分类', 'tag': '标签', 'attribute': '属性'}[category]
    return render_template('/admin/article/添加文章标签.html', category=category, category_text=category_text, CATEGORY=ARTICLE_CATEGORY, TAG=ARTICLE_TAG)


@admin.route('/article/添加文章标签提交/<string:category>', methods=["POST"])
@check_admin_login
@check_admin_power
def 添加文章标签提交(category):
    name = get_request('name')
    image = request.files.get('image')
    icon = get_request('icon')
    if category not in ['category', 'tag', 'attribute']:
        return return_data(2, '', '非法操作')
    if name == '':
        return return_data(2, '', '有信息未填写')
    if category in ['category', 'tag']:
        # 如果是分类或标签，需要判断图片是否需要上传，和图片是否上传
        image_path = ''
        if category == 'category' and ARTICLE_CATEGORY['IMAGE'] is True:
            if image is None:
                return return_data(2, '', '请上传分类图片')
            image_path = 保存图片(image, 'article')
        if category == 'tag' and ARTICLE_TAG['IMAGE'] is True:
            if image is None:
                return return_data(2, '', '请上传分类图片')
            image_path = 保存图片(image, 'article')
    else:
        # 如果是属性，则需要判断图标是否上传
        if icon == '':
            return return_data(2, '', '有信息未填写')
        image_path = icon
    obj = SysArticleTag(name=name, image=image_path, type=category)
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '添加成功', '添加文章标签/分类/属性:%s' % (name))


@admin.route('/article/修改文章标签/<int:id>')
@check_admin_login
@check_admin_power
def 修改文章标签(id):
    obj = SysArticleTag.query.filter(SysArticleTag.id == id).first()
    if obj is None or obj.is_delete == 1:
        return redirect(url_for('admin.error'))
    category_text = {'category': '分类', 'tag': '标签', 'attribute': '属性'}[obj.type]
    return render_template('/admin/article/修改文章标签.html', data=obj, id=id, category_text=category_text)


@admin.route('/article/修改文章标签提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 修改文章标签提交(id):
    name = get_request('name')
    image = request.files.get('image')
    icon = get_request('icon')
    if name == '':
        return return_data(2, '', '有信息未填写')
    obj = SysArticleTag.query.filter(SysArticleTag.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    if obj.type == 'attribute':
        obj.image = icon
    else:
        obj.image = obj.image if image is None else 保存图片(image, 'article')
    obj.name = name
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功', '修改文章标签/分类/属性:' + obj.name)


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
    return return_data(1, '', '修改成功', '删除文章标签/分类:' + obj.name)


@admin.route('/article/文章/<int:page>')
@check_admin_login
@check_admin_power
def 文章(page):
    parameters = search('文章', ['分类', '标签', '属性', '标题', '全文检索'])
    obj = SysArticle.query
    obj = obj.filter(SysArticle.category_id == parameters['分类']) if parameters['分类'] != '' else obj
    if ARTICLE_TAG['ON-OFF']:
        obj = obj.filter(SysArticle.tag_ids.like('%' + parameters['标签'] + '%')) if parameters['标签'] != '' else obj
    if ARTICLE_ATTRIBUTE['ON-OFF']:
        obj = obj.filter(SysArticle.attribute_ids.like('%' + parameters['属性'] + '%')) if parameters['属性'] != '' else obj
    obj = obj.filter(SysArticle.title.like('%' + parameters['标题'] + '%')) if parameters['标题'] != '' else obj
    obj = obj.filter(SysArticle.content.like('%' + parameters['全文检索'] + '%')) if parameters['全文检索'] != '' else obj

    models = obj.order_by(SysArticle.id.desc()).paginate(page=page, per_page=30)

    categorys = SysArticleTag.query.filter(SysArticle.is_delete == 0, SysArticleTag.type == 'category').all()
    tags = SysArticleTag.query.filter(SysArticleTag.is_delete == 0, SysArticleTag.type == 'tag').all()
    attributes = SysArticleTag.query.filter(SysArticleTag.is_delete == 0, SysArticleTag.type == 'attribute').all()
    for i in range(0, len(models.items)):
        models.items[i].datas = SysArticleData.get_all_data(models.items[i].id)
        models.items[i].tag_texts = ''
        article_tags = models.items[i].tag_ids.split(',')
        for tag in tags:
            if str(tag.id) in article_tags:
                models.items[i].tag_texts += tag.name + ' '

    return render_template('/admin/article/文章.html', models=models, parameters=parameters, TAG=ARTICLE_TAG, ATTRIBUTE=ARTICLE_ATTRIBUTE, ARTICLE=ARTICLE, categorys=categorys, tags=tags, attributes=attributes)


@admin.route('/article/添加文章')
@check_admin_login
@check_admin_power
def 添加文章():
    tags = SysArticleTag.query.filter(SysArticleTag.is_delete == 0).all()
    return render_template('/admin/article/添加文章.html', tags=tags, TAG=ARTICLE_TAG, ARTICLE=ARTICLE)


@admin.route('/article/添加文章提交', methods=["POST"])
@check_admin_login
@check_admin_power
def 添加文章提交():
    title, category_id, tag_ids, intro, keyword, author, content = get_request('title', 'category_id', 'tag_ids', 'intro', 'keyword', 'author', 'content')
    if title == '' or category_id == '' or content == '':
        return return_data(2, '', '有信息未填写')
    if ARTICLE['IMAGE'] is True:
        image = request.files.get('image')
        if image is None:
            return return_data(2, '', '请上传图片')
        image_path = 保存图片(image, 'article')
    else:
        image_path = ''
    if ARTICLE['INTRO'] is True and intro == '':
        return return_data(2, '', '有信息未填写')
    if ARTICLE['KEYWORD'] is True and keyword == '':
        return return_data(2, '', '有信息未填写')
    obj = SysArticle(title=title, category_id=category_id, tag_ids=tag_ids, intro=intro, keyword=keyword, author=author, content=content, image=image_path, insert_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '添加成功', '添加文章:' + title)


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
    return render_template('/admin/article/修改文章.html', data=obj, id=id, tags=tags, TAG=ARTICLE_TAG, ARTICLE=ARTICLE)


@admin.route('/article/修改文章提交/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 修改文章提交(id):
    title, category_id, tag_ids, intro, keyword, author, content = get_request('title', 'category_id', 'tag_ids', 'intro', 'keyword', 'author', 'content')
    obj = SysArticle.query.filter(SysArticle.id == id).first()
    if obj is None or obj.is_delete == 1:
        return return_data(2, '', '非法操作')
    if ARTICLE['IMAGE'] is True:
        image = request.files.get('image')
        obj.image = obj.image if image is None else 保存图片(image, 'article')
    obj.title, obj.category_id, obj.tag_ids, obj.intro, obj.keyword, obj.author, obj.content = title, category_id, tag_ids, intro, keyword, author, content
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功', '修改文章:' + obj.title)


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
    return return_data(1, '', '修改成功', '删除文章:' + obj.title)


@admin.route('/article/修改文章统计值/<int:id>', methods=["POST"])
@check_admin_login
@check_admin_power
def 修改文章统计值(id):
    num = get_request('num')[0]
    obj = SysArticleData.query.filter(SysArticleData.id == id).first()
    if obj is None:
        return return_data(2, '', '非法操作')
    obj.value += int(num)
    db.session.add(obj)
    db.session.commit()
    return return_data(1, '', '修改成功', '修改文章的%s%s,文章id为%s' % (obj.key, '+%s' % (num) if int(num) >= 0 else num, obj.article_id))
