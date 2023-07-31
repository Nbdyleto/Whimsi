from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=254)
    phone = forms.CharField(label='Telefone', max_length=11)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
    agree_privacy = forms.BooleanField(label='Estou de acordo com a política de privacidade')
