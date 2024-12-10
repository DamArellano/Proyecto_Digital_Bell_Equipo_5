import tkinter as tk
from tkinter import messagebox

def crear_interfaz(logica_programa):
    # Creamos la ventana principal
    ventana = tk.Tk()
    ventana.title("Digital Bell")
    ventana.geometry("500x500")
    
    Texto = tk.Label(ventana, text = "Bienvenid@ a Digital Bell", font = ("Myanmar Khyay",20))
    Texto.pack(side = tk.TOP, pady = 10)
    Registra = tk.Button(ventana, text = "Crear cuenta", command = lambda: Registro(ventana,Registrar_Usuario), font = ("Myanmar Sans Pro", 15))
    Registra.pack(side = tk.TOP, pady = 10,padx = 10)
    Sesion = tk.Button(ventana, text = "Iniciar Sesión", command = Iniciar_Sesion, font = ("Myanmar Sans Pro", 15))
    Sesion.pack(side = tk.TOP, pady = 10,padx = 10)
    Salir = tk.Button(ventana, text = "Salir", command = ventana.quit, font = ("Myanmar Sans Pro", 15))
    Salir.pack(pady = 5)

    #La primer función de todas
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
    
    def Registro():
        for widget in ventana.winfo_children:
            widget.destroy()
        
        Texto = tk.Label(ventana, text = "Elija el tipo de usuario a registrar", font = ("Myanmar Khyay",20))
        Texto.pack(pady = 10)
        Habitante = tk.Button(ventana, text = "Habitante", command = lambda: Registrar_Usuario(tipo = "Habitante"), font = ("Myanmar Sans Pro",15))
        Habitante.pack(side = tk.LEFT, padx = 10)
        Empleado = tk.Button(ventana, text = "Empleado", command = lambda: Registrar_Usuario(tipo = "Empleado"), font = ("Myanmar Sans Pro",15))
        Empleado.pack(side = tk.LEFT, padx = 10)
    
    def Registrar_Usuario(tipo):
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Agregar():
            global Usuario,nomos
            if tipo == "Usuario":
                logica_programa["Registro_Habitante"](Nom,Dir,Ne,Ni,Num,Col,Al,Cp,Con,Usuario)
                Menu_Habitante
        
            elif tipo == "Empleado":
                logica_programa["Registro_Empleado"](Nom,Num,Con,Usuario)
                Menu_Empleado
        
            else:
                messagebox.showerror("Digital Bell", "Tipo de usuario no reconocido")

        if tipo == "Habitante":
            Texto = tk.Label(ventana, text = "Ingrese sus datos", font=("Myanmar Khyay", 15))
            Texto.grid(row = 0, column = 0, padx = 10, pady = 10)

            Texto1 = tk.Label(ventana, text = "Nombre Completo:", font=("Myanmar Sans Pro", 10))
            Texto1.grid(row = 1, column = 0, padx = 10, pady = 10)
            Nom = tk.Entry(ventana, width = 30)
            Nom.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto2 = tk.Label(ventana, text = "Calle:", font=("Myanmar Sans Pro", 10))
            Texto2.grid(row = 2, column = 0, padx = 10, pady = 10)
            Dir = tk.Entry(ventana, width = 30)
            Dir.grid(row = 2, column= 1 ,padx = 10, pady = 10, sticky = "w")

            Texto3 = tk.Label(ventana, text = "N° Exterior:", font=("Myanmar Sans Pro", 10))
            Texto3.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
            Ne = tk.Entry(ventana)
            Ne.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "w")
            Texto4 = tk.Label(ventana, text = "N° Interior:", font=("Myanmar Sans Pro", 10))
            Texto4.grid(row = 3, column = 2, padx = 5, pady = 5)
            Ni = tk.Entry(ventana)
            Ni.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "w")

            Texto5 = tk.Label(ventana, text = "Colonia:", font=("Myanmar Sans Pro", 10))
            Texto5.grid(row = 4, column = 0, padx = 10, pady = 10)
            Col = tk.Entry(ventana, width = 30)
            Col.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto6 = tk.Label(ventana, text = "Alcaldia:", font=("Myanmar Sans Pro", 10))
            Texto6.grid(row = 5, column = 0, padx = 10, pady = 10)
            Al = tk.Entry(ventana, width = 30)
            Al.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto7 = tk.Label(ventana, text = "Código Postal:", font=("Myanmar Sans Pro", 10))
            Texto7.grid(row = 6, column = 0, padx = 10, pady = 10)
            Cp = tk.Entry(ventana, width = 30)
            Cp.grid(row = 6, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto8 = tk.Label(ventana, text = "Telefono:", font=("Myanmar Sans Pro", 10))
            Texto8.grid(row = 7, column = 0, padx = 10, pady = 10)
            Num = tk.Entry(ventana, width = 30)
            Num.grid(row = 7, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto9 = tk.Label(ventana, text = "Contraseña:", font=("Myanmar Sans Pro",10))
            Texto9.grid(row = 8, column = 0, padx = 10, pady = 10)
            Con = tk.Entry(ventana, width = 30, show = "*")
            Con.grid(row = 8, column = 1, padx = 10, pady = 10, sticky = "w")

            Registrar = tk.Button(ventana,text = "Ingresar", command = Agregar, font=("Myanmar Sans Pro", 10))
            Registrar.grid(row = 9, column = 0, padx = 10, pady = 10)

            Cancelar = tk.Button(ventana, text = "Cancelar", command = Menu, font=("Myanmar Sans Pro", 10))
            Cancelar.grid(row = 9, column = 1, padx = 10, pady = 10)
    
        elif tipo == "Empleado":
            Texto = tk.Label(ventana, text = "Registro", font=("Myanmar Khyay", 20))
            Texto.grid(row = 0, column = 0, padx = 10, pady = 10)

            Texto1 = tk.Label(ventana, text = "Nombre:", font=("Myanmar Sans Pro",15))
            Texto1.grid(row = 1, column = 0, padx = 10, pady = 10)
            Nom = tk.Entry(ventana, width = 30)
            Nom.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto2 = tk.Label(ventana, text = "Telefono:", font=("Myanmar Sans Pro", 15))
            Texto2.grid(row = 2, column = 0, padx = 10, pady = 10)
            Num = tk.Entry(ventana, width = 30)
            Num.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "w")

            Texto3 = tk.Label(ventana, text = "Número de empleado", font=("Myanmar Sans Pro", 15))
            Texto3.grid(row = 3, column = 0, padx = 10, pady = 10)
            Con = tk.Entry(ventana, width = 30)
            Con.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "w")

            Registrar = tk.Button(ventana,text = "Ingresar", command = Agregar, font=("Myanmar Sans Pro", 15))
            Registrar.grid(row = 4, column = 0, padx = 10, pady = 10)

            Cancelar = tk.Button(ventana, text = "Cancelar", command = Menu, font=("Myanmar Sans Pro", 15))
            Cancelar.grid(row = 4, column = 1, padx = 10, pady = 10)
    
    def Iniciar_Sesion():
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Verificar(Nom, Con, Tipo):
            global Usuario, nomos
            if Tipo == "Usuario":
                for Habitante in Usuario:
                    if Habitante['nombre'] == Nom.get() and Habitante['contraseña'] == Con.get():
                        nomos = Nom.get()
                        messagebox.showinfo("Digital Bell", "Bienvenido " + Nom.get())
                        Menu_Habitante
            

            elif Tipo == "Empleado":
                if Nom.get() == "Arellano" and Con.get() == "1234":
                    nomos = Nom.get()
                    messagebox.showinfo("Digital Bell", "Bienvenido administrador")
                    Menu_Admin
                else:
                    for Empleado in Usuario:
                        if Empleado['nombre'] == Nom.get() and Empleado['contraseña'] == Con.get():
                            nomos = Nom.get()
                            messagebox.showinfo("Digital Bell", "Bienvenido " + Nom.get())
                            Menu_Empleado

        Texto1 = tk.Label(ventana,text = "Ingrese su nombre de usuario", font=("Myanmar Sans Pro", 10))
        Texto1.pack(pady = 5)
        Nom = tk.Entry(ventana)
        Nom.pack(pady = 5)

        Texto2 = tk.Label(ventana, text = "Ingrese su contraseña", font=("Myanmar Sans Pro", 10))
        Texto2.pack(pady= 5)
        Con = tk.Entry(ventana, show = "*")
        Con.pack(pady = 5)

        Texto3 = tk.Label(ventana, text = "Indique su tipo de usuario", font=("Myanmar Sans Pro", 10))
        Texto3.pack(pady = 5)
        Tip = tk.StringVar(ventana)
        Tip.set("")
        Op = ["Empleado","Habitante"]
        Tipo = tk.OptionMenu(ventana, Tip, *Op)
        Tipo.pack(pady = 5)

        Inicio = tk.Button(ventana, text = "Iniciar Sesión", command = lambda: Verificar(Nom, Con,Tipo))
        Inicio.pack(side = tk.TOP, pady = 5)
        Cancelar = tk.Button(ventana, text = "Cancelar", command = Menu, font=("Myanmar Sans Pro", 10))
        Cancelar.pack(side = tk.TOP, pady = 5)
    
    #Aquí se encuentra la parte más "facil" del programa
    #El apartado de los Habitantes comienza aquí
    def Menu_Habitante():

        for widget in ventana.winfo_children():
            widget.destroy()
    
        Texto = tk.Label(ventana, text = ("Bienvenido usuario"), font = ("Myanmar Khyay", 15))
        Texto.pack(side = tk.TOP)

        Sugerencias = tk.Button(ventana, text = "Quejas y Sugerencias", command = Quejas_Habitante, font = ("Myanmar Sans Pro", 10))
        Sugerencias.pack(side = tk.TOP, pady = 10,padx = 10)

        Horarios = tk.Button(ventana, text = "Horarios y rutas del día", command = Horario_Habitante)
        Horarios.pack(side = tk.TOP, pady = 10,padx = 10)

        Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
        Cerrar.pack(side = tk.TOP)
    
    #Para que los Habitantes de la colonia reporten alguna queja con el servicio o quieran enviar alguna sugerencia
    def Quejas_Habitante():
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Guardar_Queja():
            global nomos
            logica_programa["Enviar_Queja"](Sugerencia,nomos,Queja)
            Sugerencia.delete(0, tk.END)
            messagebox.showinfo("Quejas y Sugerencias","Queja registrada exitosamente")

        Texto = tk.Label(ventana, text = ("Quejas y sugerencias"), font = ("Myanmar Khyay", 15))
        Texto.pack(side = tk.TOP, pady = 10)
        Sugerencia = tk.Text(ventana, height = 20, width = 50)
        Sugerencia.pack(side = tk.TOP, pady = 10)
        Enviar = tk.Button(ventana, text = "Enviar queja", command = lambda: Guardar_Queja(Sugerencia))
        Enviar.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Volver al menu", command = "Menu_Habitante")
        Regresar.pack(side = tk.TOP, pady = 10)
    
    def Horario_Habitante():

        for widget in ventana.winfo_children():
            widget.destroy()

        Titulo = tk.Label(ventana, text = "Horarios del día", font = ("Myanmar Khyay", 20))
        Titulo.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Volver al menu", command = Menu_Habitante, font=("Myanmar Sans Pro", 10))
        Regresar.pack(side = tk.TOP, pady = 10)

        Horarios = logica_programa["Ver_Horarios"]
        Horarios = tk.Text(ventana, height=30, width=40)
        Horarios.pack(side = tk.TOP, pady = 10)
        scrollbar = tk.Scrollbar(ventana, command=Horarios.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        Horarios.config(yscrollcommand=scrollbar.set)
    
    #A partir de aquí comienza la sección de empleados
    #Como se puede ver, el empleado solo tendrá una función ya que solo tiene que ver el horario asignado
    def Menu_Empleado():
        for widget in ventana.winfo_children():
            widget.destroy()
        
        Titulo = tk.Label(ventana, text = "Bienvenido Empleado", font = ("Myanmar Khyay", 15))
        Titulo.pack(side = tk.TOP, pady = 10)

        Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
        Cerrar.pack(pady = 10)

        Horarios = logica_programa["Mostrar_Horarios"]
        Horarios = tk.Text(ventana, height=30, width=40)
        Horarios.pack(side = tk.TOP, pady = 10)
        scrollbar = tk.Scrollbar(ventana, command=Horarios.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        Horarios.config(yscrollcommand=scrollbar.set)

    #El apartado del Administrador, de los más dificiles y importantes del programa
    #Aquí depende gran parte del programa que son los horarios
    def Menu_Admin():

        for widget in ventana.winfo_children:
            widget.destroy()
    
        Texto = tk.Label(ventana, text = "Bienvenido Administrador", font = ("Myanmar Khyay", 15))
        Texto.pack(side = tk.TOP, pady = 10)
        Horario = tk.Button(ventana, text = "Horarios", command = Ingresar_Horarios, font = ("Myanmar Sans Pro", 10))
        Horario.pack(side = tk.TOP, pady = 10)
        Actualizar = tk.Button(ventana, text = "Actualizar ubicación", command = Actualizar_Ubicacion, font = ("Myanmar Sans Pro", 10))
        Actualizar.pack(side = tk.TOP, pady = 10)
        Queja = tk.Button(ventana, text = "Quejas y sugerencias", commando = Quejas, font = ("Myanmar Sans Pro", 10))
        Queja.pack(side = tk.TOP, pady = 10)
        Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
        Cerrar.pack(side = tk.TOP, pady = 10)
    
    def Ingresar_Horarios():
        for widget in ventana.winfo_children:
            widget.destroy()
        
        def Asignar_Horarios(Num,Partida,Calle2,Calle3,Calle4):
            logica_programa["Horarios"](Num,Partida,Calle2,Calle3,Calle4)

        #Los horarios de este programa estarán compuestos por tres calles
        Texto = tk.Label(ventana, text = "Horarios y rutas")
        Texto.pack(side = tk.TOP, pady = 10)
        Texto1 = tk.Label(ventana, text = "Número de Empleado a asignar")
        Texto1.pack(side = tk.TOP, pady = 10)
        Num = tk.Entry(ventana)
        Num.pack(side = tk.TOP, pady = 10)
        Texto5 = tk.Label(ventana, text = "¿Por donde va a empezar el recorrido?")
        Texto5.pack(side = tk.TOP, pady = 10)
        Partida = tk.Entry(ventana)
        Partida.pack(side = tk.TOP, pady = 10)
        Texto2 = tk.Label(ventana, text = "Ingrese la segunda dirección")
        Texto2.pack(side = tk.TOP, pady = 10)
        Calle2 = tk.Entry(ventana)
        Calle2.pack(side = tk.TOP, pady = 10)
        Texto3 = tk.Label(ventana, text = "Ingrese la tercera dirección")
        Texto3.pack(side = tk.TOP, pady = 10)
        Calle3 = tk.Entry(ventana)
        Calle3.pack(side = tk.TOP, pady = 10)
        Texto4 = tk.Label(ventana, text = "Ingrese la cuarta dirección")
        Texto4.pack(side = tk.TOP, pady = 10)
        Calle4 = tk.Entry(ventana)
        Calle4.pack(side = tk.TOP, pady = 10)

        Asignar = tk.Button(ventana, text = "Asignar horarios", command = lambda: Asignar_Horarios(Num,Partida,Calle2,Calle3,Calle4))
        Asignar.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Regresar", command = Menu_Admin)
        Regresar.pack(side = tk.TOP, pady = 10)
    
    def Actualizar_Ubicacion():
        for widget in ventana.winfo_children:
            widget.destroy()
        
        def Actualizar(Num,Ubicacion):
            logica_programa["Actualizar_Ubicacion"](Num,Ubicacion)

        Texto = tk.Label(ventana, text = "Ingrese el número de empleado")
        Texto.pack(side = tk.TOP, pady = 10)
        Num = tk.Entry(ventana)
        Num.pack(side = tk.TOP, pady = 10)
        Texto1 = tk.Label(ventana, text = "Ingrese su ubicación actual")
        Texto1.pack(side = tk.TOP, pady = 10)
        Lugar = tk.Text(ventana, height = 5, width = 10)
        Lugar.pack(side = tk.TOP, pady = 10)
        Cambia = tk.Button(ventana, text = "Actualizar ubicación", command = lambda: Actualizar())
        Cambia.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Regresar", command = Menu_Admin)
        Regresar.pack(side = tk.TOP, pady = 10)
    
    #Este es diferente al de Queja_Habitante ya que este en lugar de registrarlas las muestra unicamente al Administrador
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

    #Esta función es exclusivamente para cerrar sesión y volver al menu principal
    def Cerrar_Sesion():
        global nomos
        Cerrar_Sesion = messagebox.askyesno("Digital Bell", "¿Desea cerrar sesión?")
        if Cerrar_Sesion:
            nomos = ""
            Menu()
        else:
            messagebox.showinfo("Digital Bell", "No se pudo cerrar sesión")

    ventana.mainloop()
