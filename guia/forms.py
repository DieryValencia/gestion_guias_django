from django import forms
from .models import Guia, Recurso, Tematica

class GuiaForm(forms.ModelForm):
    # Rebind del campo tematica para hacerlo opcional
    tematica = forms.ModelChoiceField(
        queryset=Tematica.objects.all(),
        required=False,            # ← ahora no es obligatorio
        label='Temática'
    )
    # Campo extra para texto libre
    nueva_tematica = forms.CharField(
        max_length=100,
        required=False,
        label="O crear nueva temática",
        widget=forms.TextInput(attrs={'placeholder': 'Título de la nueva temática'})
    )

    class Meta:
        model = Guia
        fields = ['programa', 'semana', 'estado', 'tematica']  # nota: 'nueva_tematica' NO va aquí

    def clean(self):
        data = super().clean()
        existe = data.get('tematica')
        nueva  = data.get('nueva_tematica')
        if not existe and not nueva:
            raise forms.ValidationError("Debes seleccionar o escribir una temática.")
        return data

    def save(self, commit=True):
        instancia = super().save(commit=False)
        nueva = self.cleaned_data.get('nueva_tematica')
        if nueva:
            # creamos la nueva y la asignamos
            tem = Tematica.objects.create(titulo=nueva, descripcion='')
            instancia.tematica = tem
        # si no hubo texto nuevo, el select ya estaba en instancia.tematica
        if commit:
            instancia.save()
        return instancia