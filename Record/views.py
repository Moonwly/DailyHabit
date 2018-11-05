import json

from django.views import View

from DailyHabit.error import Error
from DailyHabit.response import response
from Goal.models import Goal
from Record.models import Record
from User.models import User


class NewRecordView(View):
    @staticmethod
    def post(request):
        record_info = json.loads(request.body.decode())
        goal_id = record_info["goal_id"]
        record_date = record_info["record_date"]
        record_feeling = record_info["record_feeling"]
        user_id = request.session.get("user_id", False)

        ret_user = User.get_user_by_id(user_id)
        if ret_user.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret_user.body
        ret_goal = Goal.get_goal_by_id(goal_id)
        if ret_goal.id != Error.OK:
            return response(Error.NOT_FOUND_GOAL)
        o_goal = ret_goal.body
        ret = Record.new_record(o_user, o_goal, record_date, record_feeling)
        return response(ret.id)


class CancelRecordView(View):
    @staticmethod
    def get(request):
        goal_id = request.GET["goal_id"]
        record_id = request.GET["record_id"]
        user_id = request.session.get("user_id", False)

        ret_user = User.get_user_by_id(user_id)
        if ret_user.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret_user.body
        ret_goal = Goal.get_goal_by_id(goal_id)
        if ret_goal.id != Error.OK:
            return response(Error.NOT_FOUND_GOAL)
        o_goal = ret_goal.body
        ret = Record.cancel_record(o_user, o_goal, record_id)
        return response(ret.id)


class GetUserRecordView(View):
    @staticmethod
    def get(request):
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Record.get_user_record(o_user)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)


class GetUserRecordByDateView(View):
    @staticmethod
    def get(request):
        record_date = request.GET["record_date"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Record.get_user_record_by_date(o_user, record_date)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)

