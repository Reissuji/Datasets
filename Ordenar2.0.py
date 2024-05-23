import csv
entrada=r'C:/Users/Ani/Desktop/BVNNY/Master/TFM/Datasets/PLANTAI_Usar.csv'
salida=r'C:/Users/Ani/Desktop/BVNNY/Master/TFM/Datasets/prueba_planta_usar.csv'

#Ordenar
def ordenar(entrada, salida):

    print("leyendo:",entrada)
    with open(entrada, "r", encoding="latin-1") as entrada:
        lector=csv.reader(entrada)
        encabezado=next(lector)
        print("encabezado actual:", encabezado)

        lineas_ordenadas=sorted(lector,key=lambda x: x[0])
        print("Lineas ordenadas:", lineas_ordenadas)


    with open(salida, "w", newline="", encoding="latin-1") as salida:
        escritor=csv.writer(salida)
        escritor.writerow(encabezado)
        escritor.writerows(lineas_ordenadas)


ordenar(entrada, salida)
