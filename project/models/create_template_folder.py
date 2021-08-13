from ..main import base_path as bp
from pathlib import Path
import io


#* Function
def create_template_folder(base_path: str, app_name: str):
    if Path(f'{base_path}/{app_name}').exists():
        test_path = Path(f'{base_path}/{app_name}/templates').mkdir()


#* Program
app_name = 'conta'
create_template_folder(bp, app_name)