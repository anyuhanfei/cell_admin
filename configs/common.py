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
