from copy import deepcopy


def merge_dict(one, two):
    if isinstance(two, dict):
        result = deepcopy(one)
        for key, value in two.iteritems():
            if key in result and isinstance(result[key], dict):
                result[key] = merge_dict(result[key], value)
            else:
                result[key] = deepcopy(value)
        return result
    return two
