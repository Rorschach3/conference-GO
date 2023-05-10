from json import JSONEncoder
from datetime import datetime
from django.db.models import QuerySet

class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class ModelEncoder(DateEncoder, JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            for property in self.properties:
                value = getattr(o, property)
                d[property] = value
            return d
        else:
            return super().default(o)
        