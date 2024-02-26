import os

def crear_carpetas_y_ficheros():
    # Iterar 5 veces para crear 5 carpetas
    for i in range(1, 6):
        nombre_carpeta = f"folder{i}"
        # Crear carpeta si no existe
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta)
        # Crear 10 ficheros dentro de cada carpeta
        for j in range(1, 11):
            nombre_fichero = f"fichero{j}.txt"
            contenido = f"Este es el contenido del fichero {j}\n"
            with open(os.path.join(nombre_carpeta, nombre_fichero), 'w') as f:
                f.write(contenido)

def main():
    # Ejecutar la función para crear carpetas y ficheros
    crear_carpetas_y_ficheros()
    print("Creación de carpetas y ficheros completada.")

if __name__ == "__main__":
    main()