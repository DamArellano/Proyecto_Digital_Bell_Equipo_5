def Menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    Texto = tk.Label(ventana, text = "Bienvenid@ a Digital Bell", font = ("Myanmar Khyay",20))
    Texto.pack(side = tk.TOP, pady = 10)
    Registra = tk.Button(ventana, text = "Crear cuenta", command = lambda: Registro(ventana,Registrar_Usuario), font = ("Myanmar Sans Pro", 15))
    Registra.pack(side = tk.TOP, pady = 10,padx = 10)
    Sesion = tk.Button(ventana, text = "Iniciar Sesión", command = Iniciar_Sesion, font = ("Myanmar Sans Pro", 15))
    Sesion.pack(side = tk.TOP, pady = 10,padx = 10)
    Salir = tk.Button(ventana, text = "Salir", command = ventana.quit, font = ("Myanmar Sans Pro", 15))
    Salir.pack(pady = 5)