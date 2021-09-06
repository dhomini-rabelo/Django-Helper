from django.forms import ModelForm, ValidationError
from pessoa.models import *


class PersonForm(ModelForm):
    class Meta:
      fields = '__all__'
      model = Person
