import json

from django.views import View

from DailyHabit.error import Error
from DailyHabit.response import response
from User.models import User
from Weight.models import Weight


class NewWeightView(View):
    @staticmethod
    def post(request):
        weight_info = json.loads(request.body.decode())
        weight = weight_info["weight"]
        record_date = weight_info["record_date"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Weight.new_weight(o_user, weight, record_date)
        return response(ret.id)


class GetWeightView(View):
    @staticmethod
    def get(request):
        record_date = request.GET["record_date"]
        user_id = request.session.get("user_id", False)

        ret = User.get_user_by_id(user_id)
        if ret.id != Error.OK:
            return response(Error.NOT_FOUND_USER)
        o_user = ret.body
        ret = Weight.get_weight(o_user, record_date)
        if ret.id != Error.OK:
            return response(ret.id)
        return response(ret.id, ret.body)

