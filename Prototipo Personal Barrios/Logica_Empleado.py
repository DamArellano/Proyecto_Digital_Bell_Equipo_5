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

def Mostrar_Horarios(Horario,Horarios,nomos):
    for Ruta in Horario:
        if Ruta["Nombre"] == nomos:
            Horarios.insert(str(Ruta) + "\n")