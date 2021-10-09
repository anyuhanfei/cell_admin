import datetime

from run import db


class LogUserFund(db.Model):
    __tablename__ = 'log_user_fund'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('idx_user.user_id'))
    币种 = db.Column(db.String(255), unique=True, nullable=False, default='')
    金额 = db.Column(db.String(255), unique=True, nullable=False, default='')
    说明 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备注 = db.Column(db.String(255), unique=True, nullable=False, default='')
    流水时间 = db.Column(db.DateTime, default=datetime.datetime.now)

    @classmethod
    def create_data(cls, user_id, 币种, 金额, 说明, 备注=''):
        obj = cls()
        obj.user_id = user_id
        obj.币种 = 币种
        obj.金额 = 金额
        obj.说明 = 说明
        obj.备注 = 备注
        return obj
