from django import forms
from .models import Localrepuestos, Localcomida
class LocalesComidaForm(forms.ModelForm):
    class Meta:
        model = Localcomida
        fields = "__all__"
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({"class": "form-control"})
class LocalesRepuestosForm(forms.ModelForm):
    class Meta:
        model = Localrepuestos
        fields = "__all__"
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({"class": "form-control"})
