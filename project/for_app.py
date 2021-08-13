from main import base_path as bp
from models.create_template_folder import *
from models.create_test_folder import *
from models.create_url_archive import *
from models.eraser import *

app_name = 'app_name'

delete_comments_by_folder(bp, app_name)

create_template_folder(bp, app_name)

tests = ['models', 'views', 'forms']
create_foder_tests(bp, app_name)
for test in tests:
    sleep(0.3)
    create_test(bp, app_name, test)

create_url_archive(bp, app_name)
