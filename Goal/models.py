from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from User.models import User


class Goal(models.Model):
    L = {
        'goal_name': 255,
        'repeat_time': 255,
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # goal_status: True 进行中  False 已结束
    goal_status = models.BooleanField(
        verbose_name="目标状态",
        default=True,
    )
    goal_name = models.CharField(
        verbose_name="目标名",
        max_length=L['goal_name'],
    )
    goal_type = models.IntegerField(
        verbose_name="目标类型",
        default=0,
    )
    inspiration = models.TextField(
        verbose_name="激励语",
        null=True,
    )
    start_date = models.DateField(
        verbose_name="开始日期",
    )
    end_date = models.DateField(
        verbose_name="结束日期",
    )
    repeat_time = models.CharField(
        verbose_name="重复时间",
        max_length=L['repeat_time'],
        default="MON, TUE, WED, THU, FRI, SAT, SUN,",
    )
    total_day = models.IntegerField(
        verbose_name="总天数",
        default=0,
    )
    is_reminding = models.BooleanField(
        verbose_name="是否开启提醒",
        default=False,
    )
    reminding_time = models.TimeField(
        verbose_name="提醒时间",
        null=True,
    )
    is_delete = models.BooleanField(
        verbose_name="是否删除",
        default=False,
    )

    @classmethod
    def get_goal_by_id(cls, goal_id):
        try:
            o_goal = cls.objects.get(id=goal_id)
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_GOAL)
        return Ret(Error.OK, o_goal)

    @classmethod
    def get_goals_by_user(cls, user):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        goal_list = []
        start = 0
        end = cls.objects.filter(user=user).count()

        try:
            for o_goal in cls.objects.filter(user=user)[start:end]:
                goal_list.append(o_goal.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_GOAL_OF_USER)
        return Ret(Error.OK, dict(goal_list=goal_list))

    @classmethod
    def get_user_goal_by_id(cls, user, goal_id):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            o_goal = cls.objects.get(id=goal_id, user_id=user.id)
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_GOAL)
        return Ret(Error.OK, o_goal)

    @classmethod
    def new_goal(cls, user, goal_name, goal_status, goal_type, inspiration,
                 start_date, end_date, repeat_time, total_day, is_reminding, reminding_time):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            o_goal = cls(
                user=user,
                goal_name=goal_name,
                goal_status=goal_status,
                goal_type=goal_type,
                inspiration=inspiration,
                start_date=start_date,
                end_date=end_date,
                repeat_time=repeat_time,
                total_day=total_day,
                is_reminding=is_reminding,
                reminding_time=reminding_time,
            )
            o_goal.save()
        except Exception as err:
            print(err)
            return Ret(Error.NEW_GOAL_FAILED)
        return Ret(Error.OK)

    @classmethod
    def finish_goal(cls, user, goal_id):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret = Goal.get_goal_by_id(goal_id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            cls.objects.filter(id=goal_id).update(goal_status=False)
        except Exception as err:
            print(err)
            return Ret(Error.FINISH_GOAL_FAILED)
        return Ret(Error.OK)

    @classmethod
    def restart_goal(cls, user, goal_id):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret = Goal.get_goal_by_id(goal_id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            cls.objects.filter(id=goal_id).update(goal_status=True)
        except Exception as err:
            print(err)
            return Ret(Error.FINISH_GOAL_FAILED)
        return Ret(Error.OK)

    @classmethod
    def delete_goal(cls, user, goal_id):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret = Goal.get_goal_by_id(goal_id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            cls.objects.filter(id=goal_id).update(is_delete=True)
        except Exception as err:
            print(err)
            return Ret(Error.DELETE_GOAL_FAILED)
        return Ret(Error.OK)

    @classmethod
    def modify_goal(cls, user, goal_id, goal_status, goal_name, goal_type, inspiration,
                    start_date, end_date, repeat_time, total_day, is_reminding, reminding_time):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        ret = Goal.get_goal_by_id(goal_id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_GOAL)
        try:
            cls.objects.filter(id=goal_id).update(goal_status=goal_status, goal_name=goal_name,
                                                  goal_type=goal_type, inspiration=inspiration,
                                                  start_date=start_date, end_date=end_date,
                                                  repeat_time=repeat_time, total_day=total_day,
                                                  is_reminding=is_reminding, reminding_time=reminding_time)
        except Exception as err:
            print(err)
            return Ret(Error.MODIFY_GOAL_FAILED)
        return Ret(Error.OK)

    @classmethod
    def get_goals_by_goal_status(cls, user, goal_status):
        ret = User.get_user_by_id(user.id)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        goal_list = []
        start = 0
        end = cls.objects.filter(user=user, goal_status=goal_status).count()

        try:
            for o_goal in cls.objects.filter(user=user, goal_status=goal_status)[start:end]:
                goal_list.append(o_goal.to_dict())
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_GOAL_OF_STATUS)
        return Ret(Error.OK, dict(goal_list=goal_list))

    def to_dict(self):
        return dict(
            goal_id=self.id,
            goal_name=self.goal_name,
            goal_status=self.goal_status,
            goal_type=self.goal_type,
            inspiration=self.inspiration,
            start_date=self.start_date,
            end_date=self.end_date,
            repeat_time=self.repeat_time,
            total_day=self.total_day,
            is_reminding=self.is_reminding,
            reminding_time=self.reminding_time,
        )
