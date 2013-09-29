# -*- coding: utf-8 -*-
from django import forms

from . import models


class RegistrationUserForm(forms.ModelForm):
    re_password = forms.CharField(
        max_length=255,
        label='Re password',
    )

    class Meta:
        model = models.User
        fields = ('username', 'password', 're_password')

    def clean_re_password(self):
        """
        Checks the password and re_password are the same
        :rtype: str
        """
        try:
            password = self.cleaned_data['password']
        except KeyError:
            raise forms.ValidationError('Password should be entered')
        try:
            re_password = self.cleaned_data['password']
        except KeyError:
            raise forms.ValidationError('re password should be entered')

        if password != re_password:
            raise forms.ValidationError(
                'password and re-password should be the same'
            )
        return password
