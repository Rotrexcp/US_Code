from clima_lectura import *
from collections import Counter, defaultdict



'''1. Devuelve un diccionario que a cada año le haga 
corresponder un contador con el número de registros de ese año.'''
def diccionario_contador_por_año(lista:list[RegistroClima])->dict[int,int]:
    dicc={} # dicc=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc:
            dicc[clave]+=1
        else:
            dicc[clave]=1
    return dicc


'''2.   Devuelve un diccionario tal que dado un año 
asigna a cada mes del año el número de registros de ese mes.'''
def diccionario_contador_por_mes(lista:list[RegistroClima], año:int)->dict[int, int]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                dicc[clave]+=1
            else:
                dicc[clave]=1
    return dicc

def diccionario_contador_por_mes2(lista:list[RegistroClima], año:int)->dict[int, int]:
    dicc=dict()
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc:
            dicc[clave]+=1
        else:
            dicc[clave]=1
    return dicc


'''3.  Repita el ejercicio 2 usando el tipo Counter.'''
def diccionario_contador_por_mes_counter(lista:list[RegistroClima], año:int)->dict[int, int]:
    return Counter(r.fecha.month for r in lista if r.fecha.year==año)


'''4.  Devuelva un diccionario tal que dado un año devuelva 
para cada mes la lluvia acumulada en ese mes.'''
def diccionario_lluvia_acumulada_por_mes(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                dicc[clave]+=r.lluvia
            else:
                dicc[clave]=r.lluvia
    return dicc

def diccionario_lluvia_acumulada_por_mes2(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=dict()
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc:
            dicc[clave]+=r.lluvia
        else:
            dicc[clave]=r.lluvia
    return dicc


'''5.  Repita el ejercicio 5 usando el tipo defaultdict.'''
def diccionario_lluvia_acumulada_por_mes3(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=defaultdict(float)
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        dicc[clave]+=r.lluvia 
    return dicc


'''6.   Dado un año devuelva un diccionario tal que asocie a
 cada mes de ese año la temperatura máxima media de ese mes.'''
def diccionario_tempmax_media_por_mes(lista:list[RegistroClima], año:int)->dict[int, float]:
    lista_fil=[r for r in lista if r.fecha.year==año]
    dicc_contador=Counter(r.fecha.month for r in lista_fil)
    dicc_suma=dict()
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc_suma:
            dicc_suma[clave]+=r.temp_max
        else:
            dicc_suma[clave]=r.temp_max
    dicc_media={}
    for mes in dicc_suma:
        dicc_media[clave]=dicc_suma[clave]/dicc_contador[clave]
    return dicc_media

def diccionario_tempmax_media_por_mes2(lista:list[RegistroClima], año:int)->dict[int, float]:
    lista_fil=[r for r in lista if r.fecha.year==año]
    dicc_contador=dict()
    dicc_suma=dict()
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc_suma:
            dicc_suma[clave]+=r.temp_max
            dicc_contador[clave]+=1
        else:
            dicc_suma[clave]=r.temp_max
            dicc_contador[clave]=1
    dicc_media={}
    for mes in dicc_suma:
        dicc_media[clave]=dicc_suma[clave]/dicc_contador[clave]
    return dicc_media


'''7.   Usando el ejercicio 6 y dado un año devuelva cuál 
es el mes de ese año con la temperatura máxima media mayor.'''
def mes_mayor_tempmax_media(lista:list[RegistroClima], año:int)->int:
    dicc_temp_media=diccionario_tempmax_media_por_mes(lista, año)
    return max(dicc_temp_media.items(), key=lambda x:x[1])[0]