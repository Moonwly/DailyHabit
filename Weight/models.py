from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from User.models import User


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(
        verbose_name="体重",
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    record_date = models.DateField(
        verbose_name="记录时间",
    )
    weight_status = models.BooleanField(
        verbose_name="体重记录状态",
        default=True,
    )

    @classmethod
    def new_weight(cls, user, weight, record_date):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            count = cls.objects.filter(user=user, record_date=record_date, weight_status=True).count()
            if count != 0:
                cls.objects.filter(user=user, record_date=record_date, weight_status=True).update(weight_status=False)
            o_weight = cls(
                user=user,
                weight=weight,
                record_date=record_date,
            )
            o_weight.save()
        except Exception as err:
            print(err)
            return Ret(Error.NEW_WEIGHT_FAILED)
        return Ret(Error.OK)

    @classmethod
    def get_weight(cls, user, record_date):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        weight_list = []
        start = 0
        end = cls.objects.filter(user=user, record_date=record_date, weight_status=True).count()

        try:
            for o_weight in cls.objects.filter(user=user, record_date=record_date, weight_status=True)[start:end]:
                weight_list.append(o_weight.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_WEIGHT)
        return Ret(Error.OK, dict(weight_list=weight_list))

    def to_dict(self):
        return dict(
            weight_id=self.id,
            weight=self.weight,
            record_date=self.record_date,
        )


