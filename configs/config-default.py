APP_DEBUG = True

'''系统设置'''
# 开发者模式，True为开启，False为关闭
DEVELOPER = True
# 管理员权限，True为开启，False为关闭
ADMIN_POWER = False

'''数据库'''
DATABASE = {
    'TYPE': 'mysql',
    'HOSTNAME': '127.0.0.1',
    'DATABASE': 'cell_admin',
    'USERNAME': 'root',
    'PASSWORD': 'root',
    'HOSTPORT': '3306'
}

'''Redis'''
REDIS = {
    'HOST': '127.0.0.1',
    'PORT': 6379,
    'PASSWORD': ''
}

# 注：以下设置内容需要在项目设计时决定配置，开发阶段与生产阶段不宜修改
'''会员模块'''
USER = {
    # 会员标识说明(account字段的说明)
    'USER_IDENTITY_TEXT': '账号',
    # 会员资金类型
    'USER_FUND_TYPE': [
        '余额', '积分'
    ],
    # 会员信息类型
    'USER_DATAS': [
        ['标签', ''],
    ],
    # 二级密码, 使用为True，不使用为False
    'USER_LEVEL_PASSWORD': False,
    # 推荐关系，使用为True，不使用为False
    'USER_TOP_USER': False,
    # 会员删除按钮
    'USER_DELETE': True,  # 会员删除按钮是否使用
}

'''文章模块'''
ARTICLE_TAG = {
    # 文章标签是否使用
    'ON-OFF': False,
    # 文章标签的图片
    'IMAGE': False,
}
ARTICLE_CATEGORY = {
    # 文章分类的图片
    'IMAGE': False,
}
ARTICLE_ATTRIBUTE = {
    # 文章属性是否使用
    'ON-OFF': True
}
ARTICLE = {
    'KEYWORD': False,
    'INTRO': False,
    'IMAGE': False,
    'ARTICLE_DATAS': [
        '浏览量', '点赞数'
    ],
}
