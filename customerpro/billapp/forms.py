from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'class-controls'}),
            'bill_amount': forms.NumberInput(attrs={'class': 'class-controls'}),
            'bill_date': forms.DateInput(attrs={'class': 'class-controls'}),
            'payment_mode': forms.Select(attrs={'class': 'class-controls'})
        }


