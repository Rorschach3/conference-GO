from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
            d = {}
        #     * for each name in the properties list
        #         * get the value of that property from the model instance
        #           given just the property name
        #         * put it into the dictionary with that property name as
        #           the key
            return d
        else:
            return super().default(0)
        pass