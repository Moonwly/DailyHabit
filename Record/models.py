from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from Goal.models import Goal
from User.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    record_date = models.DateField(
        verbose_name="打卡时间",
    )
    record_feeling = models.TextField(
        verbose_name="今日心情",
        null=True,
    )
    record_status = models.BooleanField(
        verbose_name="打卡状态",
        default=True
    )

    @classmethod
    def new_record(cls, user, goal, record_date, record_feeling):
        ret_user = User.get_user_by_id(user.id)
        if ret_user.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret_goal = Goal.get_goal_by_id(goal.id)
        if ret_goal.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            o_record = cls(
                user=user,
                goal=goal,
                record_date=record_date,
                record_feeling=record_feeling,
            )
            o_record.save()
        except Exception as err:
            print(err)
            return Ret(Error.NEW_RECORD_FAILED)
        return Ret(Error.OK)

    @classmethod
    def cancel_record(cls, user, goal, record_id):
        ret_user = User.get_user_by_id(user.id)
        if ret_user.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret_goal = Goal.get_goal_by_id(goal.id)
        if ret_goal.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            cls.objects.filter(user=user, goal=goal, id=record_id, record_status=True).update(record_status=False)
        except Exception as err:
            print(err)
            return Ret(Error.CANCEL_RECORD_FAILED)
        return Ret(Error.OK)

    @classmethod
    def get_user_record(cls, user):
        ret_user = User.get_user_by_id(user.id)
        if ret_user.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        record_list = []
        start = 0
        end = cls.objects.filter(user=user, record_status=True).count()
        if end > 20:
            start = end - 20

        try:
            for o_record in cls.objects.filter(user=user, record_status=True)[start:end]:
                record_list.append(o_record.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_RECORD_OF_USER)
        return Ret(Error.OK, dict(record_list=record_list))

    @classmethod
    def get_user_record_by_date(cls, user, record_date):
        ret_user = User.get_user_by_id(user.id)
        if ret_user.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        record_list = []
        start = 0
        end = cls.objects.filter(user=user, record_date=record_date, record_status=True).count()
        if end > 20:
            start = end - 20

        try:
            for o_record in cls.objects.filter(user=user, record_date=record_date, record_status=True)[start:end]:
                record_list.append(o_record.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_RECORD_OF_DATE)
        return Ret(Error.OK, dict(record_list=record_list))

    def to_dict(self):
        return dict(
            record_id=self.id,
            record_date=self.record_date,
            record_feeling=self.record_feeling,
            record_status=self.record_status,
        )




