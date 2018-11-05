import json

from django.views import View

from Cost.models import Cost
from DailyHabit.error import Error
from DailyHabit.response import response
from User.models import User


class NewCostView(View):
    @staticmethod
    def post(request):
        cost_info = json.loads(request.body.decode())
        is_outcome = cost_info["is_outcome"]
        description = cost_info["description"]
        money = cost_info["money"]
        record_time = cost_info["record_time"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Cost.new_cost(o_user, is_outcome, description, money, record_time)
        return response(ret.id)


class DeleteCostView(View):
    @staticmethod
    def get(request):
        cost_id = request.GET["cost_id"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Cost.delete_cost(o_user, cost_id)
        return response(ret.id)


class GetUserCostByDateView(View):
    @staticmethod
    def get(request):
        record_date = request.GET["record_date"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Cost.get_user_cost_by_date(o_user, record_date)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)


