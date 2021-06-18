def return_data(code, data, msg):
    '''整合数据, 并进行返回
    Args:
        code: 状态码, 1 成功, 2 失败
        data: 数据
        msg: 说明
    Return:
        字典
    '''
    return {'code': code, 'data': data, 'msg': msg}


# def 保存图片(image_obj, 子目录):
#     '''将传入的图片保存到服务器本地
#     '''
#     import os, sys, random, string

#     # 生成随机字符串，防止图片名字重复
#     ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))

#     # 定义一个图片存放的位置 存放在static下面
#     path = "uploads/%s/" % (子目录)
#     #图片名称 给图片重命名 为了图片名称的唯一性
#     imgName = ran_str+img.filename
#     #图片path和名称组成图片的保存路径
#     file_path = path+imgName
#     #保存图片
#     img.save(file_path)
#     #这个是图片的访问路径，需返回前端（可有可无）
#     url = '/static/img/'+imgName
#     #返回图片路径 到前端
#     return url


def 随机字符串(num, pattern='数字'):
    pattern_list = ['数字', '小写字母', '大写字母', '数字+小写字母', '数字+大写字母', '小写字母+大写字母', '数字+小写字母+大写字母']
    if pattern not in pattern_list:
        pattern = '数字'

    import string
    import random

    if pattern == '小写字母':
        s = string.ascii_lowercase
    elif pattern == '大写字母':
        s = string.ascii_uppercase
    elif pattern == '数字+小写字母':
        s = string.digits + string.ascii_lowercase
    elif pattern == '数字+大写字母':
        s = string.digits + string.ascii_uppercase
    elif pattern == '小写字母+大写字母':
        s = string.ascii_uppercase + string.ascii_lowercase
    elif pattern == '数字+小写字母+大写字母':
        s = string.digits + string.ascii_uppercase + string.ascii_lowercase
    else:
        s = string.digits
    res_str = ''
    for i in range(0, num):
        res_str += random.choice(s)
    return res_str
