from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from User.models import User


class Cost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # False: 收入  True: 支出
    is_outcome = models.BooleanField(
        verbose_name="是否为收入",
        default=True,
    )
    description = models.TextField(
        verbose_name="描述",
    )
    money = models.DecimalField(
        verbose_name="收入/支出金额",
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    record_time = models.DateTimeField(
        verbose_name="记录时间",
    )
    cost_status = models.BooleanField(
        verbose_name="消费记录状态",
        default=True,
    )
    @classmethod
    def new_cost(cls, user, is_outcome, description, money, record_time):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            o_cost = cls(
                user=user,
                is_outcome=is_outcome,
                description=description,
                money=money,
                record_time=record_time,
            )
            o_cost.save()
        except Exception as err:
            print(err)
            return Ret(Error.NEW_COST_FAILED)
        return Ret(Error.OK)

    @classmethod
    def delete_cost(cls, user, cost_id):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            cls.objects.filter(user=user, id=cost_id, cost_status=True).update(cost_status=False)
        except Exception as err:
            print(err)
            return Ret(Error.DELETE_COST_FAILED)
        return Ret(Error.OK)

    @classmethod
    def get_user_cost_by_date(cls, user, record_date):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        start_date = record_date + " 00:00"
        end_date = record_date + " 23:59"
        cost_list = []
        start = 0
        end = cls.objects.filter(user=user, record_time__gte=start_date,
                                 record_time__lte=end_date, cost_status=True).count()
        try:
            for o_cost in cls.objects.filter(user=user, record_time__gte=start_date,
                                             record_time__lte=end_date, cost_status=True)[start:end]:
                cost_list.append(o_cost.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_COST)
        return Ret(Error.OK, dict(cost_list=cost_list))

    def to_dict(self):
        return dict(
            cost_id=self.id,
            is_outcome=self.is_outcome,
            description=self.description,
            money=self.money,
            record_time=self.record_time,
        )
