def Menu_Empleado():
    global Usuario,nomos

    for widget in ventana.winfo_children():
        widget.destroy()
    
    Texto = tk.Label(ventana, text = ("Bienvenido ",nomos), font = ("Myanmar Khyay", 15))
    Texto.pack(side = tk.TOP, pady = 10)
    
    for Horario['nombre'] in Horario:
        if Horario['nombre'] == nomos:
            Texto2 = tk.Label(ventana, text = ("Hora de salida: ",Horario['Salida']), font = ("Myanmar Sans Pro", 10))
            Texto2.pack(side = tk.TOP)
            Texto3 = tk.Label(ventana, text = "Horario:", font = ("Myanmar Sans Pro", 10))
            Texto3.pack(side = tk.TOP)
            Ruta = tk.Text(ventana, height = 20, width = 40, font = ("Myanmar Sans Pro", 10))
            Ruta.insert(tk.END, Horario['Ruta'])
            Ruta.config(state = tk.DISABLED)
            Ruta.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            Barra = tk.Scrollbar(ventana, command = Ruta.yview)
            Barra.pack(side = tk.RIGHT, fill = tk.Y)
    
    Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
    Cerrar.pack(pady = 10)

def Cerrar_Sesion():
    global nomos
    Cerrar_Sesion = messagebox.askyesno("Digital Bell", "¿Desea cerrar sesión?")
    if Cerrar_Sesion:
        nomos = ""
        Menu()
    else:
        messagebox.showinfo("Digital Bell", "No se pudo cerrar sesión")