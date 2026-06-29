from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    pass

# class BookForm(forms.Form):
#     title = forms.CharField(
#         max_length=100, 
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'})
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'})
#     )
#     price = forms.DecimalField(
#         max_digits=6, 
#         decimal_places=2,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
#     )

#     # Example of custom validation
#     def clean_price(self):
#         price = self.cleaned_data.get('price')
#         if price <= 0:
#             raise forms.ValidationError("Price must be greater than zero.")
#         return price