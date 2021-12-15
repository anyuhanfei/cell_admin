from run import db


class SysArticleTag(db.Model):
    __tablename__ = 'sys_article_tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False, default='')
    image = db.Column(db.String(255), unique=True, nullable=False, default='')
    type = db.Column(db.String(255), unique=True, nullable=False, default='category')
    is_delete = db.Column(db.Integer, unique=True, nullable=False, default=0)

    articles = db.relationship('SysArticle', backref='category')

    def __repe__(self):
        return "<sys_sys_article_tag:%s %s>" % (self.id, self.name)
