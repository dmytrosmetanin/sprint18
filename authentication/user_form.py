from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'password',
            'role'
            )
        labels = {
            'first_name': 'Name',
            'middle_name': 'Patronymic name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
            'role': 'Role'
        }

        # def __init__(self, *args, **kwargs):
        #     super(UserForm, self).__init__(*args, **kwargs)
        #     self.fields['role'].empty_label = 'Выберите'