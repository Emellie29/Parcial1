empleados={}
while True:
    print("Recursos Humanos")
    print("1. Ingresar empleado")
    print("2. Desempeño del empleado")
    print("3. informacion del empleado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        class empleado():
                cantidad = int(input("¿Cuantos empleados desea ingresar?: "))
                for i in range(cantidad):
                    print(f"\nEmpleado No.{i + 1}")
                    codigo = input("Codigo de empleado: ")
                    nombre = input("Nombre completo del empleado: ")
                    departamento = input("Departamento dónde se desempeña el empleado: ")
                    antiguedad = int(input("Cuantos años de antiguedad tiene trabajando: "))
                    telefono=int(input("Ingrese el número de teléfono del empleado: "))
                    correo=input("ingrese el correo electrónico del empleado: ")
                    print(f"Empleado registrado con exito.")
                else:
                    print("El empleado no existe")
                empleados = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "departamento": departamento,
                    "antiguedad": antiguedad,
                    "evaluacion":{},
                    "contacto":{}
                }
                empleados["contacto"]: {
                    "telefono": telefono,
                    "correo": correo,
                }
    elif opcion == "2":
        class evaluacion():
                print(f"Evaluacion del empleado")
                codigo = input("Ingrese código que desea buscar: ")
                if(codigo in empleados):
                    empleado = empleados[codigo]
                    print(f"Nombre: {empleado['nombre']}")
                    print(f"Departamento: {empleado['departamento']}")
                    print(f"Años de antiguedad: {empleado['antiguedad']}")
                    print(f"Número de teléfono: {empleado['telefono']}")
                    print(f"Correo electrónico: {empleado['correo']}")
                    print(f"Ingrese la evaluacion del empleado.")
                    puntualidad=int(input("Ingrese la puntualidad: "))
                    for i in 0<=puntualidad<=10:
                        print(f"Nota ingresada correctamente: {i}")
                    equipo = int(input("Ingrese la puntualidad: "))
                    for i in 0 <= equipo <= 10:
                        print(f"Nota ingresada correctamente: {i}")
                    productividad = int(input("Ingrese la puntualidad: "))
                    for i in 0 <= productividad <= 10:
                        print(f"Nota ingresada correctamente: {i}")
                    observaciones =input("Ingrese las observaciones del empleado: ")
                    promedio= puntualidad*equipo*productividad/3
                    estado=print("El estado del empleado es: ")
                    for i in 0 <= promedio <= 6:
                        print(f"Debe mejorar")
                    for i in 7 <= promedio <= 10:
                        print(f"Satisfactorio")
                else:
                    print("El empleado no existe")
                empleados["evaluacion"]: {
                    "codigo": codigo,
                    "puntualidad": puntualidad,
                    "equipo": equipo,
                    "productividad": productividad,
                    "observaciones": observaciones,
                    "promedio": promedio,
                    "estado": estado,
                }
    elif opcion == "3":
        class informacion():
            print("Información del Empleado:")
            for codigo, datos in empleados.items():
                print(f"\nCodigo: {codigo}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Departamento: {datos['departamento']}")
                print(f"Antiguedad: {datos['antiguedad']}")
                print(f"Puntualidad: {datos['evaluacion']['puntualidad']}")
                print(f"Equipo: {datos['evaluacion']['equipo']}")
                print(f"Productividad: {datos['evaluacion']['productividad']}")
                print(f"Observaciones: {datos['evaluacion']['observaciones']}")
                print(f"Promedio: {datos['evaluacion']['promedio']}")
                print(f"Estado: {datos['evaluacion']['estado']}")
                print(f"Teléfono: {datos['contacto']['telefono']}")
                print(f"Correo: {datos['contacto']['correo']}")
    elif opcion == "4":
        print("Cerrando Sesión.")
        break

