from django import forms
from .models import Review, User
from django.contrib.auth.forms import UserCreationForm

class ReviewForm (forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['rating', 'completed', 'review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'review-area'})
        }

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        label='Nome Completo'
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirme sua Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirme sua Senha'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})