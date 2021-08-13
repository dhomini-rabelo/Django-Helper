from main import base_path as bp
import io


#* Function
def create_url_archive(base_path: str, app_name: str):
    with io.open(f'{base_path}/{app_name}/urls.py', 'w', encoding='utf-8') as url:
        url.write('from django.urls import path\nfrom .views import *\n')
        url.write('urlpatterns = [\n\n]')


#* Program
app_name = 'conta'
create_url_archive(bp, app_name)
