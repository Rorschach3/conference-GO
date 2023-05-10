from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            for property in self.properties:
                value = getattr(o, property)
                d[property] = value
            return d
        else:
            return super().default(o)
        
class DateEncoder(JSONEncoder):
    def default(self, o):
        if o = 