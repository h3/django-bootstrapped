from django import template
from django.template import Context, Template
from django.conf import settings

register = template.Library()

BOOTSTRAP_FORM_CONTROL_GROUP = """
<div class="control-group{% if element.errors %} error{% endif %}{% if options.span %} span{{ options.span }}{% endif %}">
    {% if input_type == "radio" %}
    <div class="controls">
        <label for="{{ element.id_for_label }}" class="checkbox">{{ element }} {{ element.label }}</label>
    </div>
    {% else %}
    <label for="{{ element.id_for_label }}" class="control-label">{{ element.label }}</label>
    <div class="controls">
        {% if options.prepend %}
        <div class="input-prepend">
            <span class="add-on">{{ options.prepend }}</span>{{ element }}
        </div>
        {% elif options.append %}
        <div class="input-append">
            {{ element }}<span class="add-on">{{ options.append }}</span>
        </div>
        {% else %}
        {{ element }}
        {% endif %}
    </div>
    {% endif %}
</div>"""


@register.simple_tag
def bootstrap_less(less):
    return '<script src="%sjs/less-1.1.5.min.js" type="text/javascript"></script>' % settings.STATIC_URL

@register.assignment_tag
def control_group(element, *args, **kwargs):
    t = Template(BOOTSTRAP_FORM_CONTROL_GROUP)
    return t.render(Context({
        "element": element, 
        'options': kwargs,
        "input_type": kwargs.get('input_type', 'text'),
    }))
