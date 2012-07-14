from django.db import models
from django.db.models import permalink
from django.views.generic import CreateView, UpdateView

EDITOR_FORM_ID = 'editor-form'
EDITOR_DIALOG_ID = 'editor-dialog'
EDITOR_FORM_SAVE_EVENT = 'editor-form-save'


@permalink
def get_permalink(name, *args):
    return ('{name}'.format(**locals()), args)


class Action(object):

    def __init__(self, url, title):
        self.url = url
        self.title = title


class BaseModel(models.Model):

    class Meta:
        abstract = True

    def get_model_attrs(self, filter_fields=['id', 'pk']):
        for field in self._meta.fields:
            if field.name not in filter_fields:
                if field.choices:
                    yield field.name, getattr(self, 'get_%s_display' % field.name)
                else:
                    yield field.name, getattr(self, field.name)


class EditorMixin(object):
    template_name = 'editor.html'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', None)

    def _update_context(self, context):
        context['submit_url'] = self.get_submit_url()
        context['editor_form_id'] = EDITOR_FORM_ID
        context['editor_dialog_id'] = EDITOR_DIALOG_ID
        context['redirect_to'] = self.get_success_url()
        return context

    def get_submit_url(self):
        raise NotImplementedError()


class BaseUpdateView(EditorMixin, UpdateView):

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_submit_url(self):
        return get_permalink('{0}-update'.format(self.model.__name__.lower()), self.get_object().pk)

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        return self._update_context(context)


class BaseCreateView(EditorMixin, CreateView):

    def get_submit_url(self):
        return get_permalink('{0}-create'.format(self.model.__name__.lower()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        return self._update_context(context)
