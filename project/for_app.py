from main import base_path as bp
from models.app import DjangoApp

app_name = 'test'

app = DjangoApp(bp, app_name)

#* Após criação
app.create_url_archive()
app.create_forms_archive()
app.create_templates_folder()
app.create_tests_folder()

#* Criando testes
tests = ['models', 'views', 'forms']
for test in tests:
    app.create_test_archive(test)

#* Ocasionalmente
# app.create_template('index', 'base')
# app.create_form(model_name='Test')