class E:
    _error_id = 0

    def __init__(self, msg):
        self.eid = E._error_id
        self.msg = msg
        E._error_id += 1


class Error:
    OK = E("没有错误")
    STRANGE = E("奇怪错误")
    REGISTER_FAILED = E("注册失败")
    EMAIL_EXIST = E("邮箱已注册")
    NOT_FOUND_USER = E("未查找到用户")
    INCORRECT_PARAMETER = E("参数格式错误")
    LOGIN_FAILED = E("登录失败")
    MODIFY_PASSWORD_FAILED = E("修改密码失败")
    MODIFY_USERNAME_FAILED = E("修改用户名失败")
    NEW_GOAL_FAILED = E("新建目标失败")
    NOT_FOUND_GOAL = E("未查找到目标")
    FINISH_GOAL_FAILED = E("结束目标失败")
    DELETE_GOAL_FAILED = E("删除目标失败")
    MODIFY_GOAL_FAILED = E("修改目标失败")
    NOT_FOUND_GOAL_OF_USER = E("未查找到用户的目标")
    NOT_FOUND_GOAL_OF_STATUS = E("未查找到该状态的目标")
    NEW_RECORD_FAILED = E("新建打卡记录失败")
    CANCEL_RECORD_FAILED = E("取消打卡失败")
    NOT_FOUND_RECORD_OF_USER = E("未查找到打卡记录")
    NOT_FOUND_RECORD_OF_DATE = E("未查找到该日期的打卡记录")
    NEW_WEIGHT_FAILED = E("新建体重记录失败")
    NOT_FOUND_WEIGHT = E("未查找到体重记录")




