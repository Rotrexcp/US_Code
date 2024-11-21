from typing import NamedTuple
import datetime
from datetime import datetime
import csv


Entreno = NamedTuple("Entreno" ,[("tipo", str),("fechahora", datetime),("ubicacion", str),("duracion", int),
            ("calorias", int),("distancia", float),("frecuencia", int),("compartido", bool)])

def leer_entreno(entrenos_csv:str)->list[Entreno]:

    lista_entrenos=[]

    with open(entrenos_csv, encoding="utf-8") as f:
    
        lector=csv.reader(f)
        next(lector) #solo si el fichero tiene una primera línea distinta

        for tipo,fechahora_cadena,ubicacion,duracion,calorias,distancia,frecuencia,compartido in lector:
        #for tupla in lector        (esto seria si queremos los datos empaquetados)

            #convertir las cadenas de caracteres en datos con su tipo
            fechahora=datetime.strptime(fechahora_cadena,"%d/%m/%Y %H:%M")    

            #si la lectura se hubiera hecho sin desempaquetar aquí pondriamos:
            #fecha=datetime.strptime(tupla[0],"%Y-%m-%d").date()
            tipo=str(tipo)
            ubicacion=str(ubicacion)
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            frecuencia=int(frecuencia)
            if compartido=="S":
                compartido=True
            elif compartido=="N":
                compartido=False

            r=Entreno(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido)

            lista_entrenos.append(r)

    return lista_entrenos


def tipos_entreno(tupla_tipos_entrenos:list[Entreno])->list[Entreno]:

    conjunto=set()

    for r in tupla_tipos_entrenos:
        conjunto.add(r.tipo)
    lista_tipos_entrenos_conjunto=list(conjunto)

    return lista_tipos_entrenos_conjunto


def entrenos_duracion_superior(lista_duraciones_entrenos:list[Entreno], d:int)->list:
    conjunto=set()

    for registro in lista_duraciones_entrenos:
        if registro.duracion > d:
            conjunto.add(registro.tipo)

    lista_duraciones_superior_conjunto=list(conjunto)

    return lista_duraciones_superior_conjunto


def suma_calorias(lista_calorias:list[Entreno], f_inicio:int, f_fin:int)->int:
    calorias_filtradas=[]
    f_inicio = datetime.strptime(f_inicio, "%d/%m/%Y %H:%M")
    f_fin = datetime.strptime(f_fin, "%d/%m/%Y %H:%M")

    for registro in lista_calorias:
        fecha_registro=registro.fechahora
        if f_inicio < fecha_registro < f_fin:
            calorias=registro.calorias
            calorias=int(calorias)
            calorias_filtradas.append(calorias)
    
    return sum(calorias_filtradas)