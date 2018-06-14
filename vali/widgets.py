from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, FilteredSelectMultiple
from django.conf import settings
from django import forms


class ValiDashboardWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return 'render'


class ValiDateWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return 'dateinput'


class ValiDateTimeWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return 'datetimeinput'


# todo  display the ValiRelatedFieldWidgetWrapper as multiple checkboxes , it's ongoing
class ValiFilteredSelectMultiple(FilteredSelectMultiple):
    """ customize FilteredSelectMultiple, not used for now """
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'selectfilter'
        if self.is_stacked:
            context['widget']['attrs']['class'] += 'stacked'
        context['widget']['attrs']['data-field-name'] = self.verbose_name
        context['widget']['attrs']['data-is-stacked'] = int(self.is_stacked)
        return context


class ValiRelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    """ customize ValiRelatedFieldWidgetWrapper, not used for now """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = ValiFilteredSelectMultiple(verbose_name=self.widget.verbose_name,
                                                 is_stacked=self.widget.is_stacked,
                                                 attrs=self.widget.attrs,
                                                 choices=self.widget.choices)

