import json

def agregar_categoria(CategoriaID:int, Nombre:str):
    with open("biblioteca.json", mode="r") as leerarchivo:
        leerjson= json.load(leerarchivo)
        nueva_categoria = {
            "CategoriaID": CategoriaID, 
            "Nombre": Nombre}
        leerjson["Categoria"].append(nueva_categoria)
    with open("biblioteca.json", mode="w") as escribirarchivo:
        json.dump(leerjson, escribirarchivo, indent=4)
        print("Categoria agregada con exito")   




def editar_categoria(CategoriaID:int, NuevoNombre:str):
        with open("biblioteca.json", mode="r") as leerarchivo:
            leerjson= json.load(leerarchivo)
            for categoria in leerjson["Categoria"]:
                if categoria["CategoriaID"] == CategoriaID:
                    categoria["Nombre"] = NuevoNombre

        with open("biblioteca.json", mode="w") as escribirarchivo:
            json.dump(leerjson, escribirarchivo, indent=4)
            print("Categoria editada con exito")

def eliminar_categoria():
    with open("biblioteca.json", mode="r") as leerarchivo:
        leerjson= json.load(leerarchivo)
        id_categoria = int(input("Ingrese el id de la categoria a eliminar: ")) 
        for categoria in leerjson["Categoria"]:
            if categoria["CategoriaID"] == id_categoria:
                leerjson["Categoria"].remove(categoria)

    with open("biblioteca.json", mode="w") as escribirarchivo:
        json.dump(leerjson, escribirarchivo, indent=4)
        print("Categoria eliminada con exito")

def buscar_categorias():
    with open("biblioteca.json", mode="r") as leerarchivo:
        leerjson= json.load(leerarchivo)
        id_categoria = int(input("Ingrese el id de la categoria a buscar: "))
        for categoria in leerjson["Categoria"]:
            if categoria["CategoriaID"] == id_categoria:
                print(categoria)

def generar_reporte_prestamos():
                    with open("biblioteca.json", mode="r") as leerarchivo:
                        leerjson = json.load(leerarchivo)
                        prestamos = {}
                        for libro in leerjson["Libros"]:
                            libro_id = libro["LibroID"]
                            prestamos[libro_id] = prestamos.get(libro_id, 0) + 1

                    for libro_id, cantidad_prestamos in prestamos.items():
                        print(f"LibroID: {libro_id}, Cantidad de Prestamos: {cantidad_prestamos}")
                