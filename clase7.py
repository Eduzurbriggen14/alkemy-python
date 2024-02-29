from enum import Enum

class TipoInstrumento(Enum):
    VIENTO = "Viento"
    CUERDA = "Cuerda"
    PERCUSION = "Percusion"

class Fabrica:
    def __init__(self):
        self.sucursales = []

    def crearSucursal(self, nombre):
        sucursal = Sucursal(nombre)
        self.sucursales.append(sucursal)
        return sucursal

    def listarInstrumentosTotales(self):
        for sucursal in self.sucursales:
            print(f"Instrumentos en: {sucursal.nombre}")
            for instrumento in sucursal.instrumentos:
                print(instrumento)

    def listarInstrumentosPorTipo(self, tipoInstrumento):
        resultado = []
        for sucursal in self.sucursales:
            instrumentos_tipo = [instrumento for instrumento in sucursal.instrumentos if instrumento.tipo == tipoInstrumento.value]
            resultado.extend(instrumentos_tipo)
        return resultado

    def borrarInstrumento(self, id):
        for sucursal in self.sucursales:
            sucursal.instrumentos = [instrumento for instrumento in sucursal.instrumentos if instrumento.id != id]

    def porcInstrumentoPorTipo(self):
        pass

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

class Instrumento:
    def __init__(self, id, precio, tipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipo = tipoInstrumento

    def __str__(self):
        return f"Id: {self.id}, Precio: {self.precio}, Tipo: {self.tipo}"

# Crear fabrica
fabrica = Fabrica()

# Crear sucursales y agregar instrumentos
sucursal1 = fabrica.crearSucursal("Sucursal A")
sucursal1.agregarInstrumento(Instrumento("1", 500, TipoInstrumento.CUERDA))
sucursal1.agregarInstrumento(Instrumento("2", 700, TipoInstrumento.VIENTO))

sucursal2 = fabrica.crearSucursal("Sucursal B")
sucursal2.agregarInstrumento(Instrumento("3", 300, TipoInstrumento.CUERDA))

sucursal3 = fabrica.crearSucursal("Sucursal C")
sucursal3.agregarInstrumento(Instrumento("4", 400, TipoInstrumento.PERCUSION))
sucursal3.agregarInstrumento(Instrumento("5", 600, TipoInstrumento.VIENTO))

sucursal4 = fabrica.crearSucursal("Sucursal D")
sucursal4.agregarInstrumento(Instrumento("6", 200, TipoInstrumento.CUERDA))

sucursal5 = fabrica.crearSucursal("Sucursal E")
sucursal5.agregarInstrumento(Instrumento("7", 800, TipoInstrumento.PERCUSION))
sucursal5.agregarInstrumento(Instrumento("8", 1000, TipoInstrumento.CUERDA))

sucursal6 = fabrica.crearSucursal("Sucursal F")
sucursal6.agregarInstrumento(Instrumento("9", 900, TipoInstrumento.VIENTO))
sucursal6.agregarInstrumento(Instrumento("10", 1200, TipoInstrumento.PERCUSION))

# Listar instrumentos totales
print("Listar Instrumentos Totales:")
fabrica.listarInstrumentosTotales()

# Listar instrumentos de tipo 'Cuerda'
print("\nListar Instrumentos de tipo 'Cuerda':")
cuerda_instrumentos = fabrica.listarInstrumentosPorTipo(TipoInstrumento.CUERDA)
for instrumento in cuerda_instrumentos:
        print(instrumento)



# Borrar instrumento con ID 'I001'
print("\nBorrar Instrumento con ID 'I001':")
fabrica.borrarInstrumento("I001")
fabrica.listarInstrumentosTotales()