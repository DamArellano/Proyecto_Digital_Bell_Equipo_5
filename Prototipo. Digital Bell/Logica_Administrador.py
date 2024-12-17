def AsH(Num,Partida,Calle2,Calle3,Calle4,Horario):
    Numero = Num.get()
    Ubicacion = Partida.get()
    Dir1 = Calle2.get()
    Dir2 = Calle3.get()
    Dir3 = Calle4.get()
    Ruta = {
        "Empleado": Numero,
        "Ubicacion": Ubicacion,
        "Direccion1": Dir1,
        "Direccion2": Dir2,
        "Direccion3": Dir3
    }

    Horario.append(Ruta)

def Ubicacion(Num,Ubicacion,Horario):
    Ruta = Ruta.get()
    Numero = Num.get()
    Ubicacion = Ubicacion.get()
    for Ruta in Horario:
        if Ruta["Empleado"] == Numero:
            Ruta["Ubicacion"] = Ubicacion
    return