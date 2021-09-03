from models.eraser import *
from models.project import *
from models.editor import Editor

bp = r'C:\Users\G-fire\OneDrive\Documentos\Django\HELPER' # base_path
project_name = 'HELP'
project = DjangoProject(bp, project_name)


#* APÓS CRIAÇÃO
# delete_comments_by_folder(bp, project_name)
# project.adapt_urls_py()
# project.insert_important_comments()
# project.adapt_settings()