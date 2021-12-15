import datetime

from run import db


class SysArticle(db.Model):
    __tablename__ = 'sys_article'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('sys_article_tag.id'))
    tag_ids = db.Column(db.String(255), unique=True, nullable=False, default='')
    attribute_ids = db.Column(db.String(255), unique=True, nullable=False, default='')
    title = db.Column(db.String(255), unique=True, nullable=False, default='')
    author = db.Column(db.String(255), unique=True, nullable=False, default='')
    intro = db.Column(db.String(255), unique=True, nullable=False, default='')
    keyword = db.Column(db.String(255), unique=True, nullable=False, default='')
    image = db.Column(db.String(255), unique=True, nullable=False, default='')
    content = db.Column(db.String(255), unique=True, nullable=False, default='')
    insert_time = db.Column(db.DateTime, default=datetime.datetime.now)
    is_delete = db.Column(db.Integer, unique=True, nullable=False, default=0)

    def __repe__(self):
        return "<sys_sys_article_tag:%s %s>" % (self.id, self.name)
