import os
file_name = "inventario.txt"

open(file_name,'a')

while True:
    print('Listas de opciones')
    print('1. Agregar un producto')
    print('2. Eliminar un producto')
    print('3. Buscar un producto')
    print('4. Actualizar la cantidad de un producto')
    print('5. Listar todos los productos')
   
    print('6. Salir')

    opciones = int(input('Elegir una opcion del 1-6:\n'))
    match opciones:
        case 1:
            codigo = input('Ingrese el codigo del producto: ')
            producto = input('Ingrese el nombre del producto: ')
            cantidad = input('Ingrese la cantidad disponible: ')
            precio = input('Ingrese el precio por unidad: ')
            codigo_existe = False
            try:
                  with open(file_name,"r") as file:
                      lineas= file.readlines()
                      for linea in lineas:
                          if codigo==linea.split(",")[0].strip():
                              codigo_existe=True
                              break
            except:
                print(f'el archivo {file_name} no existe aun, se creara un nuevo archivo')
            
            if not codigo_existe:
                with open(file_name,'a') as file:
                    file.write(f"{codigo}, {producto}, {cantidad}, {precio}\n")
            else:
                print(f'el codigo {codigo} no se puede agreagar porque ya existe')


        
        case 2:
            codigo=input('Ingresa el codigo para eliminar el producto: ')
            with open(file_name,"r") as file:
                lineas = file.readlines()
            with open(file_name,"w") as file:
                for lines in lineas:
                    if lines.split(",")[0]!=codigo:

                        file.write(lines)
                        
                     
                    

        case 3:
            codigo:input('Ingrese el codigo para buscar y berificar que le producto exista: ')
            with open(file_name,"r") as file:
               lineas = file.readlines()
               for lines in lineas:
                   if lines.split(",")[0]==codigo:
                       print(f'El producto esta registrado en el archivo es: {lines}')


        case 4:
             codigo=input('Ingrese el codigo para actualizar la cantidad del producto: ')
             cantidad=input("Introdusca la nueva cantidad del producto: ")
            
             with open(file_name,"r") as file:
                lineas=file.readlines()
             with open(file_name,"w") as file:
                for lines in lineas:
                    if lines.split(",")[0]==codigo:
                        file.write(f"{codigo},{producto},{cantidad},{precio}\n")
                       
                    else:
                        file.write(lines)
                        
        case 5:
            with open(file_name,"r") as file:
                lineas=file.readlines()
                for lines in lineas:
                    print(lines)
        case 6:
            os.remove(file_name)
            print('Saliendo...')
            break

