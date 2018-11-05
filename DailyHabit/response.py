import json
from datetime import date, time
from decimal import Decimal

from django.http import HttpResponse

from DailyHabit.error import Error


def response(id=Error.OK, body=None):
    resp = {
        "code": id.eid,
        "msg": id.msg,
        "body": body or [],
    }
    http_resp = HttpResponse(
        json.dumps(resp, cls=OtherEncoder, ensure_ascii=False),
        status=200,
        content_type="application/json; encoding=utf-8",
    )

    return http_resp


class OtherEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.__str__()
        elif isinstance(obj, time):
            return obj.__str__()
        elif isinstance(obj, Decimal):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)