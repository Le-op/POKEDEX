# Importar la librería requests para hacer solicitudes HTTP
import requests

# Importar la librería json para trabajar con archivos JSON
import json

# Importar la librería os para trabajar con el sistema de archivos
import os

def obtener_pokemon(nombre):
    # Construir la URL para obtener la información del Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"

    # Realizar una solicitud GET a la URL y obtener la respuesta
    respuesta = requests.get(url)

    # Verificar si la respuesta fue exitosa (200 OK)
    if respuesta.status_code != 200:
        # Si no fue exitosa, mostrar un mensaje de error
        print("Pokémon no encontrado. Por favor, verifica el nombre.")
        return

    # Obtener la información del Pokémon en formato JSON
    datos = respuesta.json()

    # Crear un diccionario para almacenar la información del Pokémon
    info_pokemon = {
        "nombre": datos['name'],  # Nombre del Pokémon
        "peso": datos['weight'],  # Peso del Pokémon
        "altura": datos['height'],  # Altura del Pokémon
        "movimientos": [mov['move']['name'] for mov in datos['moves']],  # Movimientos del Pokémon
        "habilidades": [hab['ability']['name'] for hab in datos['abilities']],  # Habilidades del Pokémon
        "tipos": [tipo['type']['name'] for tipo in datos['types']],  # Tipos del Pokémon
        "imagen": datos['sprites']['front_default']  # Imagen del Pokémon
    }

    # Mostrar la información del Pokémon
    print(f"Nombre: {info_pokemon['nombre']}")
    print(f"Peso: {info_pokemon['peso']}")
    print(f"Altura: {info_pokemon['altura']}")
    print(f"Movimientos: {', '.join(info_pokemon['movimientos'])}")
    print(f"Habilidades: {', '.join(info_pokemon['habilidades'])}")
    print(f"Tipos: {', '.join(info_pokemon['tipos'])}")
    print(f"Imagen: {info_pokemon['imagen']}")

    # Crear una carpeta llamada "pokedex" si no existe
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    # Guardar la información del Pokémon en un archivo JSON
    with open(f'pokedex/{info_pokemon["nombre"]}.json', 'w') as archivo:
        json.dump(info_pokemon, archivo, indent=4)
    print(f"Información guardada en 'pokedex/{info_pokemon['nombre']}.json'.")

if __name__ == "__main__":
    # Pedir al usuario que introduzca el nombre de un Pokémon
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    obtener_pokemon(nombre_pokemon)