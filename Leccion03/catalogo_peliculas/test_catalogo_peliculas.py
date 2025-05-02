from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar película')
        print('2. Listar películas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Selecciona una opción (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
        elif opcion == 4:
            print('Saliendo...')
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa...')





