from django.forms import ModelForm
from .models import Investmento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investmento
        fields = '__all__'