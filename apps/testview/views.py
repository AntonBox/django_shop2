from django.views.generic.base import TemplateView


class TestView(TemplateView):
    template_name = "index.html"
