from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'end_at', 'plated_end_at')
        labels = {
            'user': "User",
            'book': "Borrowed book",
            'end_at': "Given back",
            'plated_end_at': "Return by date"
        }
        exclude = ('end_at', 'plated_end_at')


        # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['authors'].empty_label = 'Выберите одну или несколько книг'