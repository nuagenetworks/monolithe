# -*- coding: utf-8 -*-

class APISpecAttributeCharacteristicException:
    """ Represents an API attribute definition validation error

    """

    def __init__(self, characteristic, attribute_name, expected_value=None, actual_value=None):
        self.attribute_name = attribute_name
        self.expected_value = expected_value
        self.actual_value   = actual_value
        self.characteristic = characteristic
        self.name           = "Attribute Characteristic Error"

    def __str__(self):
        return "%s: '%s' should be '%s' but is '%s'" % (self.attribute_name, self.characteristic, self.expected_value, self.actual_value)

    def __repr__(self):
            return "<%s> attribute '%s', characteristic: '%s', expected: '%s', actual: '%s'" % (self.__class__.__name__, self.attribute_name, self.characteristic, self.expected_value, self.actual_value)

class APISpecAttributeCapitalizationException:
    """ Represents an API attribute capitalization error

    """

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        self.name           = "Attribute Naming Error"

    def __str__(self):
        return "%s: capitalization seems wrong" % (self.attribute_name)

    def __repr__(self):
            return "<%s> wrong capitalization for '%s'" % (self.__class__.__name__, self.attribute_name)


class APISpecAttributeMissingCharacteristicException:
    """ Represents an API definition missing info characteristic error

    """

    def __init__(self, characteristic, attribute_name):
        self.attribute_name = attribute_name
        self.characteristic          = characteristic
        self.name           = "Missing Attribute Information Error"

    def __str__(self):
        return "%s: information characteristic '%s' is missing" % (self.attribute_name, self.characteristic)

    def __repr__(self):
        return "<%s> attribute '%s': missing characteristic: '%s'" % (self.__class__.__name__, self.attribute_name, self.characteristic)


class APISpecAttributeMissingDefinitionException:
    """ Represents an API attribute missing error

    """

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        self.name           = "Missing Attribute Error"

    def __str__(self):
        return "%s: is missing" % (self.attribute_name)

    def __repr__(self):
        return "<%s> attribute '%s': is missing" % (self.__class__.__name__, self.attribute_name)



class APISpecAPIMissingException:
    """ Represents an API path missing error

    """

    def __init__(self, api_name):
        self.api_name = api_name
        self.name     = "Missing API Error"

    def __str__(self):
        return "%s: missing" % (self.api_name)

    def __repr__(self):
        return "<%s> api '%s': is missing" % (self.__class__.__name__, self.api_name)


class APISpecAPIMissingMethodException:
    """ Represents an API missing method error

    """

    def __init__(self, api_path, expected_methods, actual_methods):
        self.api_path = api_path
        self.expected_methods = expected_methods
        self.actual_methods = actual_methods
        self.name     = "Missing API Method"

    def __str__(self):
        return "%s: methods should be '%s' but is '%s'" % (self.api_path, self.expected_methods, self.actual_methods)

    def __repr__(self):
        return "<%s> api '%s': expected_methods: '%s', actual_methods: '%s'" % (self.__class__.__name__, self.api_path, self.expected_methods, self.actual_methods)