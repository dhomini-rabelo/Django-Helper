from time import sleep

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