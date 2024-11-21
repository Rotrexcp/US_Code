from typing import NamedTuple
import csv
import datetime
from datetime import date
from coordenadas import distancia
from collections import defaultdict, Counter



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
        
        for fecha, ciudad, estado, forma, duracion, comentarios, latitud, longitud in lector:
            fechahora=datetime.datetime.strptime(fecha,"%m/%d/%Y %H:%M")
            duracion=float(duracion)
            coordenadas=Coordenadas(float(latitud), float(longitud))
            
            r=Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, coordenadas)
            lista_avistamientos.append(r)
    
    return lista_avistamientos


'''Implemente una función tal que dada una fecha devuelva el número de avistamientos que 
se han producido en esa fecha.'''
def contador_fecha(lista_avistamientos:list[Avistamiento], fecha:date)-> int:
    contador = 0
    for registro in lista_avistamientos:
        if registro.fechahora.date() == fecha:
            contador += 1
    return contador

def contador_fecha2(lista_avistamientos:list[Avistamiento], fecha:date)-> int:
    return sum(1 for avistamiento in lista_avistamientos if avistamiento.fechahora.date() == fecha)


'''Dado un estado implemente una función que devuelva la duración total de los 
avistamientos de ese estado. '''
def duracion_total(lista_avistamientos:list[Avistamiento], estado:str)-> float:
    suma = 0
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() == estado.lower():
            suma += avistamiento.duracion
    return suma

def duracion_total2(lista_avistamientos:list[Avistamiento], estado:str)-> float:
    return sum(avistamiento.duracion for avistamiento in lista_avistamientos if avistamiento.estado.lower() == estado.lower())


'''Implemente  una  función  tal  que  dado  un  conjunto  de  estados  devuelva  el  número  de 
formas distintas de los avistamientos observados en esos estados. '''
def numero_formas_distintas(lista_avistamientos:list[Avistamiento], estados:set[str])-> int:
    conj_formas = set()
    for avistamiento in lista_avistamientos:
        if avistamiento.estado in estados:
            conj_formas.add(avistamiento.forma)
    return len(conj_formas)

def numero_formas_distintas2(lista_avistamientos:list[Avistamiento], estados:set[str])-> int:
    return len({avistamiento.forma for avistamiento in lista_avistamientos if avistamiento.estado in estados})

'''Dada  una  forma  determinada,  devuelve  el  avistamiento  de  mayor  duración  de  entre 
todos los que tienen esa forma. '''
def avistamiento_mayor_duracion(lista_avistamientos:list[Avistamiento], forma:str)-> Avistamiento | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.forma == forma]
    return max(lista_fil, key=lambda x: x.duracion)

# Si se desea que la función anterior devuelva None en caso de no haber avistamientos con esa forma, se puede hacer de la siguiente manera:
def avistamiento_mayor_duracion2(lista_avistamientos:list[Avistamiento], forma:str)-> Avistamiento | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.forma == forma]
    if len(lista_fil) > 0:    
        maximo = max(lista_fil, key=lambda x: x.duracion)
    else:
        maximo = None
    
    return maximo


'''Implemente una función tal que dado un año y una palabra devuelva el avistamiento con 
el  comentario  más  largo  y  la  longitud  de  este  para  los  avistamientos  del  año  y  que 
contenga la palabra dados como argumentos. '''
def avistamiento_comentario_mas_largo(lista_avistamientos:list[Avistamiento], año:int, palabra:str)-> tuple[Avistamiento, int] | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date().year == año and palabra in avistamiento.comentarios]
    if len(lista_fil) > 0:
        maximo = max(lista_fil, key=lambda x: len(x.comentarios))
        maximo = (maximo, len(maximo.comentarios))
    else:
        maximo = None
    return maximo


'''Dado un estado, implemente una función que devuelva el punto medio (longitud y latitud 
media de los avistamientos de ese estado.'''
def punto_medio(lista_avistamientos:list[Avistamiento], estado:str)-> tuple[float, float] | None:
    sum_lat=0.
    sum_lon=0.
    contador=0
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() == estado.lower():
            sum_lat+=avistamiento.coordenadas.latitud
            sum_lon+=avistamiento.coordenadas.longitud
            contador+=1

    if contador > 0:
        punto_medio = (sum_lat/contador, sum_lon/contador)
    else:
        punto_medio = None
    
    return punto_medio


'''Usando  la  función  distancia  de  Coordenadas,  construya  una  función  que  tiene  como 
entrada unas coordenadas ubicacion y un radio r y devuelve los avistamientos que se han 
situado dentro de un radio r a ubicación. '''
def avistamientos_en_radio(lista_avistamientos:list[Avistamiento], ubicacion:Coordenadas, r:float)-> list[Avistamiento]:
    return [avistamiento for avistamiento in lista_avistamientos if distancia(avistamiento.coordenadas, ubicacion) < r]


'''Implemente  una  función  que  devuelva  una  lista  ordenada  por  fecha  (de  más  reciente  a 
más antigua) con los avistamientos entre  fecha_inicial  y fecha_final (ambas inclusive). Si 
fecha_inicial  es  None,  entonces  se  devolverán  todos  los  registros  hasta  la  fecha_final.  Si 
fecha_final es  None,  entonces  se  devolverán todos  los  registros  desde  la  fecha_inicial.  Si 
ambas fechas son None, se devuelve la lista de registros completa. '''
def filtra_entre_fechas(lista_avistamientos:list[Avistamiento], fecha_ini:date = None, fecha_fin:date = None)-> list[Avistamiento]:
    lista_filtrada = []
    if fecha_ini == None and fecha_fin == None:
        lista_filtrada = lista_avistamientos
    elif fecha_ini == None:
        lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date() <= fecha_fin]
    elif fecha_fin == None:
       lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date() >= fecha_ini]
    else:
        lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if fecha_ini <= avistamiento.fechahora.date() <= fecha_fin]

    return sorted(lista_filtrada, key=lambda x: x.fechahora, reverse=True)

#Mejor solución
def filtra_entre_fechas2(lista_avistamientos:list[Avistamiento], fecha_ini:date = None, fecha_fin:date = None)-> list[Avistamiento]:
    lista_filtrada = []
    if fecha_ini == None:
        fecha_ini = datetime.datetime(1700,1,1).date()
    if fecha_fin == None:
        fecha_fin = datetime.datetime(2020,1,1).date()
    lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if fecha_ini <= avistamiento.fechahora.date() <= fecha_fin]
    return sorted(lista_filtrada, key=lambda x: x.fechahora, reverse=True)


'''Implemente una función que devuelva el número de avistamientos por año. Hágalo con los 
tipos dict, Counter y defaultdict.'''
#dict
def contador_por_año(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        año = avistamiento.fechahora.datetime().year
        if año in diccionario:
            diccionario[año] += 1
        else:
            diccionario[año] = 1
    return diccionario

#defaultdict        Es para evitar preguntar si la clave está en el diccionario
def contador_por_año_defaultdict(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    diccionario = defaultdict(int)
    for avistamiento in lista_avistamientos:
        año = avistamiento.fechahora.datetime().year
        diccionario[año] += 1
    return diccionario

#Counter
def contador_por_año_counter(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    return Counter(avistamiento.fechahora.datetime().year for avistamiento in lista_avistamientos)


'''Implemente una función que devuelva cuál es el año con más avistamientos'''
def año_con_mas_avistamientos(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = contador_por_año(lista_avistamientos)
    diccionario.items()
    maximo = max(diccionario.items(), key=lambda x: x[1])       #diccionario.items() es una lista de tuplas, por lo que se puede usar un max() con una key
    return maximo[0]            #Cuando se pide un maximo no se utiliza un sorted() y devolver el ultimo elemento, sino usar el maximo

def año_con_mas_avistamientos_counter(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = Counter(contador_por_año_counter(lista_avistamientos))
    maximo = diccionario.most_common(1)[0][0]       #esto seria -> diccionario.most_common(1)=[(2010, 10)] -> diccionario.most_common(1)[0]=(2010, 10) -> diccionario.most_common(1)[0][0]=2010
    return maximo[0]


'''Dada una forma, implemente una función que devuelva el año con más avistamientos de esa forma. '''
def año_con_mas_avistamientos_forma_counter(lista_avistamientos:list[Avistamiento], forma:str)-> int:
    diccionario = Counter(avistamiento.fechahora.datetime().year for avistamiento in lista_avistamientos if avistamiento.forma == forma)
    maximo = diccionario.most_common(1)[0][0]
    return maximo


'''Implemente una función que devuelva la hora en la que se producen más avistamientos.'''
def hora_con_mas_avistamientos(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = Counter(avistamiento.fechahora.datetime().hour for avistamiento in lista_avistamientos)
    maximo = diccionario.most_common(1)[0][0]
    return maximo


'''Implemente una función que devuelva un diccionario que relaciona cada fecha como clave 
con el conjunto de los avistamientos de esa fecha. '''
#dict
def conjunto_avistamientos_por_fecha(lista_avistamientos:list[Avistamiento])-> dict[date, set[Avistamiento]]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.date()
        if clave in diccionario:
            diccionario[clave].add(avistamiento)
        else:
            diccionario[clave] = {avistamiento}
    return diccionario

#defaultdict
def conjunto_avistamientos_por_fecha_defaultdict(lista_avistamientos:list[Avistamiento])-> dict[date, list[Avistamiento]]:
    diccionario = defaultdict(set)
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.date()
        diccionario[clave].add(avistamiento)
    return diccionario

        #cual es la fecha con mayor numero de formas distintas de avistamiento
def fecha_con_mas_formas_distintas(lista_avistamientos:list[Avistamiento])-> date:
    diccionario = conjunto_avistamientos_por_fecha(lista_avistamientos)
    dicc_formas={}
    for avistamientos in diccionario:
        formas={r.forma for r in diccionario[avistamientos]}
        dicc_formas[avistamientos]=formas

    return max(dicc_formas, key=lambda x: len(x[1]))[0]


'''Implemente  una  función  que  devuelva  un  diccionario  con  los  meses  como  claves  y  los 
valores son el conjunto de formas distintas de avistamientos ese mes.'''
def formas_distintas_por_mes(lista_avistamientos:list[Avistamiento])-> dict[int, set[str]]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.datetime().month
        if clave in diccionario:
            diccionario[clave].add(avistamiento.forma)
        else:
            diccionario[clave] = {avistamiento.forma}
    return diccionario


'''Implemente una función que devuelva un diccionario en el que las claves son las formas de 
los avistamientos, y los valores el porcentaje de avistamientos con dicha forma.'''
#tipos de diccionario:
#   contador
#   sumador
#   organizador a lista
#   organizador a conjunto
#   media
#   porcentaje (parecido a media)

#todos tienen la variante de máximo

def porcentaje_formas(lista_avistamientos:list[Avistamiento])-> dict[str, float]:
    dicc_cont = Counter(avistamiento.forma for avistamiento in lista_avistamientos)
    total_avistamientos = len(lista_avistamientos)
    dicc_porc={}
    for forma in dicc_cont:
        dicc_porc[forma]=dicc_cont[forma]/total_avistamientos*100
    return dicc_porc


'''Para averiguar la zona de mayor número de avistamientos, vamos a reducir las coordenadas 
de  longitud  y  latitud  a  su  parte  entera.  Implemente  de  forma  auxiliar  una  función  que 
devuelva un diccionario donde las claves sean la parte entera de la longitud y latitud y los 
valores un contador.'''
def contador_coordenadas_enteras(lista_avistamientos:list[Avistamiento])-> dict[tuple[int, int], int]:
    dicc_cont = Counter((int(avistamiento.coordenadas.latitud), int(avistamiento.coordenadas.longitud)) for avistamiento in lista_avistamientos)
    return dicc_cont
#si nos piden la zona con mayor numero de avistamientos
#return Counter((int(avistamiento.coordenadas.latitud), int(avistamiento.coordenadas.longitud)) for avistamiento in lista_avistamientos).most_common(1)[0][0]


'''Implemente una función tal que dado un año que por defecto toma el valor None, devuelve 
la media de días transcurridos entre dos avistamientos consecutivos del año especificado. 
Si en la llamada no se especifica año, entonces se calculará para todos los años. '''
#lo primero seria ordenar los avistamientos por fecha
#luego calcular la diferencia de dias entre dos avistamientos consecutivos segun el año

#       dada una lista de valores calcula la media de los incrementos entre dos valores consecutivos
#       ejemplo:[2,5,3,7,8,6,5] -> [3,2,-4,1,-2,-1] -> 3+2-4+1-2-1= -1
def lista_diferencias(lista:list[int])-> float:
    lista_dif=[]
    for i in range(len(lista)-1):
        diferencia = lista[i+1]-lista[i]
        lista_dif.append(diferencia)
    
    return sum(lista_dif)/len(lista_dif)

#       fecha1 - fecha2 = duration -> se indica como (fecha1 - fecha2).days (funcion especial de Python que mide intervalos de tiempo entre dos fechas)

def media_dias_entre_avistamientos(lista_avistamientos:list[Avistamiento], año:int = None)-> float:
    lista_ordenada = sorted(lista_avistamientos, key=lambda x: x.fechahora)
    if año == None:
        dicc_años = defaultdict(list)
        for avistamiento in lista_ordenada:
            dicc_años[avistamiento.fechahora.datetime().year].append(avistamiento.fechahora.datetime().toordinal())
        dicc_medias={}
        for año in dicc_años:
            dicc_medias[año]=lista_diferencias(dicc_años[año])
        return dicc_medias
    else:
        lista_año = [avistamiento for avistamiento in lista_ordenada if avistamiento.fechahora.datetime().year == año]
        lista_fechas = [avistamiento.fechahora.datetime().toordinal() for avistamiento in lista_año]
        return lista_diferencias(lista_fechas)