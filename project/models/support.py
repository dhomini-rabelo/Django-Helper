from time import sleep
from pathlib import Path


def response(msg: str, wait=0, entity='Feedback'):
    """
    Função que mostra um feedback ao usuário 
    Args:
        msg (str): feedback que será mostrado
        wait (int, optional): tempo de espera para vários response não sejam executados juntos. Defaults to 0.
        entity (str, optional): "Entidade" que executa  a ação. Defaults to 'Feedback'.
    """
    sleep(wait)
    print(f'{entity} > [ {msg.lower()} ]')
    
    
def assert_path_existence(path: str):
    if not Path(path).exists():
        raise FileNotFoundError(f'A pasta "{path}" não foi encontrada')
    
    
class PathIsAFolderError(Exception):
    pass
    
    
def assert_if_file(path: str):
    if not Path(path).is_file():
        raise PathIsAFolderError(f'"{path}" é o caminho de uma pasta, nesta feature precisamos de um arquivo')
    

def check_null(obj):
    return True if len(obj) > 0 else False
    