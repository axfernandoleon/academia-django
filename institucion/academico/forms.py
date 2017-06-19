# -*- encoding: utf-8 -*-
from django import forms
from academico.models import * 


class ParaleloPeriodoForm(forms.Form):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all(), label="", initial='', widget=forms.Select(), required=True)

# class CombustiblesProvinciaForm(forms.Form):
#     provincia = forms.ModelChoiceField(queryset=Provincias.objects.all(), label="", initial='', widget=forms.Select(), required=True)
#     combustible = forms.ModelChoiceField(queryset=Combustibles.objects.all(), label="", initial='', widget=forms.Select(), required=True)
