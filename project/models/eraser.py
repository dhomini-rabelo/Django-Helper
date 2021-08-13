from main import base_path as bp
from pathlib import Path
from time import sleep
from pprint import pprint
import io

class Eraser:
    def __init__(self, path):
        self.path = path
        
    def _read(self):
        with io.open(self.path, mode='r', encoding='utf-8') as code_file:
            code = code_file.readlines()
            return code
        
    def one_line(self):
        reading = self._read()
        dels = []
        for line in reading:
            try: 
                if line.strip()[0] == '#':
                    dels.append(line)
            except IndexError:
                pass
        for disponsable_line in dels:
            reading.remove(disponsable_line)
        return reading
    
    def initial_lines(self):
        reading = self._read()
        if (len(reading) > 0) and (reading[0][:3] == '"""'):
            for k, line in enumerate(reading[1:]):
                if '"""' in line:
                    end_comment = k
                    reading = reading[end_comment+2: ]
                    break
        return reading 
                    
    
    def construct(self, new_reading: list):
        with io.open(self.path, mode='w', encoding='utf-8') as code_file:
            if len(new_reading) > 0:
                start = 1 if new_reading[0] == '\n' else 0
                for line in new_reading[start:]:
                    code_file.write(line)
            


def delete_comments(path: str):
    rubber = Eraser(path)
    reader1 = rubber.one_line()
    rubber.construct(reader1)
    sleep(0.3)
    reader2 = rubber.initial_lines()
    rubber.construct(reader2)


def delete_comments_by_folder(base_path: str, folder_name: str):
    wp = Path(f'{base_path}/{folder_name}') # work path
    if wp.exists():
        for item in wp.iterdir():
            if item.suffix == '.py':
                print(f'Apagando comentários {item.name}')
                delete_comments(item)

        
        
delete_comments_by_folder(bp, 'conta')
    