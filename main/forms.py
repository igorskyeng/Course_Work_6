from django import forms
from main.models import ClientService, MessageMailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CleanNameProductMixin:
    def clean_name_product(self):
        cleaned_data = self.cleaned_data['name_product']
        list_banned = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for l_b in list_banned:
            if l_b in cleaned_data:
                raise forms.ValidationError('Запрещенное слово!')

        return cleaned_data


class ClientAddForm(StyleFormMixin, CleanNameProductMixin, forms.ModelForm):

    class Meta:
        model = ClientService
        fields = ('email', 'name', 'comments')


class MessageAddForm(StyleFormMixin, CleanNameProductMixin, forms.ModelForm):

    class Meta:
        model = MessageMailing
        fields = ('subject_line', 'body')


class ClientForm(StyleFormMixin, CleanNameProductMixin, forms.ModelForm):

    class Meta:
        model = ClientService
        fields = ('email', 'name', 'comments')
