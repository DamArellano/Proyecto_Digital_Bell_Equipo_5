def Registrar_Empleado(Nom,Num,Con,Usuario):
    Nombre = Nom.get()
    Telefono = Num.get()
    Numero_Empleado = Con.get()

    Empleado = {
        "Nombre": Nombre,
        "Telefono" : Telefono,
        "Contraseña": Numero_Empleado
    }

    Usuario.append(Empleado)