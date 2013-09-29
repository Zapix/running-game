# Create your views here.
from django import shortcuts
from django.views import generic as cbv
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from . import forms
from . import models


class RegistrationFormView(cbv.FormView):
    template_name = 'registration/registration_form.html'
    form_class = forms.RegistrationUserForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.is_active = True
        obj.set_password(obj.password)
        obj.save()
        return shortcuts.redirect(reverse('registration_finished'))


class RegistrationFinished(cbv.TemplateView):
    template_name = 'registration/finished.html'


class AccountRedirectView(cbv.View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return shortcuts.redirect(
            reverse(
                'account_profile',
                kwargs={
                    'pk': request.user.pk
                }
            )
        )


class AccountProfileView(cbv.DetailView):
    model = models.User
    template_name = 'accounts/account_detail.html'
