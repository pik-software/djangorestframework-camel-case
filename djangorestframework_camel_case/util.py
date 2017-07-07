import re
from collections import OrderedDict

from django.utils import six

first_cap_re = re.compile('(.)([A-Z]|[0-9]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def underscore_to_camel(match):
    return match.group()[0] + match.group()[2].upper()


def camelize(data):
    if isinstance(data, dict):
        new_dict = OrderedDict()
        for key, value in data.items():
            if isinstance(key, six.string_types):
                new_key = re.sub(r"[a-z0-9]_[a-z0-9]", underscore_to_camel, key)
            else:
                new_key = key
            new_dict[new_key] = camelize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        return [camelize(item) for item in data]
    return data


def camel_to_underscore(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def underscoreize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if isinstance(key, six.string_types):
                new_key = camel_to_underscore(key)
            else:
                new_key = key
            new_dict[new_key] = underscoreize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        return [underscoreize(item) for item in data]

    return data