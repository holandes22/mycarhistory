from django.db import models
from django.db.models import permalink
from django.views.generic import CreateView, UpdateView

EDITOR_FORM_ID = 'editor-form'
EDITOR_DIALOG_ID = 'editor-dialog'
EDITOR_FORM_SAVE_EVENT = 'editor-form-save'
DATE_FORMAT = '%m/%d/%Y'


def make_custom_field_callback(field):
    """
    Callback to make field customization. This is useful to midifiy the elements of a form, for example
    a custom class to a date field so it can be identified by Jquery UI datepicker in the template
    """
    formfield = field.formfield()
    if formfield:
        formfield.widget.attrs.update({'title': field.help_text})
    if isinstance(field, models.DateField):
        formfield.widget.format = DATE_FORMAT
        formfield.widget.attrs.update({'class': 'datePicker', 'readonly': 'true'})
    return formfield


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

    def get_model_attrs(self, filter_fields=['id', 'pk', 'user']):
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
        context['loader'] = self.get_loader()
        context['loader_args'] = ",".join(self.get_loader_args())
        return context

    def get_submit_url(self):
        raise NotImplementedError()

    def get_loader(self):
        raise NotImplementedError()

    def get_loader_args(self):
        raise NotImplementedError()


class BaseUpdateView(EditorMixin, UpdateView):

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_submit_url(self):
        return get_permalink('{0}-update'.format(self.model.__name__.lower()), self.get_object().pk)

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        return self._update_context(context)

    def get_loader(self):
        return 'loadUpdateDialog'

    def get_loader_args(self):
        return ['#{0}-details-id-{1}'.format(self.model.__name__.lower(), self.get_object().pk)]


class BaseCreateView(EditorMixin, CreateView):

    def get_submit_url(self):
        return get_permalink('{0}-create'.format(self.model.__name__.lower()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        return self._update_context(context)

    def get_loader(self):
        return 'loadCreateDialog'

    def get_loader_args(self):
        return [self.get_success_url()]
