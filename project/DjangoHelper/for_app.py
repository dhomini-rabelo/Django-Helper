from models.eraser import delete_comments_by_folder
from .for_project import project_name
from main import base_path as bp
from models.app import DjangoApp

app_name = 'empresa'
app = DjangoApp(bp, app_name)


#* CRIAR TESTES
# tests = ['models', 'views', 'forms']
# for test in tests:
#     app.create_test_archive(f'{app_name}/{test}')


#* CRIAR FORMS
# app.add_form('model_name')

#* REGISTRAR ADMIN
# app.register_admin('model')

#* REGISTRAR VIEW
# app.register_admin('model', logged=False)

#* APÓS CRIAÇÃO
# app.create_templates_folder(app_name)
# app.create_url_archive()
# app.create_forms_archive()
# app.import_for_model()
# app.register_app(project_name)
# app.config_app()
