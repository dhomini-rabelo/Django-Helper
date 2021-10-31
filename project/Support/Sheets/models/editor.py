from support import *
from django_class import Base
from collections.abc import Mapping
from random import randint
from time import sleep
import io




class Editor(Base):
    
    def __init__(self, base_path: str, archive_path: str):
        self.base_path = self.adapt_path(base_path)
        self.archive_path = self.adapt_path(archive_path)
        self.path = f'{self.base_path}/{self.archive_path}'
        assert_file_existence(self.path)
        self.reading = self.read(self.path)
            
    def _get_line_position(self, code_line: str) -> int:
        for position, line in enumerate(self.reading):
            if line.startswith(code_line):
                return position
        raise NotFoundError('Line not found')
        
    def replace_line(self, current: Mapping[str, int], new: str):
        if isinstance(current, str):
            line_number = self._get_line_position(current)
            self.replace_line(line_number, new)
        elif isinstance(current, int):
            self.reading[current] = f'{new}\n'
            self._update(self.reading)
        
    def add_in_line(self, current: Mapping[str, int], new: str):
        if isinstance(current, str):
            line_number = self._get_line_position(current)
            current_line = self.reading[line_number][:-1]
            self.replace_line(line_number, f'{current_line}{new}\n')
        elif isinstance(current, int):
            current_line = self.reading[current][:-1]
            self.replace_line(current, f'{current_line}{new}\n')
        
    def insert_code(self, line_code: Mapping[str, int], new: str):
        if isinstance(line_code, str):
            line_number = self._get_line_position(line_code)
            self.reading.insert(line_number + 1, f'{new}\n')
            self._update(self.reading)
        elif isinstance(line_code, int):
            self.reading.insert(line_code + 1, f'{new}\n')
            self._update(self.reading)

    def delete_line(self, line_code: Mapping[str, int]):
        if isinstance(line_code, str):
            line_number = self._get_line_position(line_code)
            del self.reading[line_number]
            self._update(self.reading)
        elif isinstance(line_code, int):
            del self.reading[line_code]
            self._update(self.reading)
                    
    def _update(self, reading: list):
        sleep(0.5)
        with io.open(self.path, mode='w', encoding='utf-8') as code_file:
            start = 1 if reading[0] == '\n' else 0
            for line in reading[start:]:
                code_file.write(line)
        self.reading = reading

