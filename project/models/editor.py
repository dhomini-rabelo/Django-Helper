from pathlib import Path
from .support import *
from .django_class import DjangoBase
import io


class Editor(DjangoBase):
    def __init__(self, base_path: str, archive_path: str):
        self.base_path = self.adapt_path(base_path)
        self.archive_path = self.adapt_path(archive_path)
        self.path = f'{self.base_path}/{self.archive_path}'
        assert_file_existence(self.path)
        self.reading = self.read(self.path)
        
    def replace_code(self, current: str, new: str):
        for line in self.reading:
            if line.startswith(current):
                pos = self.reading.index(line) # position
                self.reading[pos] = f'{new}\n'
                break
        
    def get_line(self, code_line: str):
        for line in self.reading:
            if line.startswith(code_line):
                pos = self.reading.index(line) # position
                return pos
        return None
    
    def add_in_line(self, line_code:str, new: str):
        number_line = self.get_line(line_code)
        if number_line:
            current_line = self.reading[number_line][:-2]
            self.reading[number_line] = f'{current_line}{new}\n'
        
        
    def insert_code(self, line: int, new: str):
        self.reading.insert(line, f'{new}\n')
        
    def insert_comment(self, line:int, comment: str):
        self.reading.insert(line, f'# {comment}\n')
        
    def update(self):
        if check_null(self.reading):
            return
        with io.open(self.path, mode='w', encoding='utf-8') as code_file:
            start = 1 if self.reading[0] == '\n' else 0
            for line in self.reading[start:]:
                code_file.write(line)