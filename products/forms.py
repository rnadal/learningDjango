from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Product's title"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "test-class",
        "placeholder": "Product's description here",
        "rows": 15,
        "cols": 40
    }))
    price = forms.DecimalField(initial=0.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Product's title"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "test-class",
        "placeholder": "Product's description here",
        "rows": 15,
        "cols": 40
    }))
    price = forms.DecimalField(initial=0.99)