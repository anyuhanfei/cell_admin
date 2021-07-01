from run import db

from configs.config import USER


class IdxUserData(db.Model):
    __tablename__ = 'idx_user_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False, default=0)
    key = db.Column(db.String(255), unique=True, nullable=False, default='')
    value = db.Column(db.String(255), unique=True, nullable=False, default='')

    def __repe__(self):
        return "<idx_user_data:%s %s>" % (self.key, self.value)

    @classmethod
    def get_data(cls, user_id, key):
        obj = cls.query.filter(cls.key == key, cls.user_id == user_id).first()
        if obj is None:
            cls.create_all_data(user_id)
            obj = cls.query.filter(cls.key == key, cls.user_id == user_id).first()
        return obj

    @classmethod
    def create_all_data(cls, user_id):
        for key in USER['USER_DATA_KEYS']:
            if cls.query.filter(cls.key == key, cls.user_id == user_id).first() is None:
                obj = cls(user_id=user_id, key=key)
                db.session.add(obj)
        db.session.commit()
