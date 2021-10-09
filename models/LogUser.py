import datetime

from run import db


class LogUser(db.Model):
    __tablename__ = 'log_user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('idx_user.user_id'))
    说明 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备用1 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备用2 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备用3 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备用4 = db.Column(db.String(255), unique=True, nullable=False, default='')
    备用5 = db.Column(db.String(255), unique=True, nullable=False, default='')
    操作时间 = db.Column(db.DateTime, default=datetime.datetime.now)

    @classmethod
    def create_data(cls, user_id, 说明, *args):
        obj = cls()
        obj.user_id = user_id
        obj.说明 = 说明
        obj.备用1 = args[0] if len(args) >= 1 else ''
        obj.备用2 = args[1] if len(args) >= 2 else ''
        obj.备用3 = args[2] if len(args) >= 3 else ''
        obj.备用4 = args[3] if len(args) >= 4 else ''
        obj.备用5 = args[4] if len(args) >= 5 else ''
        db.session.add(obj)
        db.session.commit()
        return True
