from django import forms
from .models import Order, Book

class OrderForm(forms.ModelForm):
    plated_end_at = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()
        self.fields['book'].label_from_instance = lambda obj: obj.name

    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
        }
