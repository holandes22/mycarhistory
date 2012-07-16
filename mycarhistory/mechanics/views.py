from django.views.generic import TemplateView, DetailView
from mycarhistory.mechanics.models import Mechanic, MechanicForm
from mycarhistory.basemodel import EDITOR_DIALOG_ID
from mycarhistory.basemodel import Action, get_permalink
from mycarhistory.basemodel import BaseUpdateView, BaseCreateView, BaseDeleteView
from django.views.generic import ListView


class MechanicMainView(TemplateView):
    template_name = 'mechanics/mechanics.html'

    def get_context_data(self, **kwargs):
        context = super(MechanicMainView, self).get_context_data(**kwargs)
        context['actions'] = [Action(get_permalink('mechanic-create'), 'Add a mechanic')]
        context['dialog_id'] = EDITOR_DIALOG_ID
        context['sidebar_url'] = get_permalink('mechanic-list')
        return context


class MechanicListView(ListView):
    template_name = 'mechanics/sidebar.html'

    def get_queryset(self):
        return Mechanic.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MechanicListView, self).get_context_data(**kwargs)
        context['mechanics'] = self.get_queryset()
        return context


class MechanicDetailView(DetailView):

    template_name = 'generic_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Mechanic.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(MechanicDetailView, self).get_context_data(**kwargs)
        context['header'] = 'Mechanic'
        context['dialog_id'] = EDITOR_DIALOG_ID
        pk = self.get_queryset()[0].pk
        context['actions'] = [
                Action(get_permalink('mechanic-update', pk), 'Update Details'),
                Action(get_permalink('mechanic-delete', pk), 'Remove Mechanic'),
                ]
        return context


class MechanicCreateView(BaseCreateView):
    form_class = MechanicForm
    model = Mechanic


class MechanicUpdateView(BaseUpdateView):
    form_class = MechanicForm
    model = Mechanic


class MechanicDeleteView(BaseDeleteView):
    model = Mechanic
