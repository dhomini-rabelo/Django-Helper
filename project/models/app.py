from pathlib import Path
from .support import *
from .django_class import DjangoBase
import io


class DjangoApp(DjangoBase):
    def __init__(self, base_path: str, app: str):
        self.base_path = self.adapt_path(base_path)
        self.app = self.adapt_path(app)
        self.path = f'{self.base_path}/{self.app}'
        assert_folder_existence(self.path)
            
    def create_templates_folder(self):
        try: 
            Path(f'{self.path}/templates').mkdir()
            response(f'pasta templates foi criada no app {self.app}')
        except FileExistsError:
            response(f'a pasta templates já existe no app {self.app}')
            
    def create_template(self, name_archive: str, extends_archive: str):
        with io.open(f'{self.path}/templates/{name_archive}.html', 'w', encoding='utf-8') as arc:
            arc.write('{% extends ' +  f"'{extends_archive}.html'" + ' %}\n')
            
    def create_tests_folder(self):
        try:
            Path(f'{self.path}/tests').mkdir()
            response(f'pasta tests foi criada  no app {self.app}')
            with io.open(f'{self.path}/tests/__init__.py', 'w', encoding='utf-8') as arc:
                arc.write('# Módulo python')
        except FileExistsError:
            response(f'a pasta tests já existe no app {self.app}')
            
    def create_test_archive(self, test_name: str):
        name = self.adapt_name(test_name)
        with io.open(f'{self.path}/tests/test_{name}', 'w', encoding='utf-8') as arc:
            arc.write('from django.test import TestCase\n')
            
    def create_url_archive(self):
        with io.open(f'{self.path}/urls.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.urls import path\nfrom .views import *\n')
            arc.write('urlpatterns = [\n\n]')
    
    def create_forms_archive(self):
        with io.open(f'{self.path}/forms.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.forms import ModelForm, ValidationError\n')

            
    def create_form(self, model_name: str):
        with io.open(f'{self.path}/forms.py', 'a', encoding='utf-8') as arc:
            arc.write(f'class Form{model_name}(ModelForm):\n')
            arc.write(f"    class Meta:\n      fields='__all__'\n")
            arc.write(f"        model = {model_name}\n")
            
    def import_for_model(self):
        current_import = 'from django.db import models'
        new_import = 'from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, DO_NOTHING, DecimalField, DateField, BooleanField)'
        return (current_import, new_import)

bp = r'C:\Users\G-fire\OneDrive\Documentos\GITHUB\UTILS\Django-Helper\project' # 


            
    