from nombres import *

def test_leer_frecuencias_nombres(lista_r):
    print(f"la primera linea es: {lista_r[0]}")
    print(f"la última linea es: {lista_r[-1]}")
    print(f"se han leído {len(lista_r)} líneas")

def test_filtrar_por_genero(lista_r):
    genero_elegido="Hombre"
    lista_f=filtrar_por_genero(lista_fichero=lista_r,genero=genero_elegido)
    print(f"El registro según el genero es: {lista_f}")

def test_calcular_nombres(lista_r):
    genero_elegido="Hombre"
    lista_f=calcular_nombres(lista_fichero=lista_r,genero=genero_elegido)
    print(f"el conjunto segun el genero {genero_elegido} es {lista_f}")




def funcion_principal():
    lista_r=leer_frecuencias_nombres("./VSCode FP/Python/laboratorio/clase5_(24-10)/data/frecuencias_nombres.csv")
    #test_leer_frecuencias_nombres(lista_r)
    #test_filtrar_por_genero(lista_r)
    test_calcular_nombres(lista_r)



if __name__=="__main__":
    funcion_principal()