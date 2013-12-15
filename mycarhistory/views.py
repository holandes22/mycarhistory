from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = 'index.html'


class BrowserIDPageView(TemplateView):

    template_name = 'browserid.html'
