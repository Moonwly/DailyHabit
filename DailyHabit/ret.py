from DailyHabit.error import Error


class Ret:
    def __init__(self, id=Error.OK, body=None):
        self.id = id
        self.body = body or []
        self.msg = id.msg

