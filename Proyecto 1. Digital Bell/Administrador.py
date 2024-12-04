def Menu_Admin():
    global Usuario,nomos

    for widget in ventana.winfo_children:
        widget.destroy()
    
    Texto = tk.Label(ventana, text = "Bienvenido Administrador", font = ("Myanmar Khyay", 15))
    Texto.pack(side = tk.TOP, pady = 10)
    Horario = tk.Button(ventana, text = "Horarios", command = Ingresar_Horarios, font = ("Myanmar Sans Pro", 10))
    Horario.pack(side = tk.TOP, pady = 10)
    Actualizar = tk.Button(ventana, text = "Actualizar ubicación", command = Actualizar_Ubiacion, font = ("Myanmar Sans Pro", 10))
    Actualizar.pack(side = tk.TOP, pady = 10)
    Queja = tk.Button(ventana, text = "Quejas y sugerencias", commando = Quejas, font = ("Myanmar Sans Pro", 10))
    Queja.pack(side = tk.TOP, pady = 10)
    Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
    Cerrar.pack(side = tk.TOP, pady = 10)

#Para horarios se requiere: Grafos

def Quejas():
    global Queja

    for widget in ventana.winfo_children:
        widget.destroy()
    
    Titulo = tk.Label(ventana, text = "Quejas y sugerencias")
    Titulo.pack(side = tk.TOP)
    if not Queja:
        Texto = tk.Label(ventana, text = "No hay quejas por el momento")
        Texto.pack(side = tk.TOP, pady = 10)
    else:
        for Sugerencia in Queja:
            Nombre = tk.Label(ventana, text = (Sugerencia['Usuario']))
            Nombre.pack(side = tk.TOP, pady = 10)
            Problema = tk.Label(ventana, text = (Sugerencia['Queja']))
            Problema.pack(side = tk.TOP, pady = 10)
    Regresar = tk.Button(ventana, text = "Volver al menu", command = Menu_Admin)
    Regresar.pack(side = tk.TOP, pady = 10)

def Cerrar_Sesion():
    global nomos
    Cerrar_Sesion = messagebox.askyesno("Digital Bell", "¿Desea cerrar sesión?")
    if Cerrar_Sesion:
        nomos = ""
        Menu()
    else:
        messagebox.showinfo("Digital Bell", "No se pudo cerrar sesión")