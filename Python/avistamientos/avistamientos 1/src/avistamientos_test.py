from avistamientos import *

def test_leer_avistamientos(lista_r):
    print(f"se han leido un total de {len(lista_r)} avistamientos")


def test_contar_avistamientos_por_fecha(lista_r):
    fecha_elegida="2017-01-01"
    num_avistamientos=contar_avistamientos_por_fecha(lista_r, fecha=fecha_elegida)
    print(f"El número de avistamientos en la fecha 2017-01-01 es {num_avistamientos}")

def test_duracion_total_por_estado(lista_r):
    estado_elegido="CA"
    duracion=duracion_total_por_estado(lista_r, estado=estado_elegido)
    print(f"La duración total de los avistamientos en el estado de California es {duracion}")

def test_formas_distintas_por_estados(lista_r):
    estados_elegidos={"CA","TX"}
    num_formas=formas_distintas_por_estados(lista_r, estados=estados_elegidos)
    print(f"El número de formas distintas de avistamientos en los estados de California y Texas es {num_formas}")

def test_avistamiento_mayor_duracion_por_forma(lista_r):
    forma_elegida="triangle"
    avistamiento=avistamiento_mayor_duracion_por_forma(lista_r, forma=forma_elegida)
    print(f"El avistamiento de mayor duración con forma de triángulo es {avistamiento}")




if __name__ == "__main__":
    lista_r = leer_avistamientos("avistamientos.csv")
    test_leer_avistamientos(lista_r)
