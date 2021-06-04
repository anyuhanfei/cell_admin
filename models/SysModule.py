from run import db


class SysModule(db.Model):
    __tablename__ = 'sys_module'

    module_id = db.Column(db.Integer, primary_key=True)
    名称 = db.Column(db.String(255))
    排序 = db.Column(db.Integer, nullable=False, default=99)
    上级id = db.Column(db.Integer, nullable=False, default=0)
    路由 = db.Column(db.String(255), unique=True, nullable=False, default='')

    def __repe__(self):
        return "<sys_catalog:%s %s>" % (self.module_id, self.名称)

    def json(self):
        return {
            'module_id': self.module_id,
            '名称': self.名称,
            '排序': self.排序,
            '上级id': self.上级id,
            '路由': self.路由,
        }
