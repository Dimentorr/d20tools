from django import template
import re

register = template.Library()


@register.filter
def get_name_stats(value):
    return value[1]


@register.filter
def get_name_skills(value):
    return value[2]


@register.filter
def get_param_from_object_by_str(obj, name):
    return getattr(obj, name[0])


@register.filter
def get_param_from_stats(obj, name):
    return (getattr(obj, name[0]) - 10) // 2


@register.filter
def _format(value):
    print(value)


register.simple_tag(get_name_skills)
register.simple_tag(get_name_stats)
register.simple_tag(get_param_from_object_by_str)
register.simple_tag(get_param_from_stats)
register.simple_tag(_format)
