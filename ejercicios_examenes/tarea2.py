import psutil
    # Obtener todas las particiones del sistema
particiones = psutil.disk_partitions()

    # Iterar sobre cada partición
for particion in particiones:
    try:
        # Obtener el uso de disco para la partición
        uso_disco = psutil.disk_usage(particion.mountpoint)
        # Calcular el porcentaje de espacio ocupado
        porcentaje_uso = uso_disco.percent
        # Mostrar el nombre de la partición y el porcentaje de uso
        print(f"{particion.device} {porcentaje_uso:.1f}%")
    except Exception as e:
            print(f"Error con la información de la partición {particion.device}: {str(e)}")