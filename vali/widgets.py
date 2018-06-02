from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, FilteredSelectMultiple
from django.conf import settings
from django import forms


class ValiFilteredSelectMultiple(FilteredSelectMultiple):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'selectfilter'
        if self.is_stacked:
            context['widget']['attrs']['class'] += 'stacked'
        context['widget']['attrs']['data-field-name'] = self.verbose_name
        context['widget']['attrs']['data-is-stacked'] = int(self.is_stacked)
        return context


class ValiRelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = ValiFilteredSelectMultiple(verbose_name=self.widget.verbose_name,
                                                 is_stacked=self.widget.is_stacked,
                                                 attrs=self.widget.attrs,
                                                 choices=self.widget.choices)