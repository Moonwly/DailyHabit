import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from DailyHabit.error import Error
from DailyHabit.response import response
from User.models import User


class CreateUserView(View):
    @staticmethod
    def post(request):
        user_info = json.loads(request.body.decode())
        password = user_info["password"]
        email = user_info["email"]

        ret = User.create_user(password, email)
        if ret.id != Error.OK:
            return response(ret.id)
        request.session["user_id"] = ret.body.id
        return response(ret.id, ret.body.to_dict())


class LoginView(View):
    @staticmethod
    def post(request):
        user_info = json.loads(request.body.decode())
        email = user_info["email"]
        password = user_info["password"]

        ret = User.login(email, password)
        if ret.id == Error.LOGIN_FAILED:
            return response(ret.id)
        request.session["user_id"] = ret.body.id
        return response(ret.id, ret.body.to_dict())


# TODO: logout
# TODO: modify_password
# TODO: modify_username
