import hashlib

from run import db


class SysAdmin(db.Model):
    __tablename__ = 'sys_admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('sys_role.role_id'))
    account = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    password_salt = db.Column(db.String(255), unique=True)
    nickname = db.Column(db.String(255), unique=True)
    is_delete = db.Column(db.Integer, unique=True, nullable=False, default=0)

    logs = db.relationship('LogAdmin', backref="admin")

    def __repr__(self):
        return "<sys_admin: %s %s %s %s>" % (self.admin_id, self.account, self.nickname, self.role_id)

    def comparison_password(self, password):
        '''检查输入的密码是否正确
        将输入的密码加密, 与数据库中的密码进行对比
        '''
        return self.password == self.get_encryption_password(password, self.password_salt)

    @classmethod
    def get_encryption_password(cls, password, password_salt):
        '''将输入的密码进行加密'''
        return hashlib.md5((password + password_salt).encode('utf-8')).hexdigest()
