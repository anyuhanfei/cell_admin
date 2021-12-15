from configs.config import ARTICLE
from run import db


class SysArticleData(db.Model):
    __tablename__ = 'sys_article_data'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, unique=True, nullable=False, default=0)
    key = db.Column(db.String(255), unique=True, nullable=False, default='')
    value = db.Column(db.Integer, unique=True, nullable=False, default=0)

    def __repe__(self):
        return "<sys_sys_article_tag:%s %s>" % (self.id, self.name)

    @classmethod
    def get_data(cls, article_id, key):
        '''获取某个数据'''
        obj = cls.query.filter(cls.key == key, cls.article_id == article_id).first()
        if obj is None:
            cls.create_all_data(article_id)
            obj = cls.query.filter(cls.key == key, cls.user_id == article_id).first()
        return obj

    @classmethod
    def get_all_data(cls, article_id):
        '''获取全部数据'''
        objs = cls.query.filter(cls.article_id == article_id).all()
        if len(objs) == 0:
            cls.create_all_data(article_id)
            objs = cls.query.filter(cls.article_id == article_id).all()
        return objs

    @classmethod
    def create_all_data(cls, article_id):
        '''创建全部数据'''
        for data in ARTICLE['ARTICLE_DATAS']:
            if cls.query.filter(cls.key == data[0], cls.article_id == article_id).first() is None:
                obj = cls(article_id=article_id, key=data, value=0)
                db.session.add(obj)
        db.session.commit()

    @classmethod
    def update_data(cls, article_id, key, num=1):
        '''修改数据value值'''
        obj = cls.get_data(article_id, key)
        if obj is None:
            return None
        obj.key += num
        db.session.add(obj)
        db.session.commit()
