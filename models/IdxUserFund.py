from run import db

from configs.config import USER

from models.LogUserFund import LogUserFund


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
        for 币种 in USER['USER_FUND_TYPE']:
            if cls.query.filter(cls.user_id == user_id, cls.币种 == 币种).first() is None:
                cls.create_data(user_id, 币种)

    @classmethod
    def get_one_coin(cls, user_id, 币种):
        '''获取某种币种的数据对象'''
        obj = cls.query.filter(cls.user_id == user_id, cls.币种 == 币种).first()
        if obj is None:
            cls.create_all_data(user_id, 币种)
            obj = cls.query.filter(cls.user_id == user_id, cls.币种 == 币种).first()
        return obj

    @classmethod
    def get_all_coin(cls, user_id):
        '''获取全部币种的数据对象'''
        objs = cls.query.filter(cls.user_id == user_id).all()
        if len(objs) == 0:
            cls.create_all_data(user_id)
            objs = cls.query.filter(cls.user_id == user_id).all()
        return objs

    @classmethod
    def update_amount(cls, user_id, 币种, 金额, 说明='', 备注='', return_type='bool'):
        '''更新币种
        一般情况下，更新币种金额伴随着日志的记录和其他数据的更新，如商城项目中购买商品要同时添加订单与扣款
        这就可能会需要放置在一起，以便保证事务的原子性
        '''
        obj = cls.get_one_coin(user_id, 币种)
        obj.金额 += float(金额)
        db.session.add(obj)
        if return_type == 'bool':
            try:
                db.session.add(LogUserFund.create_data(user_id, 币种, 金额, 说明, 备注))
                db.session.commit()
                return True
            except BaseException:
                db.session.rollback()
                return False
        else:
            return db
