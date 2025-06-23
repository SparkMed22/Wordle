from .colors import Colors
from .load_text import load_key_value


NIVELES_DISPONIBLES: int = 3 
NUMERO_DE_INTENTOS: int = 6


def start_game():
    print(f'{Colors.BLUE}El juego tiene {NIVELES_DISPONIBLES} niveles.{Colors.ENDC}')
    
    nivel_elegido: int = 0
    
    while True:
        try:
            nivel_input = input(f"{Colors.CYAN}Ingrese el nivel deseado (1 - {NIVELES_DISPONIBLES}): {Colors.ENDC}")
            nivel_elegido = int(nivel_input)

            if 1 <= nivel_elegido <= NIVELES_DISPONIBLES:
                break
            else:
                print(f"{Colors.YELLOW}Por favor, ingresa un número entre 1 y {NIVELES_DISPONIBLES}.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.RED}Entrada inválida. Por favor, ingresa un número.{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.RED}Ocurrió un error inesperado al leer el nivel: {e}{Colors.ENDC}")


    palabra_secreta, descripcion = load_key_value(nivel_elegido)
    print(f'Pista:\n\t {descripcion}\n')
    game(palabra_secreta.lower())



def comparar_y_colorear_palabras(palabra_secreta: str, palabra_ingresada: str) -> str:
    palabra_secreta_upper = palabra_secreta.lower()
    palabra_ingresada_upper = palabra_ingresada.lower()

    resultado_coloreado = []
    
    for i in range(len(palabra_ingresada_upper)):
        letra_ingresada = palabra_ingresada_upper[i]

        if i < len(palabra_secreta_upper):
            letra_secreta = palabra_secreta_upper[i]

            if letra_ingresada == letra_secreta:
                resultado_coloreado.append(Colors.GREEN + letra_ingresada + Colors.ENDC)
            else:
                resultado_coloreado.append(Colors.RED + letra_ingresada + Colors.ENDC)
        else: 
            resultado_coloreado.append(Colors.RED + letra_ingresada + Colors.ENDC)
            
    return "".join(resultado_coloreado)



def game(palabra_secreta: str):
    
     
    print(f"{Colors.YELLOW}La palabra secreta tiene {len(palabra_secreta)} letras.{Colors.ENDC}")
    print(f"{Colors.YELLOW}Tienes {NUMERO_DE_INTENTOS} intentos para adivinarla.{Colors.ENDC}\n")

    for i in range(1, NUMERO_DE_INTENTOS + 1): # Bucle para los intentos
        print(f"{Colors.BOLD}--- Intento {i}/{NUMERO_DE_INTENTOS} ---{Colors.ENDC}")
        
        intento_usuario = input(f'{Colors.CYAN}Ingrese la palabra: {Colors.ENDC}').lower()

        if intento_usuario == palabra_secreta:
            print(f'\n{Colors.GREEN}{Colors.BOLD}¡VICTORIA! ¡Has adivinado la palabra!{Colors.ENDC}')
            print(f'{Colors.GREEN}La palabra era: {palabra_secreta}{Colors.ENDC}\n')
            return

        print(f"Tu intento: {comparar_y_colorear_palabras(palabra_secreta, intento_usuario)}")
        
        if len(intento_usuario) != len(palabra_secreta):
            print(f"{Colors.YELLOW}Pista: La palabra secreta tiene {len(palabra_secreta)} letras.{Colors.ENDC}")

        print(f"{Colors.RED}No es la palabra correcta.{Colors.ENDC}\n")

    print(f"{Colors.RED}{Colors.BOLD}¡HAS PERDIDO! Te quedaste sin intentos.{Colors.ENDC}")
    print(f"{Colors.BLUE}La palabra secreta era: {palabra_secreta}{Colors.ENDC}\n")
