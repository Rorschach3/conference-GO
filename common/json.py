from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    def default(self, o):
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
        #   otherwise,
        #       return super().default(o)  # From the documentation
        pass