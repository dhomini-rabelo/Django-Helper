from pathlib import Path
from support import *
import io


class DjangoApp:
    def __init__(self, base_path, app):
        self.base_path = self.adapt_path(base_path)
        self.app = self.adapt_path(app)
        self.path = f'{self.base_path}/{self.app}'
        assert_path_existence(self.path)
        
    @staticmethod
    def adapt_path(path: str):
        backslash = '\*'[0]
        return path.replace(backslash, '/')
            
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

bp = r'C:\Users\G-fire\OneDrive\Documentos\GITHUB\UTILS\Django-Helper\project' # base path
# app = DjangoApp(bp, 'test')
# app.create_url_archive()


            
    