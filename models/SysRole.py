from run import db


class SysRole(db.Model):
    __tablename__ = 'sys_role'

    role_id = db.Column(db.Integer, primary_key=True)
    角色名 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备注 = db.Column(db.String(255), nullable=False, default='')
    权限 = db.Column(db.String(255), nullable=False, default='')

    admins = db.relationship('SysAdmin', backref='role')

    def __repe__(self):
        return "<sys_role:%s %s>" % (self.role_id, self.角色名)
