from django.views.generic import TemplateView, DetailView, CreateView
from mycarhistory.cars.models import Car, CarForm
from mycarhistory.basemodel import Action, get_permalink
from mycarhistory.basemodel import EDITOR_FORM_ID, EDITOR_DIALOG_ID


class CarMainView(TemplateView):
    template_name = 'cars/cars.html'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CarMainView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        context['actions'] = [Action(get_permalink('car-create'), 'Create a car')]
        context['editor_dialog_id'] = EDITOR_DIALOG_ID
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

class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'editor.html'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', None)
        # return get_permalink('cars-main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CarCreateView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('car-create')
        context['editor_form_id'] = EDITOR_FORM_ID
        context['editor_dialog_id'] = EDITOR_DIALOG_ID
        return context
