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
            'first_name': 'Имя',
            'middle_name': 'Отчество',
            'last_name': 'Фамилия',
            'email': 'Почта',
            'password': 'Пароль',
            'role': 'Статус'
        }

        # def __init__(self, *args, **kwargs):
        #     super(UserForm, self).__init__(*args, **kwargs)
        #     self.fields['role'].empty_label = 'Выберите'