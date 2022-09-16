from datetime import datetime

from django import template
from django.utils.safestring import mark_safe

from web.models import Content

register = template.Library()


@register.simple_tag
def get_content(slug, default):
    content, _ = Content.objects.get_or_create(slug=slug, defaults={"content": default})
    if content == "":
        content = "{" + slug + "}"
    return mark_safe(content.content)


@register.filter
def more_human_readable_price(human_readable_price):
    return human_readable_price.replace(".00", "").replace("USD", "")


@register.filter
def readable_price(price):
    if price < 0:
        return f'(${str(price).replace(".00", "").replace(".0", "").replace("-", "")})'

    return f'${str(price).replace(".00", "").replace(".0", "")}'


@register.filter
def clean_str_date(value):
    if value and " " in value:
        split_value = value.split(" ", 1)
        return split_value[0]
    return value
