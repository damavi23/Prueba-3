import os
import time
import json
import funcion
import json

while True:
    
        print("***************************************")
        print("*            MUNDO LIBRO              *")
        print("***************************************")
        print("\n, \n")
        print("[1] - Mantenedor de categorias")
        print("[2] - Reportes")
        print("[3] - Salir")
        opcion = input("Ingrese una opcion: ")
        while True:
            if opcion == "1":
                print("***************************************")
                print("*            MUNDO LIBRO              *")
                print("***************************************")
                print("\n, \n")
                print("[1] Agregar categoria")
                print("[2] Editar categoria")
                print("[3] Eliminar categoria")
                print("[4] Buscar categoria")
                print("[5] Volver")
                opcion = input("Ingrese una opcion: ")
                while True:    
                    if opcion == "1":
                        print("***************************************")
                        CategoriaID = +1
                        Nombre = input("Ingrese el nombre de la categoria: ")
                        funcion.agregar_categoria(CategoriaID, Nombre)
                        time.sleep(1)
                        os.system("cls")
                        
                    elif opcion == "2":
                        CategoriaID = input("Ingrese el id de la categoria a editar: ")
                        NuevoNombre = input("Ingrese el nuevo nombre de la categoria: ")
                        funcion.editar_categoria(CategoriaID, NuevoNombre)
                        time.sleep(1)
                        os.system("cls")
                        
                    elif opcion == "3":
                        id_categoria = input("Ingrese el id de la categoria a eliminar: ")
                        funcion.eliminar_categoria(id_categoria)
                        time.sleep(1)
                        os.system("cls")
                        
                    elif opcion == "4":
                        id_categoria = input("Ingrese el id de la categoria a buscar: ")
                        funcion.buscar_categorias(id_categoria)
                        time.sleep(1)
                        os.system("cls")
                        
                    elif opcion == "5":
                        break
                    else:
                        print("Opcion no valida")

            elif opcion == "2":
                funcion.generar_reporte_prestamos()
                
            elif opcion == "3":
                break

