from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            for property in self.properties:
                d[property] = getattr(o, property)
            return d
        else:
            return super().default(o)
        pass