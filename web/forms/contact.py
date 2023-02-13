from captcha.fields import CaptchaField
from django import forms

from web.models import Contact


class ContactWithCaptchaForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Contact
        exclude = [
            "id",
        ]
