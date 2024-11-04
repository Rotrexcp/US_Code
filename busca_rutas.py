import os

def buscar_archivo(nombre_archivo, directorio_base="."):
    for root, _, files in os.walk(directorio_base):
        if nombre_archivo in files:
            return os.path.abspath(os.path.join(root, nombre_archivo))
    return None

# Ejemplo de uso:
nombre_archivo = "frecuencias_nombres.csv"  # El nombre del archivo que quieres encontrar
ruta = buscar_archivo(nombre_archivo)

if ruta:
    print(f"Archivo encontrado en: {ruta}")
else:
    print("Archivo no encontrado.")
