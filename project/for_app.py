from main import base_path as bp
from models.app import DjangoApp
from models.editor import Editor

app_name = 'test'

app = DjangoApp(bp, app_name)


#* APÓS CRIAÇÃO
# app.create_url_archive()
# app.create_forms_archive()
# app.create_templates_folder()
# app.create_parts_folder()
# app.create_tests_folder()

#* criando testes
# tests = ['models', 'views', 'forms']
# for test in tests:
#     app.create_test_archive(test)


#* OCASIONALMENTE

#* criar template
# app.create_template('index', 'base')

#* criar form
# model = 'Model'
# app.create_form(model)

