from enum import Enum

empleadosPorComision = []
empleadosFijo= []

class TipoContrato(Enum):
    FIJO = "Salario fijo"
    COMI = "Por comisión"

class Antiguedad(Enum):
    CAT1 = "menos de 2 años"
    CAT2 = "entre 2 y 5 años"
    CAT3 = "mayor a 5 años"

class Empleado:
    def __init__(self, nombre, apellido, dni, anioIngreso, tipoContrato):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.anioIngreso = anioIngreso
        self.tipoContrato = tipoContrato

    def calcularSalario(self):
        pass

class PorComision(Empleado):
    def __init__(self, nombre, apellido, dni, anioIngreso, tipoContrato, salarioMinimo, clientesCaptados, montoPorClientes):
        super().__init__(nombre, apellido, dni, anioIngreso, tipoContrato)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorClientes = montoPorClientes

    def calcularSalario(self):
        salarioTotal = self.clientesCaptados * self.montoPorClientes
        return salarioTotal

    
    def mostrarSalario(self):
        if self.calcularSalario() < self.salarioMinimo:
            return f"El empleado {self.nombre} cobrará este mes: {self.salarioMinimo}"
        else:
            return f"El empleado {self.nombre} {self.apellido} cobrará este mes: {self.calcularSalario()}"

    def empleadoConMasClientes(empleados):
        empleadoMaxClientes = None
        maxClientes = -1

        for empleado in empleados:
            if empleado.clientesCaptados > maxClientes:
                maxClientes = empleado.clientesCaptados
                empleadoMaxClientes = empleado

        return empleadoMaxClientes

class SalarioFijo(Empleado):
    def __init__(self, nombre, apellido, dni, anioIngreso, tipoContrato, sueldoBasico, porcAntiguedad, antiguedad):
        super().__init__(nombre, apellido, dni, anioIngreso, tipoContrato)
        self.sueldoBasico = sueldoBasico
        self.porcAntiguedad = porcAntiguedad
        self.antiguedad = antiguedad

    def calcularSalario(self):
        if self.antiguedad == Antiguedad.CAT1:
            salarioTotal = self.sueldoBasico
        elif self.antiguedad == Antiguedad.CAT2:
            salarioTotal = self.sueldoBasico + self.sueldoBasico * 0.05
        elif self.antiguedad == Antiguedad.CAT3:
            salarioTotal = self.sueldoBasico + self.sueldoBasico * 0.1
        else:
            salarioTotal = 0
        
        return salarioTotal

    def mostrarSalarios(self):
        return f"El empleado {self.nombre} {self.apellido} cobrará este mes: ${self.calcularSalario()}"


def agregarEmpleadoPorComision(nombre, apellido, dni, anioIngreso, tipoContrato, salarioMinimo, clientesCaptados, montoPorClientes):
    nuevo_empleado = PorComision(nombre, apellido, dni, anioIngreso, tipoContrato, salarioMinimo, clientesCaptados, montoPorClientes)
    empleadosPorComision.append(nuevo_empleado)
    return nuevo_empleado

agregarEmpleadoPorComision("Juan", "Pérez", "123456789", 2019, TipoContrato.COMI.value, 1000, 15, 50)
agregarEmpleadoPorComision("María", "López", "987654321", 2018, TipoContrato.COMI.value, 1200, 20, 60)
agregarEmpleadoPorComision("Carlos", "Gómez", "456789012", 2020, TipoContrato.COMI.value, 800, 10, 40)
agregarEmpleadoPorComision("Laura", "Rodríguez", "789012345", 2017, TipoContrato.COMI.value, 1500, 25, 55)
agregarEmpleadoPorComision("Ana", "Martínez", "543210987", 2021, TipoContrato.COMI.value, 1100, 18, 48)


fijo1 = SalarioFijo("Pedro", "Sánchez", "234567890", 2016, TipoContrato.FIJO.value, 2000, 0.1, Antiguedad.CAT3)
fijo2 = SalarioFijo("Elena", "García", "678901234", 2015, TipoContrato.FIJO.value, 1800, 0.05, Antiguedad.CAT2)
fijo3 = SalarioFijo("Sergio", "Hernández", "890123456", 2019, TipoContrato.FIJO.value, 2200, 0.15, Antiguedad.CAT3)
fijo4 = SalarioFijo("Isabel", "Díaz", "345678901", 2018, TipoContrato.FIJO.value, 1900, 0.08, Antiguedad.CAT2)
fijo5 = SalarioFijo("Marta", "Luna", "012345678", 2017, TipoContrato.FIJO.value, 2100, 0.12, Antiguedad.CAT3)

empleadosFijo = [fijo1, fijo2, fijo3, fijo4, fijo5]

print("\n")
print("Salarios empleados a sueldo Fijo: ")
for empleado in empleadosFijo:
    salario = empleado.mostrarSalarios()
    print(salario)
print("---------------")
print("Salarios de empleados con sueldo a comision: ")
for empleado in empleadosPorComision:
    salario = empleado.mostrarSalario()
    print(salario)

empleadoComisionMasClientes = PorComision.empleadoConMasClientes(empleadosPorComision)

print("---------------")
print("El empleado que mas clientes tiene captado es: ")
if empleadoComisionMasClientes:
    print(f"El empleado por comisión con más clientes es {empleadoComisionMasClientes.nombre} {empleadoComisionMasClientes.apellido} con {empleadoComisionMasClientes.clientesCaptados} clientes.")
else:
    print("No hay empleados por comisión registrados.")