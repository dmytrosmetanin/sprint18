from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'end_at', 'plated_end_at')
        labels = {
            'user': "Пользователь библлитеки",
            'book': "Взятая книга",
            'end_at': "Возвращена",
            'plated_end_at': "Когда вернуть"
        }
        exclude = ('end_at', 'plated_end_at')


        # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['authors'].empty_label = 'Выберите одну или несколько книг'