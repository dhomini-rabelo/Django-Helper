from ..main import base_path as bp
from pathlib import Path
from time import sleep
import io


#* Functions

class FolderNotFound(Exception):
    pass

def create_foder_tests(base_path: str, app_name: str):
    if not Path(f'{base_path}/{app_name}').exists():
        raise FolderNotFound(f'{base_path}/{app_name} não foi encontrado')
    if not Path(f'{base_path}/{app_name}/tests').exists():
        test_path = Path(f'{base_path}/{app_name}/tests').mkdir()
    
    
def create_test(base_path: str, app_name: str, test_name: str):
    if not Path(f'{base_path}/{app_name}/tests').exists():
        raise FolderNotFound(f'{base_path}/{app_name}/tests não foi encontrado')
    with io.open(f'{base_path}/{app_name}/tests/test_{test_name}.py', 'w', encoding='utf-8') as models_test:
        models_test.write('from django.test import TestCase\n')

      
#* PROGRAM

tests = ['models', 'views', 'forms']
app_name = 'conta'

create_foder_tests(bp, app_name)
for test in tests:
    sleep(0.3)
    create_test(bp, app_name, test)