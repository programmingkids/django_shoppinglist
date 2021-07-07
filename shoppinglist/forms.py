from django import forms
from django.forms import ModelForm

from django.contrib.auth import get_user_model

from .models import Category
from .models import Item
from .models import ShoppingList
from .models import ShoppingItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'autofocus' : True}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','price','category']
        widgets = {
            'name' : forms.TextInput(attrs={'autofocus' : True}),
        }


class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name','user']
        widgets = {
            'name' : forms.TextInput(attrs={'autofocus' : True}),
        }


class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['shoppinglist','item','quantity']
        widgets = {
            'shoppinglist' : forms.Select(attrs={'autofocus' : True}),
        }

