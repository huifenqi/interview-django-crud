from django.views.generic import TemplateView


class HouseList(TemplateView):
    template_name = 'list.html'
