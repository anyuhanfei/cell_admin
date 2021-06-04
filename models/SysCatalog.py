from run import db


class SysCatalog(db.Model):
    __tablename__ = 'sys_catalog'

    catalog_id = db.Column(db.Integer, primary_key=True)
    名称 = db.Column(db.String(255))
    图标 = db.Column(db.String(255), nullable=False, default='')
    排序 = db.Column(db.Integer, nullable=False, default=99)
    上级id = db.Column(db.Integer, nullable=False, default=0)
    路由 = db.Column(db.String(255), unique=True, nullable=False, default='')

    def __repe__(self):
        return "<sys_catalog:%s %s>" % (self.catalog_id, self.名称)

    def json(self):
        return {
            'catalog_id': self.catalog_id,
            '名称': self.名称,
            '图标': self.图标,
            '排序': self.排序,
            '上级id': self.上级id,
            '路由': self.路由,
        }
