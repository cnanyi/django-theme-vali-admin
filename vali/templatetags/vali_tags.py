import re
from django import template
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse, resolve
from django.utils.safestring import mark_safe
from django.forms.models import ModelMultipleChoiceField
from vali.widgets import ValiRelatedFieldWidgetWrapper
register = template.Library()


@register.simple_tag(takes_context=True)
def get_menu(context, request):
    """ copy from django-suit project, return the system app_list directly """
    if not isinstance(request, HttpRequest):
        return None
    if hasattr(request, 'current_app'):
        # Django 1.8 uses request.current_app instead of context.current_app
        template_response = get_admin_site(request.current_app).index(request)
    else:
        try:
            template_response = get_admin_site(context.current_app).index(request)
        # Django 1.10 removed the current_app parameter for some classes and functions.
        # Check the release notes.
        except AttributeError:
            template_response = get_admin_site(context.request.resolver_match.namespace).index(request)
    try:
        app_list = template_response.context_data['app_list']
    except Exception:
        return
    return app_list


@register.simple_tag()
def vali_fieldset(fieldset):
    for field in fieldset.form.fields:
        if isinstance(fieldset.form.fields[field], ModelMultipleChoiceField):
            relw = fieldset.form.fields[field].widget
            fieldset.form.fields[field].widget = \
                ValiRelatedFieldWidgetWrapper(relw.widget, relw.rel, relw.admin_site,
                                              relw.can_add_related, relw.can_change_related, relw.can_delete_related)
        else:
            attrs = fieldset.form.fields[field].widget.attrs

            oldclass = attrs['class'] if 'class' in attrs else ''

            if fieldset.form.errors and field in fieldset.form._errors:
                oldclass = oldclass + ' is-invalid'

            fieldset.form.fields[field].widget.attrs['class'] = oldclass + ' form-control'
    return fieldset


@register.simple_tag()
def vali_field(field):
    attrs = field.field.widget.attrs
    oldclass = attrs['class'] if 'class' in attrs else ''
    field.field.widget.attrs['class'] = oldclass + ' form-control'
    return field


@register.simple_tag()
def vali_rendered_widget(widget):
    if "multiple" in widget:
        return mark_safe(widget)
    if 'class=' in widget:
        return mark_safe(widget.replace('class="', 'class="form-control '))
    else:
        return mark_safe(widget.replace('<select ', '<select class="form-control" '))


@register.simple_tag()
def vali_errors(errors):

    return mark_safe(re.sub('<.+?>', '', errors))


@register.simple_tag(name='VALI_THEME')
def vali_theme():
    theme = vali_config('theme')
    return theme if theme else 'default'


def get_admin_site(current_app):
    """
        Method tries to get actual admin.site class, if any custom admin sites
        were used. Couldn't find any other references to actual class other than
        in func_closer dict in index() func returned by resolver.
        """
    try:
        resolver_match = resolve(reverse('%s:index' % current_app))
        # Django 1.9 exposes AdminSite instance directly on view function
        if hasattr(resolver_match.func, 'admin_site'):
            return resolver_match.func.admin_site

        for func_closure in resolver_match.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass
    return admin.site


@register.simple_tag()
def vali_config(param=None):
    config_key = 'VALI_CONFIG'
    if hasattr(settings, config_key):
        config = getattr(settings, config_key, {})
    else:
        config = {'theme': 'default'}
    if param:
        return config.get(param)
    else:
        return config