from pathlib import Path
from support import *

class DjangoApp:
    def __init__(self, base_path, app_name):
        self.base_path = self.adapt_path(base_path)
        self.app = self.adapt_path(app_name)
        self.path = f'{self.base_path}/{self.app_name}'
        if not (self.path).exists():
            raise FileNotFoundError(f'A pasta "{self.path}" não foi encontrada')
        
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

            


            
    