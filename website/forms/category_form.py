from django.contrib.auth.models import User
from django import forms
from website.models import Category

class CategoryForm(forms.ModelForm):
    '''Category form
    
        Defines the fields for the category add form

        author: Levi Schubert
    '''

    class Meta:
        model = Category
        fields = ('name',)