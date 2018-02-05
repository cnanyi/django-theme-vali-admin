from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class DashboardView(TemplateView):
    template_name = 'vali/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # load sample data
        context['icons'] = [{"title": "展示数据1", "value": 5, "style": "primary", "icon": "fa-users"},
                                {"title": "展示数据2", "value": 15, "style": "info", "icon": "fa-thumbs-o-up"},
                                {"title": "展示数据3", "value": 80, "style": "warning", "icon": "fa-files-o"},
                                {"title": "展示数据4", "value": 500, "style": "danger", "icon": "fa-star"}]
        return context
