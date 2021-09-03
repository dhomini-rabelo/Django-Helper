from main import base_path as bp
from models.eraser import *
from models.project import *
from models.editor import Editor

project_name = 'COMPANY'
delete_comments_by_folder(bp, project_name)


#* APÓS CRIAÇÃO
# project = DjangoProject(bp, project_name)
# project.adapt_urls_py()
# project.insert_important_comments()
# project.adapt_settings()