from json import JSONEncoder


class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(0)
        
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
        