informacion_pacientes = []

# muestra el menu principal
def menu_principal():
    opcion_elegida = int(input("""
          Sistema de Gestion De clinica
          1. Cargar pacientes
          2. Mostrtar todos los pacientes
          3. Buscar pacientes por numero de Historial clínica
          4. Ordenar pacientes por número de historia clínica 
          5. Mostrar paciente con mas días de internacion
          6. Mostrar paciente con menos días de internación
          7. Cantidad de pacientes con más de 5 días de internacíon
          8. Promedio de días de internacion de todos los pacientes
          9. Salir
          
          respuesta: """))
    
    return opcion_elegida
# agregamos a los pacientes ya con los datos validados
def agregar_paciente(nro_clinico, nombre, edad, diagnostico, nro_dias_internacion):
    paciente_nuevo = []
    paciente_nuevo.append(nro_clinico)
    paciente_nuevo.append(nombre)
    paciente_nuevo.append(edad)
    paciente_nuevo.append(diagnostico)
    paciente_nuevo.append(nro_dias_internacion)
    return paciente_nuevo
    
# ----------------------------------------------------
# validamos datos del paciente
def validar_nro_historial(nro_historial: str) -> int:
    while nro_historial.isdigit() == False:
        nro_historial = input("Error, ingrese un numero del historial clinica: ")
    
    nro_historial = int(nro_historial)
    while nro_historial < 1:
        nro_historial = validar_nro_historial(input("Error, ingrese un número postivo del historial: "))
    return nro_historial 
  
def validar_nombre(nombre: str) -> str:
    while nombre.isalpha() == False:
        nombre = input("Error, ingrese el nombre del paciente: ")
    return nombre
   
def validar_edad(edad: str) -> int:
    while edad.isdigit() == False:
        edad = input("Error, ingrese su edad: ")
    
    edad = int(edad)
    while edad < 1:
        edad = validar_edad(input("Error, ingrese su edad: "))
    return edad

def validar_diagnostico(diagnostico: str) -> str:
    while diagnostico.isalpha() == False:
        diagnostico = input("Error, ingrese el diagnosticor: ")
    return diagnostico

def validar_cant_dias_internacion(dias_internacion: str) -> int:
    while dias_internacion.isdigit() == False:
        dias_internacion = input("Error, ingrese los dias de internacion: ")
    
    dias_internacion = int(dias_internacion)
    while dias_internacion < 1:
        dias_internacion = validar_cant_dias_internacion(input("Error, ingrese los dias de internacion: "))
    return dias_internacion
    
def validar_datos_ingresados(cantidad_pacientes) -> list:
    for _ in range(cantidad_pacientes):
        numero_historia_clinica = validar_nro_historial(input("ingrese el numero del historial clinica: "))
        nombre_paciente = validar_nombre(input("ingrese el nombre del paciente: "))
        edad = validar_edad(input("Ingrese la edad del paciente: "))
        diagnostico = validar_diagnostico(input("ingrese el diagnóstico del paciente: "))
        cant_dias_internacion = validar_cant_dias_internacion(input("ingrese la cantidad de días de internación: "))

        paciente_nuevo = agregar_paciente(numero_historia_clinica, nombre_paciente, edad, diagnostico, cant_dias_internacion)
        informacion_pacientes.append(paciente_nuevo)

    return informacion_pacientes


# -----------------------------------
# mostramos los pacientes con su informacion
def mostrar_pacientes(informacion_pacientes):
    num = 0
    for i in range(len(informacion_pacientes)):
        num += 1
        print(f"""
            Paciente {num} 
            Nro Hisotorial Clinico: {informacion_pacientes[i][0]} 
            Nombre: {informacion_pacientes[i][1]}
            edad: {informacion_pacientes[i][2]}
            Diagnóstico: {informacion_pacientes[i][3]}
            Cantidad de días de internación: {informacion_pacientes[i][4]}
                  """) 
    return ""

# -------------------------------------------------------------
# validamos su numero de historial para usarlo despues en la funcion paciente_a_buscar()
def validar_nro_historia_clinica(nro_historial):
    while nro_historial.isdigit() == False:
        nro_historial = input("Error, ingrese un numero del historial clinica: ")
    
    nro_historial = int(nro_historial)
    while nro_historial < 1:
        nro_historial = validar_nro_historia_clinica(input("Error, ingrese un número postivo del historial: "))
    return nro_historial

# buscamos el paciente por su numero de historial clinica
def paciente_a_buscar(nro_historia_clinica):
    for i in range(len(informacion_pacientes)):
        if informacion_pacientes[i][0] == nro_historia_clinica:
            informacion_paciente_encontrado = f"""
                                            Nro Hisotorial Clinico: {informacion_pacientes[i][0]} 
                                            Nombre: {informacion_pacientes[i][1]}
                                            edad: {informacion_pacientes[i][2]}
                                            Diagnóstico: {informacion_pacientes[i][3]}
                                            Cantidad de días de internación: {informacion_pacientes[i][4]}"""
            return  informacion_paciente_encontrado
    return "no se encontro el numero de historial del paciente"

# ordenamos la informacion de forma ascendente de los pacientes
def ordenar_informacion_paciente():
    n = len(informacion_pacientes)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if informacion_pacientes[j][0] > informacion_pacientes[j+1][0]:
                informacion_pacientes[j], informacion_pacientes[j+1] = informacion_pacientes[j+1], informacion_pacientes[j]

    return informacion_pacientes

# ordemaos de mayor a menor para sacar el mayor paciente con dias internados
def ordenar_paciente_dias_internacion(informacion_pacientes):
    n = len(informacion_pacientes)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if informacion_pacientes[j][4] > informacion_pacientes[j+1][4]:
                informacion_pacientes[j], informacion_pacientes[j+1] = informacion_pacientes[j+1], informacion_pacientes[j]

    return informacion_pacientes


# -----------------------------------------------
# retornamos los pacientes cn¡on mas de 5 dias de internacion
def pacientes_mayor_5_dias(informacion_pacientes):
    paciente_con_mas_5_dias_internacion = 0
    for i in range(len(pacientes_mayor_5_dias)):
        if informacion_pacientes[i][4] > 5:
            paciente_con_mas_5_dias_internacion += 1
    return paciente_con_mas_5_dias_internacion
# sumamos los dias de internacion de los pacientes
def suma_dias_internacion(informacion_pacientes):
    acumulador_dias = 0
    for i in range(len(informacion_pacientes)):
        acumulador_dias += informacion_pacientes[i][4]       

    return acumulador_dias
# promedio de los dias sumados
def promedio_dias_internacion(dias_internacion, contador):
    promedio_dias = dias_internacion / contador
    return promedio_dias


ingreso = 1   
while ingreso == 1:
    opcion_menu = menu_principal()
    
    # carga de pacientes
    if opcion_menu == 1:
        cantidad_a_cargar_pacientes = int(input("¿Cuantos pacientes deasea ingresar?: "))

        while cantidad_a_cargar_pacientes < 1:
            cantidad_a_cargar_pacientes = int(input("Error, ¿Cuantos pacientes deasea ingresar?: "))
        datos_ingresados = validar_datos_ingresados(cantidad_a_cargar_pacientes)
        
        print(datos_ingresados)
    
    # mostrar lista de pacientes
    elif opcion_menu == 2:
        mostrar_pacientes(informacion_pacientes)
    
    # busqueda de pasciente
    elif opcion_menu == 3:
        if informacion_pacientes != []:
            mostrar_pacientes(informacion_pacientes)
            buscar_paciente = validar_nro_historia_clinica(input("ingrese el numero de la historia clinica: "))
            paciente_encontrado = paciente_a_buscar(buscar_paciente)
            print(paciente_encontrado)
        else:
            print("no hay pacientes")
            
    # ordenar pacientes
    elif  opcion_menu == 4:
        informacion_paciente_ordenado = ordenar_informacion_paciente()
        mostrar_pacientes(informacion_pacientes)
    
    # paciente con mayor dias de internacion
    elif opcion_menu == 5:
        paciente_dias_internacion = len(ordenar_paciente_dias_internacion(informacion_pacientes) )
        print(f"""
            El paciente con mas dias de internacion es:
            Nro Hisotorial Clinico: {informacion_pacientes[paciente_dias_internacion - 1][0]} 
            Nombre: {informacion_pacientes[paciente_dias_internacion - 1][1]}
            edad: {informacion_pacientes[paciente_dias_internacion - 1][2]}
            Diagnóstico: {informacion_pacientes[paciente_dias_internacion - 1][3]}
            Cantidad de días de internación: {informacion_pacientes[paciente_dias_internacion - 1][4]}""")
     
    #  # paciente con menor dias de internacion
    elif opcion_menu == 6:
        paciente_dias_internacion = len(ordenar_paciente_dias_internacion(informacion_pacientes) )
        print(f"""
            El paciente con mas dias de internacion es:
            Nro Hisotorial Clinico: {informacion_pacientes[paciente_dias_internacion - paciente_dias_internacion][0]} 
            Nombre: {informacion_pacientes[paciente_dias_internacion - paciente_dias_internacion][1]}
            edad: {informacion_pacientes[paciente_dias_internacion - paciente_dias_internacion][2]}
            Diagnóstico: {informacion_pacientes[paciente_dias_internacion - paciente_dias_internacion][3]}
            Cantidad de días de internación: {informacion_pacientes[paciente_dias_internacion - paciente_dias_internacion][4]}""")
    
    # cantidad de pacientes con mayor de 5 dias de internacion
    elif opcion_menu == 7:
        cant_paciente_mayor_5_dias_internacion = pacientes_mayor_5_dias(informacion_pacientes)
        print(f"pacientes con días de internación mayor a 5 días: {cant_paciente_mayor_5_dias_internacion}")
    
    # promedio de los dias de internacion
    elif opcion_menu == 8:
        contador = len(informacion_pacientes)
        total_suma_dias_internacion = suma_dias_internacion(informacion_pacientes)
        resultado_promedio_dias = promedio_dias_internacion(total_suma_dias_internacion)
        print(f"Promedio de días de internación de todos los pacientes: {resultado_promedio_dias}")
    
    # salida del menu
    else:
        print("nos vemos profe")
        break
        
    pregunta = input("desea seguir ivolver al menu (si/no): ").lower()
    while pregunta != "si" and pregunta != "no":
        pregunta = input("Error, desea volver al menu principal: ").lower()
    if pregunta == "no":
        print("nos vemos profe")
        ingreso = 0