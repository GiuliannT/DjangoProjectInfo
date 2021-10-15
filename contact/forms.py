from django import forms

class ContactForm(forms.Form):

    name=forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}))
    email=forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email address', 'class':'form-control'}))
    content=forms.CharField(label='Content', required=False, max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Message', 'class':'form-control'}))
    