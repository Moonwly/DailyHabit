import json

from django.views import View

from DailyHabit.error import Error
from DailyHabit.response import response
from Goal.models import Goal
from Record.models import Record
from User.models import User


class NewGoalView(View):
    @staticmethod
    def post(request):
        goal_info = json.loads(request.body.decode())
        goal_name = goal_info["goal_name"]
        goal_status = goal_info["goal_status"]
        goal_type = goal_info["goal_type"]
        inspiration = goal_info["inspiration"]
        start_date = goal_info["start_date"]
        end_date = goal_info["end_date"]
        repeat_time = goal_info["repeat_time"]
        recorded_times = goal_info["recorded_times"]
        is_reminding = goal_info["is_reminding"]
        reminding_time = goal_info["reminding_time"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.new_goal(o_user, goal_name, goal_status, goal_type, inspiration, start_date,
                            end_date, repeat_time, recorded_times, is_reminding, reminding_time)
        return response(ret.id)


class FinishGoalView(View):
    @staticmethod
    def get(request):
        goal_id = request.GET["goal_id"]

        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.finish_goal(o_user, goal_id)
        return response(ret.id)


class RestartGoalView(View):
    @staticmethod
    def get(request):
        goal_id = request.GET["goal_id"]

        user_id = request.session.get("user_id", False)
        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.restart_goal(o_user, goal_id)
        return response(ret.id)


class DeleteGoalView(View):
    @staticmethod
    def get(request):
        goal_id = request.GET["goal_id"]

        user_id = request.session.get("user_id", False)
        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.delete_goal(o_user, goal_id)
        return response(ret.id)


class ModifyGoalView(View):
    @staticmethod
    def post(request):
        goal_info = json.loads(request.body.decode())
        goal_id = goal_info["goal_id"]
        goal_name = goal_info["goal_name"]
        goal_status = goal_info["goal_status"]
        goal_type = goal_info["goal_type"]
        inspiration = goal_info["inspiration"]
        start_date = goal_info["start_date"]
        end_date = goal_info["end_date"]
        repeat_time = goal_info["repeat_time"]
        recorded_times = goal_info["recorded_times"]
        is_reminding = goal_info["is_reminding"]
        reminding_time = goal_info["reminding_time"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.modify_goal(o_user, goal_id, goal_status, goal_name, goal_type, inspiration,
                               start_date, end_date, repeat_time, recorded_times, is_reminding, reminding_time)
        return response(ret.id)


class GetUserGoalByIDView(View):
    @staticmethod
    def get(request):
        goal_id = request.GET["goal_id"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.get_user_goal_by_id(o_user, goal_id)
        return response(ret.id, ret.body.to_dict())


class GetGoalByUserView(View):
    @staticmethod
    def get(request):
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.get_goals_by_user(o_user)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)


class GetUserGoalsByGoalStatusView(View):
    @staticmethod
    def get(request):
        goal_status = request.GET["goal_status"]
        user_id = request.session["user_id"]

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.get_goals_by_goal_status(o_user, goal_status)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)


class GetUserTodayGoalsView(View):
    @staticmethod
    def get(request):
        today_date = request.GET["today_date"]
        today_day = request.GET["today_day"]
        user_id = request.session["user_id"]

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Goal.get_user_today_goals(o_user, today_date, today_day)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)
