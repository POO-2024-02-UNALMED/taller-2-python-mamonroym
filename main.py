class Asiento():
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor (self, nuevoColor):
        coloresPermitidos = ["rojo","verde","amarillo","negro","blanco"]
        if nuevoColor in coloresPermitidos:
            self.color = nuevoColor
    
class Motor():
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro (self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        tiposPermitidos = ["electrico","gasolina"]
        if nuevoTipo in tiposPermitidos:
            self.tipo = nuevoTipo
    
class Auto():
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos (self):
        contador = 0
        for asiento in self.asientos:
            if asiento is not None:
                contador +=1
        return contador
    
    def verificarIntegridad (self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
                        
        return "Auto original"
