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
