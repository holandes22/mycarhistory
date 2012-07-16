from django.views.generic import TemplateView, DetailView
from mycarhistory.cars.models import Car, CarForm
from mycarhistory.basemodel import Action, get_permalink
from mycarhistory.basemodel import EDITOR_DIALOG_ID
from mycarhistory.basemodel import BaseUpdateView, BaseCreateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy


class CarMainView(TemplateView):
    template_name = 'cars/cars.html'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CarMainView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        #For the toolbar action dropdown
        context['actions'] = [Action(get_permalink('car-create'), 'Add a car')]
        context['dialog_id'] = EDITOR_DIALOG_ID
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
        context['dialog_id'] = EDITOR_DIALOG_ID
        # Action buttons within the details table
        context['actions'] = [
                Action(get_permalink('car-update', self.get_queryset()[0].pk), 'Update Details'),
                Action(get_permalink('car-delete', self.get_queryset()[0].pk), 'Remove Car')
                ]
        return context


class CarCreateView(BaseCreateView):
    form_class = CarForm
    model = Car


class CarUpdateView(BaseUpdateView):
    form_class = CarForm
    model = Car


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car-main')
