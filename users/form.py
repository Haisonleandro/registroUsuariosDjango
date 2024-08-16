form django import forms
form .models import persona


class personaForm(forms.ModelForm):

    class Meta:
        model = persona
        fields = '__all__'
