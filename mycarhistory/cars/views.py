from django.views.generic import TemplateView
from mycarhistory.cars.models import Car

class Action(object):

    def __init__(self, url, title):
        self.url = url
        self.title = title

class CarMainView(TemplateView):
    template_name = 'cars/cars.html'

    def get_context_data(self, **kwargs):
        context = super(CarMainView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        context['actions'] = [Action('del', 'Delete'), Action('add', 'Add car')]
        return context
