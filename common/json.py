from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, self.model):
        #   if the object to decode is the same class as what's in the
        #   model property, then
        #     * create an empty dictionary that will hold the property names
        #       as keys and the property values as values
        #     * for each name in the properties list
        #         * get the value of that property from the model instance
        #           given just the property name
        #         * put it into the dictionary with that property name as
        #           the key
        #     * return the dictionary
        else:
            return super().default(0)
        pass