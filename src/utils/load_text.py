import json
import random
from typing import List, Dict, Any , Union ,Tuple

from .colors import Colors


def load_key_value(nivel: int) -> Tuple[str,str]:
    niveles : List[str] = ['data/nivel_uno.json','data/nivel_dos.json','data/nivel_tres.json']
    key: str  = ''
    valor:str =''

    # Any funciona como comodin
    try:
        if not (1 <= nivel <= len(niveles)):
            raise IndexError(f"Nivel {nivel} fuera de rango. Niveles disponibles: 1 a {len(niveles)}.")

        with open(niveles[nivel-1],'r', encoding='utf-8', errors='ignore') as arhivo:
            data : Union[Dict[str,Any], List[Any]] = json.load(arhivo)
            index:int = random.randint(0,len(data)-1)

            key = data[index].get("palabra")
            valor = data[index].get("descripcion")

            return key, valor
    except FileNotFoundError:
        print(f'{Colors.RED}El archivo no fue encontrado{Colors.ENDC}')

    except json.JSONDecodeError:
        print(f'{Colors.RED}El archivo JSON no es valido {Colors.ENDC}')
