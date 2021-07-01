from run import db


class SysAd(db.Model):
    __tablename__ = 'sys_ad'

    ad_id = db.Column(db.Integer, primary_key=True)
    广告位 = db.Column(db.Integer, nullable=False, default=0)
    标题 = db.Column(db.String(255), unique=True, nullable=False, default='')
    图片 = db.Column(db.String(255), unique=True, nullable=False, default='')
    值 = db.Column(db.String(255), unique=True, nullable=False, default='')
    富文本 = db.Column(db.String(255), unique=True, nullable=False, default='')

    def __repe__(self):
        return "<sys_ad:%s %s>" % (self.ad_id, self.标题)
