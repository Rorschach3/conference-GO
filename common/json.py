from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            for property in self.properties:
                d.append(
            return d
        else:
            return super().default(0)
        pass