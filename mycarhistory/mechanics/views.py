from django.views.generic import TemplateView, DetailView
from mycarhistory.mechanics.models import Mechanic
from mycarhistory.basemodel import Action

class MechanicMainView(TemplateView):
    template_name = 'mechanics/mechanics.html'

    def get_context_data(self, **kwargs):
        context = super(MechanicMainView, self).get_context_data(**kwargs)
        context['mechanics'] = Mechanic.objects.all()
        context['actions'] = [Action('del', 'Delete mechanic'), Action('add', 'Add a mechanic'), Action('modify', 'Modify mechanic')]
        return context

class MechanicDetailView(DetailView):

    template_name = 'generic_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Mechanic.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MechanicDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['header'] = 'Mechanic'
        return context
