empleados={}
class Informacion:
    def __init__(self, codigo, nombre, departamento, antiguedad, telefono, correo):
        self.identidad = {
            "codigo": codigo,
            "nombre": nombre,
            "departamento": departamento,
            "antiguedad": antiguedad
        }
        self.contacto = {
            "telefono": telefono,
            "correo": correo
        }
class Evaluacion:
    def __init__(self, puntualidad, equipo, productividad, observaciones):
        promedio = (puntualidad + equipo + productividad) / 3
        if 0 <= promedio <= 6:
            estado = "Debe mejorar"
        elif 7 <= promedio <= 10:
            estado = "Satisfactorio"
        else:
            estado = "Valor fuera de rango"
        self.datos={
            "puntualidad": puntualidad,
            "equipo": equipo,
            "productividad": productividad,
            "observaciones": observaciones,
            "promedio": promedio,
            "estado": estado
        }
class Empleado:
    def __init__(self, info: Informacion):
        self.identidad=info.identidad
        self.contacto=info.contacto
        self.evaluacion={}
    def registrar(self, puntualidad,equipo,productividad,observaciones):
        evaluacion=Evaluacion(puntualidad,equipo,productividad,observaciones)
        self.evaluacion=evaluacion.datos
    def mostrar(self):
        print("Datos del Empleado")
        for clave, valor in self.identidad.items():
            print(f"{clave.capitalize()}: {valor}")
        print("Contacto")
        for clave, valor in self.contacto.items():
            print(f"{clave.capitalize()}: {valor}")
        print("Evaluacion")
        if self.evaluacion:
            for clave, valor in self.evaluacion.items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print("Pendiente de Evaluar.")
while True:
    print("Recursos Humanos")
    print("1. Ingresar empleado")
    print("2. Desempeño del empleado")
    print("3. informacion del empleado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = int(input("¿Cuantos empleados desea ingresar?: "))
        for i in range(cantidad):
            print(f"\nEmpleado No.{i + 1}")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            departamento = input("Departamento: ")
            antiguedad = int(input("Años de antigüedad: "))
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            info = Informacion(codigo, nombre, departamento, antiguedad, telefono, correo)
            empleados[codigo] = Empleado(info)
            print("Empleado registrado con exito.")
    elif opcion == "2":
        codigo = input("Código del empleado: ")
        emp = empleados.get(codigo)
        if emp:
            puntualidad = int(input("Puntualidad: "))
            equipo = int(input("Trabajo en equipo: "))
            productividad = int(input("Productividad: "))
            observaciones = input("Observaciones: ")
            emp.registrar(puntualidad, equipo, productividad, observaciones)
            print("Evaluación guardada.")
            print(f"Promedio: {emp.evaluacion['promedio']}")
            print(f"Estado: {emp.evaluacion['estado']}")
        else:
            print("Empleado no encontrado.")
    elif opcion == "3":
        for emp in empleados.values():
            emp.mostrar()
        if not empleados:
            print("No hay empleados registrados.")
    elif opcion == "4":
        print("Cerrando Sesión.")
        break
    else:
        print("Opcion no valida, intente de nuevo.")