# cerrarwhatsapp.py
import psutil

def funcion_ejecutar():
    # Buscar procesos por nombre
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'WhatsApp.exe':  # Cambia esto por el nombre del proceso
            proc.kill()  # Esto fuerza la detención del proceso
            return f"Proceso {proc.info['name']} detenido"
    return "No se encontró el proceso WhatsApp.exe en ejecución."