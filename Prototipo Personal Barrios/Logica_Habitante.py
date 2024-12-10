def Registrar_Habitante(Nom,Dir,Ne,Ni,Num,Col,Al,Cp,Con,Usuario):
    Nombre = Nom.get()
    Direccion = Dir.get()
    Numero_Exterior = Ne.get()
    if Ni != "":
        Numero_Interior = Ni.get()
    else:
        Numero_Interior = ""
    Telefono = Num.get()
    Colonia = Col.get()
    Alcaldia = Al.get()
    Codigo_Postal = Cp.get()
    Contraseña = Con.get()

    Habitante = {
        "Nombre": Nombre,
        "Direccion": Direccion,
        "Numero Exterior": Numero_Exterior,
        "Numero Interior": Numero_Interior,
        "Telefono": Telefono,
        "Colonia": Colonia,
        "Alcaldia": Alcaldia,
        "Codigo Postal": Codigo_Postal,
        "Contraseña": Contraseña
    }

    Usuario.append(Habitante)

def QuejaHa(Sugerencia,nomos,Queja):
    Sug = Sugerencia.get()
    Usuario = nomos
    Sugerencia = {
        "Usuario": Usuario,
        "Queja": Sug
    }
    Queja.append(Sugerencia)

def Mostrar_Horarios(Horario,Horarios):
    if not Horario:
        Horarios.insert("No hay horarios al momento")
    else:
        for Ruta in Horario:
            Horarios.insert(str(Ruta) + "\n")