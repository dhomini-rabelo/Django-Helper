from pathlib import Path
from support import *
from django import Django
import io


class DjangoApp(Django):
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
            
    def create_tests_folder(self):
        try:
            Path(f'{self.path}/tests').mkdir()
            response(f'pasta templates foi criada  no app {self.app}')
        except FileExistsError:
            response(f'a pasta tests já existe no app {self.app}')
            
    def create_url_archive(self):
        with io.open(f'{self.path}/urls.py', 'w', encoding='utf-8') as url:
            url.write('from django.urls import path\nfrom .views import *\n')
            url.write('urlpatterns = [\n\n]')
            
    def import_for_model(self):
        current_import = 'from django.db import models'
        new_import = 'from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, DO_NOTHING, DecimalField, DateField, BooleanField)'
        return (current_import, new_import)

bp = r'C:\Users\G-fire\OneDrive\Documentos\GITHUB\UTILS\Django-Helper\project' # base path
# app = DjangoApp(bp, 'test')
# app.create_url_archive()


            
    