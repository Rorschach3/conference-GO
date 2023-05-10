from json import JSONEncoder


class DateEncoder(JSONEncoder):
    def default(self, o):
        # if o is an instance of datetime
        #    return o.isoformat()
        # otherwise
        #    return super().default(o)
        
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
        