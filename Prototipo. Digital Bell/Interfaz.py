import tkinter as tk
from tkinter import messagebox,ttk
Usuario = []
Queja = []
Horario = []
nomos = ""

def crear_interfaz(logica_programa):
    # Creamos la ventana principal
    ventana = tk.Tk()
    ventana.title("Digital Bell")
    ventana.geometry("500x500")
    ventana.configure(bg="#6699CC")

    #La primer función de todas
    def Menu():
        for widget in ventana.winfo_children():
            widget.destroy()
        # Sección delimitada para el menú principal
        menu_frame = tk.Frame(ventana, bg="white", bd=3, relief="solid")
        menu_frame.pack(pady=10, padx=10, expand=True)

        Texto = tk.Label(menu_frame, text="BIENVENID@ A DIGITAL BELL", font=("Myanmar Khyay", 20), bg="white")
        Texto.pack(side=tk.TOP, pady=10)

        Registra = tk.Button(menu_frame, text="Crear cuenta", command=Registro, font=("Myanmar Sans Pro", 15), bg="green",fg="white")
        Registra.pack(side=tk.TOP, pady=(180,10), padx=10)

        Sesion = tk.Button(menu_frame, text="Iniciar Sesión", command=Iniciar_Sesion, font=("Myanmar Sans Pro", 15), bg="green",fg="white")
        Sesion.pack(side=tk.TOP, pady=10, padx=10)

        Salir = tk.Button(menu_frame, text="Salir", command=ventana.quit, font=("Myanmar Sans Pro", 15), bg="red",fg="white")
        Salir.pack(pady=5)
    
    def Registro():

        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana)
        frame.pack(pady=20, padx=20)  # Espaciado alrededor del frame

        # Agregar widgets al frame
        Texto = tk.Label(frame, text="Elija el tipo de usuario a registrar", font=("Myanmar Khyay", 20))
        Texto.pack(pady=10)

        # Crear un sub-frame para los botones de "Habitante" y "Empleado"
        botones_frame = tk.Frame(frame)
        botones_frame.pack(pady=10)

        Habitante = tk.Button(botones_frame, text="Habitante", command=lambda: Registrar_Usuario(tipo="Habitante"), font=("Myanmar Sans Pro", 15))
        Habitante.pack(side=tk.LEFT, padx=50)

        Empleado = tk.Button(botones_frame, text="Empleado", command=lambda: Registrar_Usuario(tipo="Empleado"), font=("Myanmar Sans Pro", 15))
        Empleado.pack(side=tk.RIGHT, padx=50)
    
    
    def Registrar_Usuario(tipo):
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Agregar():
            global Usuario,nomos
            if tipo == "Habitante":
                Nombre = Nom.get()
                Direccion = Dir.get()
                Nume = Ne.get()
                Numero = Num.get()
                Colonia = Col.get()
                Alcaldia = Al.get()
                Copo = Cp.get()
                Contraseña = Con.get()
                if not Nombre or not Direccion  or not Nume or not Numero or not Colonia or not Alcaldia or not Copo or not Contraseña:
                    messagebox.showerror("Error", "Por favor, complete todos los campos")
                else:
                    nomos = Nom.get()
                    logica_programa["Registro_Habitante"](Nom,Dir,Ne,Ni,Num,Col,Al,Cp,Con,Usuario)
                    Menu_Habitante()
        
            elif tipo == "Empleado":
                Nombre = Nom.get()
                Numero = Num.get()
                Contraseña = Con.get()
                if not Nombre or not Numero or not Contraseña:
                    messagebox.showerror("Error", "Por favor, complete todos los campos")
                else:
                    nomos = Num.get()
                    logica_programa["Registro_Empleado"](Nom,Num,Con,Usuario)
                    Menu_Empleado()
        
            else:
                messagebox.showerror("Digital Bell", "Tipo de usuario no reconocido")

        if tipo == "Habitante":
            # Destruir todos los widgets existentes en la ventana
            # Destruir todos los widgets existentes en la ventana
            for widget in ventana.winfo_children():
                widget.destroy()

            # Configurar la ventana para centrar el frame
            ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
            ventana.grid_rowconfigure(2, weight=1)
            ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico a la izquierda y derecha
            ventana.grid_columnconfigure(2, weight=1)

            # Crear un frame dentro de la ventana
            frame = tk.Frame(ventana, bg="white", bd=2, relief="solid")  # Bordes para simular un recuadro
            frame.grid(row=1, column=1, padx=20, pady=20)  # Centrado en el medio

            # Agregar widgets al frame
            Texto = tk.Label(frame, text="Ingrese sus datos", font=("Myanmar Khyay", 15), bg="white")
            Texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            Texto1 = tk.Label(frame, text="Nombre Completo:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto1.grid(row=1, column=0, padx=10, pady=10)
            Nom = tk.Entry(frame, width=30)
            Nom.grid(row=1, column=1, padx=10, pady=10, sticky="w")

            Texto2 = tk.Label(frame, text="Calle:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto2.grid(row=2, column=0, padx=10, pady=10)
            Dir = tk.Entry(frame, width=30)
            Dir.grid(row=2, column=1, padx=10, pady=10, sticky="w")

            Texto3 = tk.Label(frame, text="N° Exterior:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto3.grid(row=3, column=0, padx=5, pady=5)
            Ne = tk.Entry(frame)
            Ne.grid(row=3, column=1, padx=5, pady=5, sticky="w")

            Texto4 = tk.Label(frame, text="N° Interior:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto4.grid(row=4, column=0, padx=5, pady=5)
            Ni = tk.Entry(frame)
            Ni.grid(row=4, column=1, padx=5, pady=5, sticky="w")

            Texto5 = tk.Label(frame, text="Colonia:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto5.grid(row=5, column=0, padx=10, pady=10)
            Col = tk.Entry(frame, width=30)
            Col.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            Texto6 = tk.Label(frame, text="Alcaldia:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto6.grid(row=6, column=0, padx=10, pady=10)
            Al = tk.Entry(frame, width=30)
            Al.grid(row=6, column=1, padx=10, pady=10, sticky="w")

            Texto7 = tk.Label(frame, text="Código Postal:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto7.grid(row=7, column=0, padx=10, pady=10)
            Cp = tk.Entry(frame, width=30)
            Cp.grid(row=7, column=1, padx=10, pady=10, sticky="w")

            Texto8 = tk.Label(frame, text="Teléfono:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto8.grid(row=8, column=0, padx=10, pady=10)
            Num = tk.Entry(frame, width=30)
            Num.grid(row=8, column=1, padx=10, pady=10, sticky="w")

            Texto9 = tk.Label(frame, text="Contraseña:", font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Texto9.grid(row=9, column=0, padx=10, pady=10)
            Con = tk.Entry(frame, width=30, show="*")
            Con.grid(row=9, column=1, padx=10, pady=10, sticky="w")

            Registrar = tk.Button(frame, text="Ingresar", command=Agregar, font=("Myanmar Sans Pro", 10), bg="green", fg="white")
            Registrar.grid(row=10, column=0, padx=10, pady=10)

            Cancelar = tk.Button(frame, text="Cancelar", command=Menu, font=("Myanmar Sans Pro", 10), bg="red", fg="white")
            Cancelar.grid(row=10, column=1, padx=10, pady=10)

    
        elif tipo == "Empleado":
            # Destruir todos los widgets existentes en la ventana
            for widget in ventana.winfo_children():
                widget.destroy()

            # Configurar la ventana para centrar el frame
            ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
            ventana.grid_rowconfigure(2, weight=1)
            ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha
            ventana.grid_columnconfigure(2, weight=1)

            # Crear un frame dentro de la ventana
            frame = tk.Frame(ventana, bg="white", bd=2, relief="solid")  # Bordes para simular un recuadro
            frame.grid(row=1, column=1, padx=20, pady=20)  # Centrado en la ventana

            # Agregar widgets al frame
            Texto = tk.Label(frame, text="Registro", font=("Myanmar Khyay", 20), bg="white")
            Texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            Texto1 = tk.Label(frame, text="Nombre:", font=("Myanmar Sans Pro", 15), bg="green", fg="white")
            Texto1.grid(row=1, column=0, padx=10, pady=10)
            Nom = tk.Entry(frame, width=30)
            Nom.grid(row=1, column=1, padx=10, pady=10, sticky="w")

            Texto2 = tk.Label(frame, text="Teléfono:", font=("Myanmar Sans Pro", 15), bg="green", fg="white")
            Texto2.grid(row=2, column=0, padx=10, pady=10)
            Num = tk.Entry(frame, width=30)
            Num.grid(row=2, column=1, padx=10, pady=10, sticky="w")

            Texto3 = tk.Label(frame, text="Número de empleado:", font=("Myanmar Sans Pro", 15), bg="green", fg="white")
            Texto3.grid(row=3, column=0, padx=10, pady=10)
            Con = tk.Entry(frame, width=30)
            Con.grid(row=3, column=1, padx=10, pady=10, sticky="w")

            Registrar = tk.Button(frame, text="Ingresar", command=Agregar, font=("Myanmar Sans Pro", 15), bg="green", fg="white")
            Registrar.grid(row=4, column=0, padx=10, pady=10)

            Cancelar = tk.Button(frame, text="Cancelar", command=Menu, font=("Myanmar Sans Pro", 15), bg="red", fg="white")
            Cancelar.grid(row=4, column=1, padx=10, pady=10)

    
    def Iniciar_Sesion():
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Verificar(Nom, Con, Tip):
            global Usuario, nomos
            Tipo_Usuario = Tip.get()
            Nombre = Nom.get()
            Contrasena = Con.get()

            if Tipo_Usuario == "Habitante":
                for Habitante in Usuario:
                    if Habitante['Nombre'] == Nombre and Habitante['Contraseña'] == Contrasena:
                        nomos = Nombre
                        messagebox.showinfo("Digital Bell", "Bienvenido " + Nombre)
                        Menu_Habitante()
                        return
            

            elif Tipo_Usuario == "Empleado":
                if Nombre == "Arellano" and Contrasena == "1234":
                    nomos = Nombre
                    messagebox.showinfo("Digital Bell", "Bienvenido administrador")
                    Menu_Admin()
                else:
                    for Empleado in Usuario:
                        if Empleado['Nombre'] == Nombre and Empleado['Contraseña'] == Contrasena:
                            nomos = Nombre
                            messagebox.showinfo("Digital Bell", "Bienvenido " + Nombre)
                            Menu_Empleado()
                            return
        #                
        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha
        ventana.grid_columnconfigure(2, weight=1)

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=400, height=300)  # Tamaño más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes mayores
        frame.grid_propagate(False)  # Evita que el frame se ajuste al contenido

        # Agregar widgets al frame
        Texto1 = tk.Label(frame, text="Ingrese su nombre de usuario", font=("Myanmar Sans Pro", 10), bg="white", fg="black")
        Texto1.pack(pady=10)  # Más espacio vertical
        Nom = tk.Entry(frame, width=40)  # Entrada más ancha
        Nom.pack(pady=10)

        Texto2 = tk.Label(frame, text="Ingrese su contraseña", font=("Myanmar Sans Pro", 10), bg="white", fg="black")
        Texto2.pack(pady=10)
        Con = tk.Entry(frame, show="*", width=40)
        Con.pack(pady=10)

        Texto3 = tk.Label(frame, text="Indique su tipo de usuario", font=("Myanmar Sans Pro", 10), bg="white", fg="black")
        Texto3.pack(pady=10)
        Tip = tk.StringVar(ventana)
        Tip.set("Usuario")
        Op = ["Empleado", "Habitante"]
        Tipo = tk.OptionMenu(frame, Tip, *Op)
        Tipo.pack(pady=10)

        Inicio = tk.Button(frame, text="Iniciar Sesión", command=lambda: Verificar(Nom, Con, Tip), bg="green", fg="white", width=20)
        Inicio.pack(pady=10)

        Cancelar = tk.Button(frame, text="Cancelar", command=Menu, font=("Myanmar Sans Pro", 10), bg="red", fg="white", width=20)
        Cancelar.pack(pady=10)


    
    #Aquí se encuentra la parte más "facil" del programa
    #El apartado de los Habitantes comienza aquí
    def Menu_Habitante():

        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha
        ventana.grid_columnconfigure(2, weight=1)

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=1000, height=700)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Texto = tk.Label(frame, text="Bienvenido usuario", font=("Myanmar Khyay", 15), bg="white")
        Texto.pack(side=tk.TOP, pady=25)  # Espaciado mayor

        Sugerencias = tk.Button(frame, text="Quejas y Sugerencias", command=Quejas_Habitante, font=("Myanmar Sans Pro", 12), bg="green", fg="white")
        Sugerencias.pack(side=tk.TOP, pady=25, padx=25)

        Horarios = tk.Button(frame, text="Horarios y rutas del día", command=Horario_Habitante, bg="green", fg="white")
        Horarios.pack(side=tk.TOP, pady=25, padx=25)

        Cerrar = tk.Button(frame, text="Cerrar Sesión", command=Cerrar_Sesion, bg="red", fg="white")
        Cerrar.pack(side=tk.TOP, pady=25, padx=25)
    
    #Para que los Habitantes de la colonia reporten alguna queja con el servicio o quieran enviar alguna sugerencia
    def Quejas_Habitante():
        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Guardar_Queja():
            global nomos
            Sug = Sugerencia.get("1.0", tk.END).strip()
            logica_programa["Enviar_Queja"](Sug,nomos,Queja)
            messagebox.showinfo("Quejas y Sugerencias","Queja registrada exitosamente")
            Menu_Habitante()

        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(3, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha
        ventana.grid_columnconfigure(3, weight=1)

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=700, height=500)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Texto = tk.Label(frame, text="Quejas y sugerencias", font=("Myanmar Khyay", 15), bg="white")
        Texto.pack(side=tk.TOP, pady=25)  # Espaciado mayor

        Sugerencia = tk.Text(frame, height=15, width=40)  # Aumento del tamaño del área de texto
        Sugerencia.pack(side=tk.TOP, pady=25)

        Enviar = tk.Button(frame, text="Enviar queja", command=Guardar_Queja, bg="green", fg="white")
        Enviar.pack(side=tk.TOP, pady=25)

        Regresar = tk.Button(frame, text="Volver al menu", command=Menu_Habitante, bg="red", fg="white")
        Regresar.pack(side=tk.TOP, pady=25)

    
    def Horario_Habitante():

        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha
        ventana.grid_columnconfigure(2, weight=1)

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=700, height=500)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Titulo = tk.Label(frame, text="Horarios del día", font=("Myanmar Khyay", 20))
        Titulo.pack(side=tk.TOP, pady=10)  # Espaciado mayor

        Regresar = tk.Button(frame, text="Volver al menu", command=Menu_Habitante, font=("Myanmar Sans Pro", 10), bg="red", fg="white")
        Regresar.pack(side=tk.TOP, pady=10)

        if not Horario:
            Texto = tk.Label(ventana, text = "No hay horarios disponibles de momento", font = ("Myanmar Sans Pro",10))
            Texto.pack(side = tk.TOP,pady = 10)
        else:
            for Ruta in Horario:
                Empleado = tk.Label(ventana, text = (Ruta['Empleado']))
                Empleado.pack(side = tk.TOP, pady = 10)
                Ubicacion = tk.Label(ventana, text = (Ruta['Ubicacion']))
                Ubicacion.pack(side = tk.TOP, pady = 10)
                Dir1 = tk.Label(ventana, text = (Ruta['Direccion1']))
                Dir1.pack(side = tk.TOP, pady = 10)
                Dir2 = tk.Label(ventana, text = (Ruta['Direccion2']))
                Dir2.pack(side = tk.TOP, pady = 10)
                Dir3 = tk.Label(ventana, text = (Ruta['Direccion3']))
                Dir3.pack(side = tk.TOP, pady = 10)
    
    #A partir de aquí comienza la sección de empleados
    #Como se puede ver, el empleado solo tendrá una función ya que solo tiene que ver el horario asignado
    def Menu_Empleado():
        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=700, height=500)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Titulo = tk.Label(frame, text="Bienvenido Empleado", font=("Myanmar Khyay", 15))
        Titulo.pack(side=tk.TOP, pady=10)

        Cerrar = tk.Button(frame, text="Cerrar Sesión", command=Cerrar_Sesion, bg="red", fg="white")
        Cerrar.pack(pady=10)

        if not Horario:
            Texto = tk.Label(ventana, text = "No tiene un horario asignado de momento")
            Texto.pack(side = tk.TOP, pady = 10)
        else:
            for Ruta in Horario:
                if Ruta['Empleado'] == nomos:
                    Emp = tk.Label(ventana, text = (Ruta['Empleado']))
                    Emp.pack(side = tk.TOP, pady = 10)
                    Ubicacion = tk.Label(ventana, text = (Ruta['Ubicacion']))
                    Ubicacion.pack(side = tk.TOP, pady = 10)
                    Dir1 = tk.Label(ventana, text = (Ruta['Direccion1']))
                    Dir1.pack(side = tk.TOP, pady = 10)
                    Dir2= tk.Label(ventana, text = (Ruta['Direccion2']))
                    Dir2.pack(side = tk.TOP, pady = 10)
                    Dir3 = tk.Label(ventana, text = (Ruta['Direccion3']))
                    Dir3.pack(side = tk.TOP, pady = 10)

    #El apartado del Administrador, de los más dificiles y importantes del programa
    #Aquí depende gran parte del programa que son los horarios
    def Menu_Admin():

        # Destruir todos los widgets existentes en la ventana
        for widget in ventana.winfo_children():
            widget.destroy()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=700, height=500)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Texto = tk.Label(frame, text="Bienvenido Administrador", font=("Myanmar Khyay", 15))
        Texto.pack(side=tk.TOP, pady=10)

        Horario = tk.Button(frame, text="Horarios", command=Ingresar_Horarios, font=("Myanmar Sans Pro", 10), bg="green", fg="white")
        Horario.pack(side=tk.TOP, pady=10)

        Actualizar = tk.Button(frame, text="Actualizar ubicación", command=Actualizar_Ubicacion, font=("Myanmar Sans Pro", 10), bg="green", fg="white")
        Actualizar.pack(side=tk.TOP, pady=10)

        Queja = tk.Button(frame, text="Quejas y sugerencias", command=Quejas, font=("Myanmar Sans Pro", 10), bg="green", fg="white")
        Queja.pack(side=tk.TOP, pady=10)

        Cerrar = tk.Button(frame, text="Cerrar Sesión", command=Cerrar_Sesion, bg="red", fg="white")
        Cerrar.pack(side=tk.TOP, pady=10)

    
    def Ingresar_Horarios():

        for widget in ventana.winfo_children():
            widget.destroy()
        
        def Asignar_Horarios():
            logica_programa["Horarios"](Num, Partida, Calle2, Calle3, Calle4, Horario)
            messagebox.showinfo("Digital Bell","Horario ingresado exitosamente")
            Menu_Admin()

        # Configurar la ventana para centrar el frame
        ventana.grid_rowconfigure(0, weight=1)  # Espacio dinámico arriba y abajo
        ventana.grid_rowconfigure(3, weight=1)
        ventana.grid_columnconfigure(0, weight=1)  # Espacio dinámico izquierda y derecha

        # Crear un frame dentro de la ventana
        frame = tk.Frame(ventana, bg="white", bd=3, relief="solid", width=700, height=500)  # Tamaño aún más grande
        frame.grid(row=1, column=1, padx=50, pady=50)  # Márgenes exteriores mayores
        frame.grid_propagate(False)  # Evita que el tamaño del frame se ajuste al contenido

        # Agregar widgets al frame
        Texto = tk.Label(frame, text="Horarios y rutas", font=("Myanmar Khyay", 15))
        Texto.pack(side=tk.TOP, pady=5)

        Texto1 = tk.Label(frame, text="Número de Empleado a asignar")
        Texto1.pack(side=tk.TOP, pady=5)
        Num = tk.Entry(frame)
        Num.pack(side=tk.TOP, pady=5)

        Texto5 = tk.Label(frame, text="¿Por donde va a empezar el recorrido?")
        Texto5.pack(side=tk.TOP, pady=5)
        Partida = tk.Entry(frame)
        Partida.pack(side=tk.TOP, pady=5)

        Texto2 = tk.Label(frame, text="Ingrese la segunda dirección")
        Texto2.pack(side=tk.TOP, pady=5)
        Calle2 = tk.Entry(frame)
        Calle2.pack(side=tk.TOP, pady=5)

        Texto3 = tk.Label(frame, text="Ingrese la tercera dirección")
        Texto3.pack(side=tk.TOP, pady=5)
        Calle3 = tk.Entry(frame)
        Calle3.pack(side=tk.TOP, pady=5)

        Texto4 = tk.Label(frame, text="Ingrese la cuarta dirección")
        Texto4.pack(side=tk.TOP, pady=5)
        Calle4 = tk.Entry(frame)
        Calle4.pack(side=tk.TOP, pady=5)

        Asignar = tk.Button(frame, text="Asignar horarios", command=Asignar_Horarios, bg="green", fg="white")
        Asignar.pack(side=tk.TOP, pady=10)

        Regresar = tk.Button(frame, text="Regresar", command=Menu_Admin, bg="red", fg="white")
        Regresar.pack(side=tk.TOP, pady=10)

    
    def Actualizar_Ubicacion():
        
        for widget in ventana.winfo_children():
            widget.destroy()

        def Actualizar():
            logica_programa["Ac_Ubicacion"](Num,Ubicacion,Horario)
            messagebox.showinfo("Digital Bell", "Ubicación actualizada exitosamente")
            Menu_Admin()  # Regresar al menú del administrador

        Texto = tk.Label(ventana, text = "Ingrese el número de empleado")
        Texto.pack(side = tk.TOP, pady = 10)
        Num = tk.Entry(ventana)
        Num.pack(side = tk.TOP, pady = 10)
        Texto1 = tk.Label(ventana, text = "Ingrese su ubicación actual")
        Texto1.pack(side = tk.TOP, pady = 10)
        Ubicacion = tk.Entry(ventana)
        Ubicacion.pack(side = tk.TOP, pady = 10)
        Cambia = tk.Button(ventana, text = "Actualizar ubicación", command = Actualizar,bg="green",fg="white")
        Cambia.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Regresar", command = Menu_Admin,bg="red",fg="white")
        Regresar.pack(side = tk.TOP, pady = 10)
    
    #Este es diferente al de Queja_Habitante ya que este en lugar de registrarlas las muestra unicamente al Administrador
    def Quejas():
        global Queja

        for widget in ventana.winfo_children():
            widget.destroy()
    
        Titulo = tk.Label(ventana, text = "Quejas y sugerencias")
        Titulo.pack(side = tk.TOP)
        Regresar = tk.Button(ventana, text = "Volver al menu", command = Menu_Admin,bg="red",fg="white")
        Regresar.pack(side = tk.TOP, pady = 10)
        if not Queja:
            Texto = tk.Label(ventana, text = "No hay quejas de momento", font = ("Myanmar Sans Pro",10),bg="black",fg="white")
            Texto.pack(side = tk.TOP,pady = 10)
        else:
            for quejas in Queja:
                Usuario = tk.Label(ventana, text = quejas['Usuario'])
                Usuario.pack(side = tk.TOP, pady = 10)
                Sugerencia = tk.Label(ventana, text = quejas['Queja'])
                Sugerencia.pack(side = tk.TOP, pady = 10)


    #Esta función es exclusivamente para cerrar sesión y volver al menu principal
    def Cerrar_Sesion():
        global nomos
        Cerrar_Sesion = messagebox.askyesno("Digital Bell", "¿Desea cerrar sesión?")
        if Cerrar_Sesion:
            nomos = ""
            Menu()
        else:
            messagebox.showinfo("Digital Bell", "No se pudo cerrar sesión")
    
    frame = tk.Frame(ventana)
    frame.pack(pady=10, padx=10)  # Espaciado alrededor del frame

# Agregar widgets al frame
    frame = tk.Frame((ventana), bd=3, relief="solid")
    frame.pack(pady=10, padx=10, expand=True)  # Espaciado alrededor del frame

    # Agregar widgets al frame
    Texto = tk.Label(frame, text="Bienvenid@ a Digital Bell", font=("Myanmar Khyay", 20))
    Texto.pack(side=tk.TOP, pady=10)

    Registra = tk.Button(frame, text="Crear cuenta", command=Registro, font=("Myanmar Sans Pro", 15),bg="green",fg="white")
    Registra.pack(side=tk.TOP, pady=(180,10), padx=10)

    Sesion = tk.Button(frame, text="Iniciar Sesión", command=Iniciar_Sesion, font=("Myanmar Sans Pro", 15),bg="green",fg="white")
    Sesion.pack(side=tk.TOP, pady=10, padx=10)

    Salir = tk.Button(frame, text="Salir", command=ventana.quit, font=("Myanmar Sans Pro", 15),bg="red",fg="white")
    Salir.pack(pady=5)
    ventana.mainloop()