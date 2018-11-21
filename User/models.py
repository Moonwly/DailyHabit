from django.db import models

from DailyHabit.error import Error
from DailyHabit.ret import Ret
from DailyHabit.valid import Valid


class User(models.Model):
    L = {
        'email': 255,
        'username': 255,
        'password': 255,
    }

    email = models.CharField(
        verbose_name='邮箱',
        max_length=L['email'],
        unique=True,
    )
    username = models.CharField(
        verbose_name='用户名',
        max_length=L['username'],
    )
    password = models.CharField(
        verbose_name='密码',
        max_length=L['password'],
    )

    @classmethod
    def get_user_by_email(cls, email):
        if not Valid.valid_email(email):
            return Ret(Error.INCORRECT_PARAMETER)
        try:
            o_user = cls.objects.get(email=email)
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_USER)
        return Ret(Error.OK, o_user)

    @classmethod
    def get_user_by_id(cls, user_id):
        try:
            o_user = cls.objects.get(id=user_id)
        except cls.DoesNotExist:
            return Ret(Error.NOT_FOUND_USER)
        return Ret(Error.OK, o_user)

    @classmethod
    def create_user(cls, password, email):
        if not Valid.valid_email(email) or not Valid.valid_password(password):
            return Ret(Error.INCORRECT_PARAMETER)
        try:
            o_user = cls(
                email=email,
                password=password,
            )
            ret = User.get_user_by_email(email)
            if ret.id == Error.OK:
                return Ret(Error.EMAIL_EXIST)
            o_user.save()
        except Exception as err:
            print(err)
            return Ret(Error.REGISTER_FAILED)
        return Ret(Error.OK, o_user)

    @classmethod
    def login(cls, email, password):
        if not Valid.valid_email(email) or not Valid.valid_password(password):
            return Ret(Error.INCORRECT_PARAMETER)
        try:
            o_user = cls.objects.get(email=email, password=password)
        except cls.DoesNotExist:
            return Ret(Error.LOGIN_FAILED)
        return Ret(Error.OK, o_user)

    @classmethod
    def modify_password(cls, email, new_password):
        if not Valid.valid_email(email) or not Valid.valid_password(new_password):
            return Ret(Error.INCORRECT_PARAMETER)
        ret = User.get_user_by_email(email)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            cls.objects.filter(email=email).update(password=new_password)
        except Exception as err:
            print(err)
            return Ret(Error.MODIFY_PASSWORD_FAILED)
        return Ret(Error.OK)

    @classmethod
    def modify_username(cls, email, new_username):
        if not Valid.valid_email(email) or not Valid.valid_username(new_username):
            return Ret(Error.INCORRECT_PARAMETER)
        ret = User.get_user_by_email(email)
        if ret.id != Error.OK:
            return Ret(Error.NOT_FOUND_USER)
        try:
            cls.objects.filter(email=email).update(username=new_username)
        except Exception as err:
            print(err)
            return Ret(Error.MODIFY_USERNAME_FAILED)
        return Ret(Error.OK)

    def to_dict(self):
        return dict(
            user_id=self.id,
            username=self.username,
            email=self.email
        )
