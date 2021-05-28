import hashlib

from run import db


class SysAdmin(db.Model):
    __tablename__ = 'sys_admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    password_salt = db.Column(db.String(255), unique=True)
    nickname = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<sys_admin: %s %s %s %s>" % (self.admin_id, self.account, self.nickname, self.role_id)

    def comparison_password(self, password):
        return self.password == hashlib.md5((password + self.password_salt).encode('utf-8')).hexdigest()
