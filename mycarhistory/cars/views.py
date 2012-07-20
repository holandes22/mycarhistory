from django.views.generic import TemplateView, DetailView
from mycarhistory.cars.models import Car, CarForm
from mycarhistory.mechanics.models import Mechanic
from mycarhistory.cars.models import CarTreatmentEntry, PlannedCarTreatmentEntry, CarTreatmentForm, PlannedCarTreatmentForm
from mycarhistory.basemodel import Action, get_permalink
from mycarhistory.basemodel import EDITOR_DIALOG_ID
from mycarhistory.basemodel import BaseUpdateView, BaseCreateView, BaseDeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy


class CarMainView(TemplateView):
    template_name = 'cars/cars.html'

    def get_context_data(self, **kwargs):
        context = super(CarMainView, self).get_context_data(**kwargs)
        #For the toolbar action dropdown
        context['actions'] = [
                Action(get_permalink('car-create'), 'Add a car'),
                Action(get_permalink('cartreatmententry-create'), 'Add a treatment'),
                ]
        context['dialog_id'] = EDITOR_DIALOG_ID
        context['sidebar_url'] = get_permalink('car-list')
        return context


class CarListView(ListView):
    template_name = 'cars/sidebar.html'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        context['cars'] = self.get_queryset()
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


class CarDeleteView(BaseDeleteView):
    model = Car
    success_url = reverse_lazy('car-main')


class CarTreatmentListView(ListView):
    template_name = 'cars/treatment_list.html'

    def get_queryset(self):
        car = Car.objects.get(pk=self.kwargs['car_pk'])
        return CarTreatmentEntry.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super(CarTreatmentListView, self).get_context_data(**kwargs)
        context['treatments'] = self.get_queryset()
        return context


class CarTreatmentCreateView(BaseCreateView):
    form_class = CarTreatmentForm
    model = CarTreatmentEntry

    def get_loader_args(self):
        # TODO: for now only. Change the loader to trigger treatment list of
        # car
        return ['.car-details', get_permalink('car-list')]

    def get_form(self, form_class):
        # Filter the cars and mechanics that belong to the logged user
        form = super(CarTreatmentCreateView, self).get_form(form_class)
        form.fields['mechanic'].queryset = Mechanic.objects.filter(user=self.request.user)
        form.fields['car'].queryset = Car.objects.filter(user=self.request.user)
        return form
