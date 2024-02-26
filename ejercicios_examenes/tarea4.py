import os
import logging
import psutil

# Directorio de logs
directorio_logs = '/home/pruevaa/logs/'

# Verificar si el directorio de logs existe, si no existe, crearlo
if not os.path.exists(directorio_logs):
    os.makedirs(directorio_logs)


def configurar_logger():
    # Crear el logger
    logger = logging.getLogger("espacio_logger")
    logger.setLevel(logging.DEBUG)

    # Crear el formateador
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Crear el manejador para escribir en el archivo
    archivo_log = '/home/pruevaa/logs/espacio.log'
    file_handler = logging.FileHandler(archivo_log)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Agregar el manejador al logger
    logger.addHandler(file_handler)

    return logger

def analizar_espacio():
    # Obtener el espacio en disco para la raíz "/"
    espacio_raiz = psutil.disk_usage('/')
    espacio_ocupado_porcentaje = espacio_raiz.percent

    # Configurar el logger
    logger = configurar_logger()

    # Determinar el nivel de mensaje según el espacio ocupado
    if espacio_ocupado_porcentaje > 80:
        logger.error(f"Espacio ocupado en la raíz (/) es mayor que 80%: {espacio_ocupado_porcentaje}%")
    elif espacio_ocupado_porcentaje > 60:
        logger.warning(f"Espacio ocupado en la raíz (/) es mayor que 60% y menor que 80%: {espacio_ocupado_porcentaje}%")
    elif espacio_ocupado_porcentaje > 0:
        logger.info(f"Espacio ocupado en la raíz (/) es mayor que 0% y menor que 60%: {espacio_ocupado_porcentaje}%")

def main():
    analizar_espacio()

if __name__ == "__main__":
    main()