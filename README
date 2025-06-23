# Wordle-like

Wordle, donde los jugadores intentan adivinar una palabra secreta con un número limitado de intentos, recibiendo pistas sobre la longitud de la palabra y el color de las letras según su corrección.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
.
├── data
│   ├── nivel_dos.json
│   ├── nivel_tres.json
│   └── nivel_uno.json
└── src
    ├── main.py
    └── utils
        ├── colors.py
        ├── __init__.py
        ├── load_text.py
        ├── opciones_game.py
        └── __pycache__
            ├── colors.cpython-311.pyc
            ├── __init__.cpython-311.pyc
            ├── load_text.cpython-311.pyc
            └── opciones_game.cpython-311.pyc
```

### Descripción de Archivos y Directorios:

  * **`data/`**: Este directorio contiene los archivos JSON con las palabras y descripciones para cada nivel del juego.

      * `nivel_uno.json`: Contiene palabras para el Nivel 1.
      * `nivel_dos.json`: Contiene palabras para el Nivel 2.
      * `nivel_tres.json`: Contiene palabras para el Nivel 3.

  * **`src/`**: Contiene el código fuente principal del juego.

      * **`main.py`**: El punto de entrada del juego. Inicia el juego del ahorcado.
      * **`utils/`**: Un paquete que contiene módulos de utilidad para el juego.
          * `colors.py`: Define las clases para los códigos de color ANSI utilizados para colorear la salida de la consola (verde para letras correctas, rojo para incorrectas, amarillo para pistas, etc.).
          * `__init__.py`: Archivo de inicialización del paquete `utils`.
          * `load_text.py`: Contiene la función `load_key_value` que es responsable de cargar una palabra secreta y su descripción de los archivos JSON en el directorio `data` según el nivel elegido. Maneja errores como `FileNotFoundError` y `json.JSONDecodeError`.
          * `opciones_game.py`: Contiene la lógica principal del juego.
              * `NIVELES_DISPONIBLES`: Constante que define el número total de niveles en el juego (3).
              * `NUMERO_DE_INTENTOS`: Constante que define el número de intentos que tiene el jugador para adivinar la palabra (6).
              * `start_game()`: Inicia el flujo del juego, solicitando al jugador que elija un nivel y manejando la entrada inválida. Carga la palabra secreta y la descripción usando `load_key_value`.
              * `comparar_y_colorear_palabras()`: Compara la palabra ingresada por el usuario con la palabra secreta y devuelve una cadena coloreada, donde las letras correctas en la posición correcta son verdes y las incorrectas o fuera de posición son rojas.
              * `game()`: Gestiona la lógica principal del juego, incluyendo el bucle de intentos, la comparación de palabras, la provisión de pistas y la determinación de la victoria o la derrota.
          * `__pycache__/`: Directorio generado automáticamente por Python para almacenar los archivos bytecode compilados (`.pyc`) de los módulos Python.

## Cómo Jugar

1.  **Ejecutar el juego**: Navega hasta el directorio `src` y ejecuta el archivo `main.py`:
    ```bash
    python main.py
    ```
2.  **Seleccionar Nivel**: El juego te pedirá que ingreses el nivel deseado (1, 2 o 3).
3.  **Adivinar la Palabra**: Se te mostrará una pista (descripción) y la longitud de la palabra secreta. Tendrás 6 intentos para adivinarla.
4.  **Retroalimentación de Colores**: Después de cada intento, las letras de tu palabra se colorearán:
      * **Verde**: La letra es correcta y está en la posición correcta.
      * **Rojo**: La letra es incorrecta o no está en la posición correcta.
5.  **Pistas**: Si tu intento tiene una longitud diferente a la palabra secreta, recibirás una pista sobre la longitud correcta.
6.  **Victoria o Derrota**: El juego termina cuando adivinas la palabra (¡Victoria\!) o te quedas sin intentos (¡Derrota\!).

## Requisitos

  * Python 3.x

## Instalación

1.  Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```
2.  Asegúrate de que tus archivos JSON de datos estén en el directorio `data/`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un "issue" o envía un "pull request".