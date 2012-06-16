from django.views.generic import TemplateView, DetailView
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

class CarDetailView(DetailView):

    template_name = 'generic_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Car.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CarDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['header'] = 'Car'
        return context
