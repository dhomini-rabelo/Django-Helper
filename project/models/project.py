from support import *
from django import Django
import io


class DjangoProject(Django):
    def __init__(self, base_path: str, project: str):
        self.base_path = self.adapt_path(base_path)
        self.project = self.adapt_path(project)
        self.path = f'{self.base_path}/{self.project}'
        assert_folder_existence(self.path)

    def settings_replaces(self):
        replaces = [
            ('', ''),
            ('', ''),
        ]

    