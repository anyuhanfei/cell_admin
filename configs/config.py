APP_DEBUG = True

# Database
DATABASE = {
    'TYPE': 'mysql',
    'HOSTNAME': '127.0.0.1',
    'DATABASE': 'cell_admin',
    'USERNAME': 'root',
    'PASSWORD': 'root',
    'HOSTPORT': '3306'
}

# User
USER = {
    'USER_IDENTITY_TEXT': '手机号',  # 会员标识说明
    'USER_FUND_TYPE': {  # 账户币种, key(币种名): value(币种名中文说明)
        'money': '余额',
        'integral': '积分',
        'gold': '金币',
        'usdt': 'USDT'
    },
    'VIO_ENABLE': True,
    'USER_DATA_KEYS': [
        'vio', '标签', 'phone', 'email'
    ],
}
