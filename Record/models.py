from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from Goal.models import Goal
from User.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    record_time = models.DateField(
        verbose_name="打卡时间",
    )
    record_feeling = models.TextField(
        verbose_name="今日心情",
        null=True,
    )
    record_position = models.TextField(
        verbose_name="打卡定位",
        null=True,
    )
    record_image = models.ImageField(
        verbose_name="打卡配图",
        null=True,
    )
    record_status = models.BooleanField(
        verbose_name="打卡状态",
        default=True
    )

    @classmethod
    def new_record(cls, user, goal, record_time, record_feeling, record_position, record_image):
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
                record_time=record_time,
                record_feeling=record_feeling,
                record_position=record_position,
                record_image=record_image,
            )
            o_record.save()
        except Exception as err:
            print(err)
            return Ret(Error.NEW_RECORD_FAILED)
        return Ret(Error.OK)

    @classmethod
    def cancel_record(cls, user, goal):
        ret_user = User.get_user_by_id(user.id)
        if ret_user.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret_goal = Goal.get_goal_by_id(goal.id)
        if ret_goal.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:


