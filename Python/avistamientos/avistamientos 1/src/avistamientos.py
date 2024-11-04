from typing import NamedTuple
import csv
import datetime



'''Defina dos NamedTuple Avistamiento y Coordenadas para los namedtuple dados.'''
Avistamiento = NamedTuple("Avistamiento",[("fechahora", datetime), ("ciudad", str), ("estado", str), ("forma", str), ("duracion", float), ("comentarios", str), ("coordenadas", "Coordenadas")])
Coordenadas = NamedTuple('Coordenadas', [('latitud', float), ('longitud', float)])


'''Implemente  una  función  que  lea  un  fichero  con  una  estructura  como  la  descrita  y 
devuelva una lista de tuplas, según el namedtuple que se proporciona. '''
def leer_avistamientos(fichero: str) -> list[Avistamiento]:
    with open(fichero, encoding="utf-8") as f:
        lista_avistamientos = []
        lector = csv.reader(f)
        next(lector)
        
        for fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud in lector:
            fechahora=datetime.datetime.strptime(fechahora,"%m/%d/%Y %H:%M:%S")
            duracion=float(duracion)
            coordenadas=Coordenadas(float(latitud), float(longitud))
            
            r=Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, coordenadas)
            lista_avistamientos.append(r)
    
    return lista_avistamientos


'''Implemente una función tal que dada una fecha devuelva el número de avistamientos que 
se han producido en esa fecha.'''
def contar_avistamientos_por_fecha(lista_avistamientos:list[Avistamiento], fecha):
    fecha_obj = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    contador = 0
    for avistamiento in lista_avistamientos:
        avistamiento_fecha = datetime.datetime.strptime(avistamiento.fechahora, "%Y-%m-%d %H:%M:%S")
        if avistamiento_fecha.date() == fecha_obj.date():
            contador += 1
    return contador


'''Dado un estado implemente una función que devuelva la duración total de los 
avistamientos de ese estado. '''
def duracion_total_por_estado(lista_avistamientos:list[Avistamiento], estado:str):
    duracion_total = 0
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() == estado.lower():
            try:
                duracion = float(avistamiento.duracion.split()[0])
                duracion_total += duracion
            except ValueError:
                continue
    return duracion_total


'''Implemente  una  función  tal  que  dado  un  conjunto  de  estados  devuelva  el  número  de 
formas distintas de los avistamientos observados en esos estados. '''
def formas_distintas_por_estados(lista_avistamientos:list[Avistamiento], estados:str):
    formas_distintas = set()
    estados = set(estado.lower() for estado in estados)
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() in estados:
            formas_distintas.add(avistamiento.forma.lower())
    return len(formas_distintas)


'''Dada  una  forma  determinada,  devuelve  el  avistamiento  de  mayor  duración  de  entre 
todos los que tienen esa forma. '''
def avistamiento_mayor_duracion_por_forma(lista_avistamientos:list[Avistamiento], forma:str):
    mayor_duracion = 0
    avistamiento_mayor_duracion = None
    for avistamiento in lista_avistamientos:
        if avistamiento.forma.lower() == forma.lower():
            try:
                duracion = float(avistamiento.duracion.split()[0])
                if duracion > mayor_duracion:
                    mayor_duracion = duracion
                    avistamiento_mayor_duracion = avistamiento
            except ValueError:
                continue
    return avistamiento_mayor_duracion