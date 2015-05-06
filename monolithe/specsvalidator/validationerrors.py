# -*- coding: utf-8 -*-

class APISpecAttributeDefinitionError:
    """ Represents an API attribute definition validation error

    """

    def __init__(self, token, attribute_name, expected_value=None, actual_value=None):
        self.attribute_name = attribute_name
        self.expected_value = expected_value
        self.actual_value   = actual_value
        self.token          = token

    def __str__(self):
        return "%s: '%s' should be '%s' but is '%s'" % (self.attribute_name, self.token, self.expected_value, self.actual_value)

    def __repr__(self):
            return "<%s> attribute '%s', token: '%s', expected: '%s', actual: '%s'" % (self.__class__.__name__, self.attribute_name, self.token, self.expected_value, self.actual_value)

class APISpecAttributeCapitalizationError:
    """ Represents an API attribute capitalization error

    """

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __str__(self):
        return "%s: capitalization seems wrong" % (self.attribute_name)

    def __repr__(self):
            return "<%s> wrong capitalization for '%s'" % (self.__class__.__name__, self.attribute_name)


class APISpecMissingTokenError:
    """ Represents an API definition missing info token error

    """

    def __init__(self, token, attribute_name):
        self.attribute_name = attribute_name
        self.token = token

    def __str__(self):
        return "%s: information token '%s' is missing" % (self.attribute_name, self.token)

    def __repr__(self):
        return "<%s> attribute '%s': missing token: '%s'" % (self.__class__.__name__, self.attribute_name, self.token)


class APISpecMissingAttributeDefinitionError:
    """ Represents an API attribute missing error

    """

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __str__(self):
        return "%s: is missing" % (self.attribute_name)

    def __repr__(self):
        return "<%s> attribute '%s': is missing" % (self.__class__.__name__, self.attribute_name)


class APISpecMissingParentAPIError:
    """ Represents an API path missing error

    """

    def __init__(self, api_name):
        self.api_name = api_name

    def __str__(self):
        return "%s: missing" % (self.api_name)

    def __repr__(self):
        return "<%s> parent api '%s': is missing" % (self.__class__.__name__, self.api_name)


class APISpecMissingParentAPIMethodError:
    """ Represents an API missing method error

    """

    def __init__(self, api_path, expected_methods, actual_methods):
        self.api_path = api_path
        self.expected_methods = expected_methods
        self.actual_methods = actual_methods

    def __str__(self):
        return "%s: methods should be '%s' but is '%s'" % (self.api_path, self.expected_methods, self.actual_methods)

    def __repr__(self):
        return "<%s> parent api '%s': expected_methods: '%s', actual_methods: '%s'" % (self.__class__.__name__, self.api_path, self.expected_methods, self.actual_methods)