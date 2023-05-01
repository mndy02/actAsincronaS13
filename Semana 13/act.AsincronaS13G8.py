#Definición de datos de los integrantes del equipo
integrantes = [
    {
        "nombres": "Amanda Yuridia",
        "apellidos": "Portillo Marroquín",
        "género": "Femenino",
        "edad": 17,
        "departamento": "San Salvador",
        "municipio": "El Paisnal",
        "dirección": "Cantón La Cabaña, Zona 'C', Casa #25"    
    },
    {
        "nombres": "Wendy Marisol",
        "apellidos": "Espinoza Rivas",
        "género": "Femenino",
        "edad": 17,
        "departamento":"San Salvador",
        "municipio": "Aguilares",
        "dirección": "Col. Santa Eugenia, Calle principal Casa #23, blog B"    
    },
    {
        "nombres": "Kenia Guadalupe",
        "apellidos": "Figueroa Ortega",
        "género": "Femenino",
        "edad": 17,
        "departamento":"San Salvador",
        "municipio": "Aguilares",
        "dirección": "Col. Girón pje 1, Casa #11"    
    },
    {
        "nombres": "Brandon Josué",
        "apellidos": "Rivera Alemán",
        "género": "Masculino",
        "edad": 20,
        "departamento":"San Salvador",
        "municipio": "Aguilares",
        "dirección": "Col. Girón pje 3, Casa #9"    
    },
    {
        "nombres": "Romilio David",
        "apellidos": "Galdamez Escobar",
        "género": "Masculino",
        "edad": 17,
        "departamento":"Chalatenango",
        "municipio": "Comalapa",
        "dirección": "Cantón Calendaria frente al desvío El Pilon"    
    }
]

#Mostrar menú de los integrantes
def mostrar_menu():
    print("\nIntegrantes del equipo:")
    for i, integrante in enumerate(integrantes):
        print(f"{i+1}. {integrante['nombres']}")
        
#Solicitar al usuario el nombre del integrante a consultar
def pedir_nombre():
    intentos = 0
    while intentos < 3:
        nombre = input("\nIngrese el nombre del integrante a consultar: ")
        for integrante in integrantes:
            if nombre.lower() == integrante['nombres'].lower():
                return integrante 
        intentos += 1
        print(f"\nNo se encontró un integrante con el nombre {nombre}. Por favor intente de nuevo")
    print("\nEl límite de intentos ha sido alcanzado. Regresando al menú principal")
    return None

#Mostrar los datos del integrante consultado 
def mostrar_datos(integrante):
    if integrante:
        print("\nDATOS DEL INTEGRANTE:")
        print(f"Nombre completo: {integrante['nombres']} {integrante['apellidos']}")
        print(f"Género: {integrante['género']}")
        print(f"Edad: {integrante['edad']} ")
        print(f"Departamento: {integrante['departamento']}")
        print(f"Municipio: {integrante['municipio']}")
        print(f"Dirección: {integrante['dirección']}")
        
#Función principal del programa
def ejecutar_programa():
    print("¡BIENVENIDO AL PROGRAMA!\n")   
    while True:
        opcion = input("\n¿Desea ejecutar el programa? (s/n): ")
        if opcion.lower() == 'n':
            print("\nEl programa ha terminado")
            break
        elif opcion.lower() == 's':
            mostrar_menu()
            integrante = pedir_nombre()
            mostrar_datos(integrante)
            if not integrante:
                continue
            else:
                opcion2 = input("\n¿Desea consultar otros datos de otro integrante? (s/n):  ")
                if opcion2.lower() == 's':
                    continue 
                else:
                    print("\nEl programa ha terminado")
                    break
    else:
        ("\nOpción inválida. Por favor imtente de nuevo")
        
#Ejecutar función principal del programa
ejecutar_programa()

print("\n¡FIN DEL PROGRAMA!")
