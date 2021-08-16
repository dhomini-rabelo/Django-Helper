from .support import *
import io


class DjangoBase:
    
    
    @staticmethod
    def adapt_path(path: str):
        backslash = '\*'[0]
        return path.replace(backslash, '/')
    
    @staticmethod
    def adapt_name(archive_name: str):
        if archive_name.endswith('.py'):
            return archive_name
        return f'{archive_name}.py'
    
    def read(self, archive: str):
        path = f'{self.adapt_name(archive)}.py'
        assert_file_existence(path)
        with io.open(path, mode='r', encoding='utf-8') as code_file:
            code = code_file.readlines()
            return code