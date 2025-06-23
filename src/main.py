from utils.opciones_game import start_game
from utils.colors import Colors

if __name__ == "__main__":
    print(f"{Colors.CYAN + Colors.BOLD}¡Bienvenido al Juego del Ahorcado!{Colors.ENDC}")
    start_game()
    print(f"{Colors.GREEN}Gracias por jugar al Ahorcado.{Colors.ENDC}")    

