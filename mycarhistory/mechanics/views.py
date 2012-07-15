from django.views.generic import TemplateView, DetailView
from mycarhistory.mechanics.models import Mechanic, MechanicForm
from mycarhistory.basemodel import EDITOR_DIALOG_ID
from mycarhistory.basemodel import Action, get_permalink
from mycarhistory.basemodel import BaseUpdateView, BaseCreateView


class MechanicMainView(TemplateView):
    template_name = 'mechanics/mechanics.html'

    def get_context_data(self, **kwargs):
        context = super(MechanicMainView, self).get_context_data(**kwargs)
        context['mechanics'] = Mechanic.objects.all()
        context['actions'] = [Action(get_permalink('mechanic-create'), 'Add a mechanic')]
        context['editor_dialog_id'] = EDITOR_DIALOG_ID
        return context


class MechanicDetailView(DetailView):

    template_name = 'generic_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Mechanic.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(MechanicDetailView, self).get_context_data(**kwargs)
        context['header'] = 'Mechanic'
        context['editor_dialog_id'] = EDITOR_DIALOG_ID
        context['actions'] = [Action(get_permalink('mechanic-update', self.get_queryset()[0].pk), 'Update details')]
        return context


class MechanicCreateView(BaseCreateView):
    form_class = MechanicForm
    model = Mechanic


class MechanicUpdateView(BaseUpdateView):
    form_class = MechanicForm
    model = Mechanic
