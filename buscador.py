import os

def buscar_palabra_en_archivos(directorio, palabra):
    archivos_encontrados = []

    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)
            try:
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        lineas = f.readlines()
                except UnicodeDecodeError:
                    with open(ruta_archivo, 'r', encoding='latin-1') as f:
                        lineas = f.readlines()
                
                for numero_linea, linea in enumerate(lineas, start=1):
                    if palabra in linea:
                        archivos_encontrados.append((ruta_archivo, numero_linea, linea.strip()))
            except Exception as e:
                print(f"No se pudo leer el archivo {ruta_archivo}: {e}")

    return archivos_encontrados

if __name__ == "__main__":
    while True:
        directorio = os.path.dirname(os.path.abspath(__file__))
        palabra = input("Introduce la palabra a buscar: ")
        archivos = buscar_palabra_en_archivos(directorio, palabra)

        if archivos:
            print(f"La palabra '{palabra}' se encontró en los siguientes archivos:")
            for archivo, numero_linea, linea in archivos:
                print(f"Archivo: ({archivo})\n Línea: (({numero_linea}))\n Contenido: ((({linea})))\n\n")
        else:
            print(f"No se encontró la palabra '{palabra}' en ningún archivo.")
        
        while True:
            continuar = input("¿Desea continuar? [Y/N]: ").strip().lower()
            if continuar in ['y', 'n']:
                break
            else:
                print("Por favor, introduce 'y' para continuar o 'n' para salir.")
        
        if continuar == 'n':
            break

##esto es important ;)
##hola caracola
##holis