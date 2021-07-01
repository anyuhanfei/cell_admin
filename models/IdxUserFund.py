from run import db

from configs.config import USER


class IdxUserFund(db.Model):
    __tablename__ = 'idx_user_fund'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False, default=0)
    币种 = db.Column(db.String(255), unique=True, nullable=False, default='')
    金额 = db.Column(db.Float, unique=True, nullable=False, default='0.00')

    def __repe__(self):
        return "<idx_user_fund:%s %s>" % (self.币种, self.金额)

    @classmethod
    def create_data(cls, user_id, 币种):
        '''创建一种币种的数据'''
        data = cls(user_id=user_id, 币种=币种)
        db.session.add(data)
        db.session.commit()

    @classmethod
    def create_all_data(cls, user_id):
        '''创建全部币种的数据'''
        for key, value in USER['USER_FUND_TYPE'].items():
            if cls.query.filter(cls.user_id == user_id, cls.币种 == key).first() is None:
                cls.create_data(user_id, key)

    @classmethod
    def get_one_coin(cls, user_id, 币种):
        return cls.query.filter(cls.user_id == user_id, cls.币种 == 币种).first()

    @classmethod
    def get_all_coin(cls, user_id):
        return cls.query.filter(cls.user_id == user_id).all()

    @classmethod
    def update_amount(cls, user_id, 币种, 金额):
        obj = cls.get_one_coin(user_id, 币种)
        if obj is None:
            cls.create_data
            obj = cls.get_one_coin(user_id, 币种)
        obj.金额 += float(金额)
        db.session.add(obj)
        db.session.commit()
