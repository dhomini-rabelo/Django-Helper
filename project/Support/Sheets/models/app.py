from .django_class import DjangoBase
from .editor import Editor
from pathlib import Path
from .support import *
import io


class DjangoApp(DjangoBase):
    def __init__(self, base_path: str, app: str):
        self.base_path = self.adapt_path(base_path)
        self.app = self.adapt_path(app)
        self.path = f'{self.base_path}/{self.app}'
        assert_folder_existence(self.path)
        self.response = lambda message: response(message, app)
            
    def create_py_folder(self, folder_path):
        path = f'{self.base_path}/{folder_path}'
        Path(path).mkdir()
        sleep(0.5)
        with io.open(f'{path}/__init__.py', 'w') as file:
            pass
        
    def create_py_archive(self, archive_path):
        path = f'{self.base_path}/{self.adapt_pyname(archive_path)}'
        with io.open(path, 'w') as file:
            pass
        
    def create_archive(self, archive_path):
        path = f'{self.base_path}/{archive_path}'
        with io.open(path, 'w') as file:
            pass

    def create_templates_folder(self, name_space: str=''):
        try: 
            Path(f'{self.path}/templates').mkdir()
            sleep(0.3)
            Path(f'{self.path}/templates/{name_space}').mkdir()
            self.response(f'pasta templates foi criada')
        except FileExistsError:
            self.response(f'a pasta templates já existe')
            
    def create_test_archive(self, test_name: str):
        name = f'test_{self.adapt_pyname(test_name)}'
        with io.open(f'{self.base_path}/Support/code/tests/{name}', 'w', encoding='utf-8') as arc:
            arc.write('from django.test import TestCase\n')
            self.response(f'Criando {name} na pasta tests')
            
    def create_url_archive(self):
        with io.open(f'{self.path}/urls.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.urls import path\nfrom .views import *\n')
            arc.write(f'\nurlpatterns = [\n{sp(4)}path(),\n]\n')
            self.response(f'arquivo urls.py criado')
    
    def create_forms_archive(self):
        with io.open(f'{self.base_path}/Support/code/forms/{self.app}.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.forms import ModelForm, ValidationError\n')
            arc.write(f'from {self.app}.models import *\n')
            self.response('arquivo form criado')

    def add_form(self, model_name: str):
        path = f'{self.base_path}/Support/code/forms'
        editor = Editor(path, f'{self.app}.py')
        form_script = [
            f"class {model_name.title()}Form(ModelForm):",
            "    class Meta:\n", f"{sp(8)}fields = '__all__'\n",
            f"{sp(8)}model = {model_name}"
        ]
        editor.add_in_end(form_script)
        self.response(f'criando form para {model_name}')
            
    def import_for_model(self):
        editor = Editor(self.path, 'models.py')
        current_import = 'from django.db import models'
        new_import = 'from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)'
        editor.replace_code(current_import, new_import) # new_reading
        self.response(f'import do model foi editado')
        
    def config_app(self):
        editor = Editor(self.path, '__init__.py')
        new_import = [
            "from django.apps import AppConfig", f"\n\nclass {self.app.title()}Config(AppConfig):",
            f"{sp(4)}default_auto_field = 'django.db.models.BigAutoField'", f"{sp(4)}name = '{self.app}'"
        ]
        editor.insert_code(0, new_import) # new_reading
        self.response('criada a classe app config')


    def register_app(self, project_name: str):
        editor  = Editor(self.base_path, f'{project_name}/settings.py')
        editor.insert_code('    # My apps', f"    '{self.app}.{self.app.title()}Config',")
        self.response('app foi registrado')

    def register_admin(self, model_name: str):
        editor  = Editor(self.path, f'admin.py')
        model = model_name.title()
        admin_class = [
            f"\n\n@admin.register({model})\nclass {model}Admin(admin.ModelAdmin):",
            "    list_display = ''", "    list_display_links = '',"
        ]
        editor.add_in_end(admin_class)
        self.response(f'class admin para {model_name} criada com sucesso')
        
    def create_view(self, name_view, logged=True):
        editor  = Editor(self.path, f'views.py')
        editor.read(editor.path)
        login = '@login_required' if logged else ''
        new_view = [
            f"{login}def {name_view}(request):", "    # initial flow", "    context = dict()",
            "    # main flow", "    # endflow",
            f"    return render(request, 'apps/{self.app}/{name_view}.html', context)"
        ]
        editor.add_in_end(new_view)
        self.response(f'view {name_view} criada')
        
    def create_abstract_user_model(self):
        editor = Editor(self.path, 'models.py')
        imports =  [
            "from django.contrib.auth.models import AbstractUser", "from django.utils.safestring import mark_safe",
            "from django.utils import timezone"
        ]
        abstract_user_class = [
            '\n\nclass User(AbstractUser):', 
            "    photo = ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, default='images/user.jpg')",
            "    def __str__(self):", f"{sp(8)}return self.username", "\n\n    @mark_safe", "    def icon(self):",
            f"""{sp(8)}return f'<a href="/media/{self.photo}" target="_blank"><img src="/media/{self.photo}" style="width: 35px; height: 25px;"></a>"""
        ]
        editor.add_in_start(imports)
        editor.add_in_end(abstract_user_class)
        self.response('Criado modelo padrão de usuário')

    def register_abstract_user(self, project_name):
        editor  = Editor(self.base_path, f'{project_name}/settings.py')
        editor.add_in_end(f"\nAUTH_USER_MODEL = 'accounts.User'")
        self.response('Registrado modelo padrão de usuário')
        
            
