import hashlib

from run import db

from configs.config import USER
from configs.common import 随机字符串

from models.IdxUserFund import IdxUserFund
from models.IdxUserData import IdxUserData


class IdxUser(db.Model):
    __tablename__ = 'idx_user'

    user_id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255), unique=True, nullable=False, default='')
    account = db.Column(db.String(255), unique=True, nullable=False, default='')
    password = db.Column(db.String(255), unique=True, nullable=False, default='')
    password_salt = db.Column(db.String(255), unique=True, nullable=False, default='')
    level_password = db.Column(db.String(255), unique=True, nullable=False, default='')
    top_id = db.Column(db.Integer, unique=True, nullable=False, default=0)
    is_freeze = db.Column(db.Integer, unique=True, nullable=False, default=0)
    is_delete = db.Column(db.Integer, unique=True, nullable=False, default=0)

    def __repe__(self):
        return "<sys_ad:%s %s>" % (self.user_id, self.identity)

    @classmethod
    def create_data(cls, nickname, account, password, level_password, top_id):
        '''创建一个新会员'''
        obj = cls()
        obj.nickname = nickname
        obj.account = account
        obj.password_salt = 随机字符串(6)
        obj.password = cls.get_encryption_password(password, obj.password_salt)
        obj.level_password = level_password
        obj.top_id = top_id
        db.session.add(obj)
        db.session.commit()

    def comparison_password(self, password):
        '''检查输入的密码是否正确
        将输入的密码加密, 与数据库中的密码进行对比
        '''
        return self.password == self.get_encryption_password(password, self.password_salt)

    @classmethod
    def get_encryption_password(cls, password, password_salt):
        '''将输入的密码进行加密'''
        return hashlib.md5((password + password_salt).encode('utf-8')).hexdigest()

    def fund(self):
        '''获取会员余额'''
        funds = IdxUserFund.get_all_coin(self.user_id)
        if len(funds) == 0:
            IdxUserFund.create_all_data(self.user_id)
            funds = IdxUserFund.get_all_coin(self.user_id)
        data = []
        for i in funds:
            data.append([i.币种, i.金额, USER['USER_FUND_TYPE'][i.币种]])
        return data

    def get_data(self, key):
        '''获取会员数据'''
        data = IdxUserData.get_data(self.user_id, key)
        return data.value
