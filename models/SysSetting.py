from run import db


class SysSetting(db.Model):
    __tablename__ = 'sys_setting'

    id = db.Column(db.Integer, primary_key=True)
    上级id = db.Column(db.Integer, nullable=False, default=0)
    标题 = db.Column(db.String(255), unique=True, nullable=False, default='')
    类型 = db.Column(db.String(255), unique=True, nullable=False, default='')
    值 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备注 = db.Column(db.String(255), unique=True, nullable=False, default='')
    排序 = db.Column(db.Integer, nullable=False, default=99)

    def __repe__(self):
        return "<sys_ad:%s %s>" % (self.id, self.标题)
