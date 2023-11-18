class Usuario:
    def __init__(self) -> None:
        pass

    def capturar (self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
    
    def imprimir(self):
        print(  f"Estos son sus datos:\n"
                f"    nombre: {self.nombre}\n"
                f"    telefono: {self.tel}\n"
                f"    direccion: {self.direccion}")
    
    def modificar(self, opc, editable):
        if   (opc == 1):
            self.nombre = editable
        elif (opc == 2):
            self.direccion = editable
        elif (opc == 3):
            self.tel = editable