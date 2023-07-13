import numpy as np


print("----------------------------------------------------")
print("bienvenides a CREATIVOS.CL")
print("Ventas de entradas al concierto VIP de Michael Jam")
print("----------------------------------------------------")


run=[]
cantidad=[]
ubicaciones=[]
precio=[[120000],[80000],[50000]]
tipo=["Platinum","Gold","Silver"]
ganancia=[]


def mostrar_menu():
    print("----MENÚ----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


def comprar_entrada():
    run=input("Ingrese su RUN sin digito verificador ni puntos: ")
    cantidad=input("Ingrese la cantidad de entradas que desee comprar: ")
    print(len(ubicaciones))
    ubicacion=input("Ingrese la ubicacion que desee comprar: ")
    
    if len(run)!=8:
        print("El RUN debe tener 8 caracteres.")
        return
    for i in range(len(run)):
        if run[i]==run:
            print("RUN ya ingresado previamente")
            return
    
    if len(cantidad)<1 or len(cantidad)>3:
        print("La cantidad de entradas que puede comprar son entre 1 y 3.")
        return
    
    for i in range(len(ubicaciones))
        if ubicaciones[i]==ubicacion:
            print("No esta disponible")
            return

    run.append(run)
    cantidad.append(cantidad)
    ubicaciones.append(ubicaciones)
  
    print("Compra realizada exitosamente.");


def mostrar_ubicaciones():
    print("A continuacion se muestan las ubicaciones disponibles: ")
    print(len(ubicaciones))
      return


def listado_asistentes():
    print("A continuación se muestra la lista de asistentes: ")
    print(len(run))
    

def ganancias_totales():
    print("las ganancias hasta el momento son: ")
    print(len(ganancia))


def salir():
    print("Gracias por su compra")
    print("Andrés Salcedo Morales")
    print("13-07-2023")


def main():
    while True:
        mostrar_menu()
        opcion=input("Ingrese la opción deseada (1-5): ")
        if opcion=="1":
            comprar_entrada()
        elif opcion=="2":
            mostrar_ubicaciones()
        elif opcion=="3":
            listado_asistentes()
        elif opcion=="4":
            ganancias_totales()
        elif opcion=="5":
            salir()
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__=="__main__":
    main()