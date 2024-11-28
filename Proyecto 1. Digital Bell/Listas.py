import tkinter as tk
from tkinter import messagebox,ttk
ventana = tk.Tk()
ventana.title("Creador de baraja Yu-Gi-Oh!")
ventana.geometry("500x600")
Deck= []

def Mostrar_Menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    
    Saludo = tk.Label(ventana, text="Bienvenido a tu deck")
    Saludo.grid(row = 0, column = 0, pady = 10)
    Texto1 = tk.Label(ventana, text = "¿Qué le gustaria realizar?")
    Texto1.grid(row = 1, column = 0, pady = 10)
    Registro = tk.Button(ventana, text = "Registrar carta nueva", command = lambda: Registra1(ventana,Registrar_Carta))
    Registro.grid(row = 2, column = 0, pady = 10)
    Busqueda = tk.Button(ventana, text = "Buscar una carta", command = lambda: Consulta(ventana, Buscar_Carta))
    Busqueda.grid(row = 3, column = 0, pady = 10)
    Borrar = tk.Button(ventana, text = "Eliminar una carta", command = lambda: Borra(ventana, Eliminar_Carta))
    Borrar.grid(row = 4, column = 0, pady = 10)
    Cambio = tk.Button(ventana, text = "Modificar carta", command = lambda: Cambiar(ventana, Modificar_Carta))
    Cambio.grid(row = 5, column = 0, pady = 10)
    Baraja = tk.Button(ventana, text = "Estado de la baraja", command = Mostrar_Deck)
    Baraja.grid(row = 6, column = 0, pady = 10)
    Salida = tk.Button(ventana, text="Cerrar", command=ventana.quit)
    Salida.grid(row = 7, column = 0, pady = 10)
    
def Registra1(ventana,callback):
    Registra1 = tk.Toplevel(ventana)
    Registra1.title("Registrar Carta")
    Texto2 = tk.Label(Registra1, text="Elija el tipo de carta a ingresar")
    Texto2.pack(pady=5)

    Variable = tk.StringVar(Registra1)
    Variable.set("Carta")
    Op = ["Monstruo","Trampa","Magia"]
    Menu = tk.OptionMenu(Registra1, Variable, *Op)
    Menu.pack(pady = 10)

    def Seleccion():
        tipo = Variable.get()
        if tipo:
            callback(tipo) 
            Registra1.destroy()
    
    EnviarO = tk.Button(Registra1, text = "Enviar", command = Seleccion)
    EnviarO.pack(pady=10)

def Consulta(ventana,callback):
    if not Deck:
        messagebox.showwarning("Busqueda","No hay cartas en el Deck")
    else:
        Registra1 = tk.Toplevel(ventana)
        Registra1.title("Consultar Carta")
        Texto2 = tk.Label(Registra1, text="Elija el tipo de carta")
        Texto2.pack(pady=5)

        Variable = tk.StringVar(Registra1)
        Variable.set("Carta")
        Op = ["Monstruo","Trampa","Magia"]
        Menu = tk.OptionMenu(Registra1, Variable, *Op)
        Menu.pack(pady = 10)

        def Seleccion():
            tipo = Variable.get()
            if tipo:
                callback(tipo) 
                Registra1.destroy()
    
        EnviarO = tk.Button(Registra1, text = "Enviar", command = Seleccion)
        EnviarO.pack(pady=10)

def Borra(ventana,callback):
    if not Deck:
        messagebox.showwarning("Borrado","No hay cartas en el Deck")
    else:
        Registra1 = tk.Toplevel(ventana)
        Registra1.title("Borrar Carta")
        Texto2 = tk.Label(Registra1, text = "Elija el tipo de carta a borrar")
        Texto2.pack(pady = 5)

        Variable = tk.StringVar(Registra1)
        Variable.set("Carta")
        Op = ["Monstruo","Trampa","Magia"]
        Menu = tk.OptionMenu(Registra1, Variable, *Op)
        Menu.pack(pady = 10)

        def Seleccion():
            tipo = Variable.get()
            if tipo:
                callback(tipo) 
                Registra1.destroy()
    
        EnviarO = tk.Button(Registra1, text = "Enviar", command = Seleccion)
        EnviarO.pack(pady=10)

def Cambiar(ventana,callback):
    if not Deck:
        messagebox.showwarning("Cambiar","No hay cartas en el Deck")
    else:
        Registra = tk.Toplevel(ventana)
        Registra.title("Cambiar")
        Texto2 = tk.Label(Registra, text = "Elija el tipo de carta a modificar")
        Texto2.pack(pady = 5)

        Variable = tk.StringVar(Registra)
        Variable.set("Carta")
        Op = ["Monstruo","Trampa","Magia"]
        Menu = tk.OptionMenu(Registra, Variable, *Op)
        Menu.pack(pady = 10)

        Texto1 = tk.Label(Registra, text = "Ingrese el nombre de la carta")
        Texto1.pack(pady = 5)
        Entrada = tk.Entry(Registra)
        Entrada.pack(pady = 5)

        def Seleccion():
            tipo = Variable.get()
            nombre = Entrada.get()
            if tipo and nombre:
                callback(tipo,nombre)
                Registra.destroy()
    
        EnviarO = tk.Button(Registra, text = "Enviar", command = Seleccion)
        EnviarO.pack(pady=10)

def Registrar_Carta(tipo):
    global Deck
    for widget in ventana.winfo_children():
        widget.destroy()
    
    def agregar_carta():
        global Deck
        if tipo == "Monstruo":
            nombre = Nombre.get()
            atributo = Atributo.get()
            tipo_monstruo = Tipo.get()
            atke = ATK.get()
            defn = DEF.get()
            estado = Estado.get()
            nivel = Estrella.get()
            efecto = Efecto.get()
            
            Monstruo = {
                "name": nombre,
                "attribute": atributo,
                "type": tipo_monstruo,
                "ATK": atke,
                "DEF": defn,
                "status": estado,
                "level": nivel,
                "effect": efecto
            }
            Deck.append(Monstruo)
            messagebox.showinfo("Información", "Carta Agregada")
            Registrar_Carta(tipo)
        
        elif tipo == "Trampa":
            nombre = Nombre.get()
            tipo_trampa = Tip.get()
            efecto = Efecto.get()

            Trampa = {
                "name": nombre,
                "type": tipo_trampa,
                "effect": efecto
            }
            Deck.append(Trampa)
            messagebox.showinfo("Información", "Carta agregada")
            Registrar_Carta(tipo)
        
        elif tipo == "Magia":
            nombre = Nombre.get()
            tipo_magia = Tip.get()
            efecto = Efecto.get()

            Magia = {
                "name": nombre,
                "type": tipo_magia,
                "effect": efecto
            }
            Deck.append(Magia)
            messagebox.showinfo("Información", "Carta agregada")
            Registrar_Carta(tipo)
        
        else:
            messagebox.showerror("Error", "Opción no válida")

    if tipo == "Monstruo":

        Nom = tk.Label (ventana, text = "Ingrese el nombre del monstruo")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        At = tk.Label(ventana,text = "Ingrese el atributo del monstruo")
        At.pack(side = tk.TOP)
        Atributo = tk.Entry(ventana,width = 40)
        Atributo.pack(pady = 10)

        ti = tk.Label(ventana, text = "Ingrese el tipo del monstruo")
        ti.pack(side = tk.TOP)
        Tipo = tk.Entry(ventana, width = 40)
        Tipo.pack(pady = 10)
        
        Ataque = tk.Label(ventana, text = "Ingrese el ataque del monstruo")
        Ataque.pack(side = tk.TOP)
        ATK = tk.Entry(ventana, width = 40)
        ATK.pack(pady = 10)

        Defensa = tk.Label(ventana, text = "Ingrese la defensa del monstruo")
        Defensa.pack(side = tk.TOP)
        DEF = tk.Entry(ventana, width = 40)
        DEF.pack(pady = 10)

        Estado = tk.StringVar(ventana)
        Estado.set("Normal")
        Texto = tk.Label(ventana, text = "Elija el tipo de carta")
        Texto.pack(side = tk.TOP)
        Mons = ["Normal","Efecto","Fusión","Sincronía","Xyz","Péndulo","Enlace"]
        status = tk.OptionMenu(ventana, Estado, *Mons)
        status.pack(pady = 10)

        Nivel = tk.Label(ventana, text = "Ingrese el número de estrellas del monstruo")
        Nivel.pack(side = tk.TOP)
        Estrella = tk.Entry(ventana, width = 40)
        Estrella.pack(pady = 10)

        Ef = tk.Label(ventana, text = "Ingrese el efecto del monstruo")
        Ef.pack(side = tk.TOP)
        Efecto = tk.Entry(ventana, width = 50)
        Efecto.pack(pady = 10)

        boton_agregar = tk.Button(ventana, text="Agregar Carta", command=agregar_carta)
        boton_agregar.pack(pady=10)
        MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        MenuP.pack(pady = 10)

    elif tipo == "Trampa":
        Nom = tk.Label(ventana, text = "Ingrese el nombre de la carta")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        Texto = tk.Label(ventana, text = "Elija el tipo de carta")
        Texto.pack(side = tk.TOP)
        Tip = tk.StringVar(ventana)
        Tip.set("Normal")
        Tram = ["Normal","ContraEfecto","Continua"]
        Tipo = tk.OptionMenu(ventana, Tip, *Tram)
        Tipo.pack(pady = 10)

        Ef = tk.Label(ventana, text = "Ingrese el efecto de la carta")
        Ef.pack(side = tk.TOP)
        Efecto = tk.Entry(ventana, width = 40)
        Efecto.pack(pady = 10)
        
        boton_agregar = tk.Button(ventana, text="Agregar Carta", command=agregar_carta)
        boton_agregar.pack(pady=10)
        MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        MenuP.pack(pady = 10)

    elif tipo == "Magia":
        Nom = tk.Label(ventana, text = "Ingrese el nombre de la carta")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        Texto = tk.Label(ventana, text = "Elija el tipo de carta")
        Texto.pack(side = tk.TOP)
        Tip = tk.StringVar(ventana)
        Tip.set("Normal")
        Mag = ["Normal","Continua","Juego Rapido","Equipo","Campo","Ritual"]
        Tipo = tk.OptionMenu(ventana, Tip, *Mag)
        Tipo.pack(pady = 10)
        Ef = tk.Label(ventana, text = "Ingrese el efecto de la carta")
        Ef.pack(side = tk.TOP)
        Efecto = tk.Entry(ventana, width = 40)
        Efecto.pack(pady = 10)

        boton_agregar = tk.Button(ventana, text="Agregar Carta", command=agregar_carta)
        boton_agregar.pack(pady=10)
        MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        MenuP.pack(pady = 10)

def Buscar_Carta(tipo):
    global Deck
    for widget in ventana.winfo_children():
        widget.destroy()
    
    def mostrar_datos():
            global Deck
            if tipo == "Monstruo":
                for Monstruo in Deck:
                    if Monstruo['name'] == Nombre.get():
                        Name = tk.Label(ventana, text = Monstruo['name'])
                        Name.pack(pady = 5)
                        Tipo = tk.Label(ventana, text = Monstruo['type'])
                        Tipo.pack(pady = 5)
                        Atk = tk.Label(ventana, text = Monstruo['ATK'])
                        Atk.pack(pady = 5)
                        Def = tk.Label(ventana, text = Monstruo['DEF'])
                        Def.pack(pady = 5)
                        Est = tk.Label(ventana, text = Monstruo['status'])
                        Est.pack(pady = 5)
                        N = tk.Label(ventana, text = Monstruo['level'])
                        N.pack(pady = 5)

                        effect_frame = tk.Frame(ventana)
                        effect_frame.pack(pady=5)
                        Ef = tk.Text(effect_frame, height=5, width=50)
                        Ef.insert(tk.END, Monstruo['effect'])
                        Ef.config(state=tk.DISABLED)
                        Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                        scrollbar = tk.Scrollbar(effect_frame, command = Ef.yview)
                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                        Ef.config(yscrollcommand=scrollbar.set)

            elif tipo == "Trampa":
                for Trampa in Deck:
                    if Trampa['name'] == Nombre.get():
                        Name = tk.Label(ventana, text = Trampa['name'])
                        Name.pack(pady = 5)
                        Tipo = tk.Label(ventana, text = Trampa['type'])
                        Tipo.pack(pady = 5)

                        effect_frame = tk.Frame(ventana)
                        effect_frame.pack(pady=5)
                        Ef = tk.Text(effect_frame, height=5, width=50)
                        Ef.insert(tk.END, Trampa['effect'])
                        Ef.config(state=tk.DISABLED)
                        Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                        scrollbar = tk.Scrollbar(effect_frame, command = Ef.yview)
                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                        Ef.config(yscrollcommand=scrollbar.set)
            
            elif tipo == "Magia":
                for Magia in Deck:
                    if Magia['name'] == Nombre.get():
                        Name = tk.Label(ventana, text = Magia['name'])
                        Name.pack(pady = 5)
                        Tipo = tk.Label(ventana, text = Magia['type'])
                        Tipo.pack(pady = 5)

                        effect_frame = tk.Frame(ventana)
                        effect_frame.pack(pady=5)
                        Ef = tk.Text(effect_frame, height=5, width=50)
                        Ef.insert(tk.END, Magia['effect'])
                        Ef.config(state=tk.DISABLED)
                        Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                        scrollbar = tk.Scrollbar(effect_frame, command = Ef.yview)
                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                        Ef.config(yscrollcommand=scrollbar.set)

    if tipo == "Monstruo":
        Nom = tk.Label (ventana, text = "Ingrese el nombre del monstruo")
        Nom.pack(pady = 10)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        Buscar = tk.Button(ventana, text="Buscar Carta", command=mostrar_datos)
        Buscar.pack(pady=10)
        Otra = tk.Button(ventana, text="Buscar otra carta", command=Consulta)
        MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        MenuP.pack(pady = 10)

    elif tipo == "Trampa":
        Nom = tk.Label (ventana, text = "Ingrese el nombre de la carta")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        Buscar = tk.Button(ventana, text="Buscar Carta", command=mostrar_datos)
        Buscar.pack(pady=10)

        MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        MenuP.pack(pady = 10)

    elif tipo == "Magia":
        Nom = tk.Label (ventana, text = "Ingrese el nombre de la carta")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        Buscar = tk.Button(ventana, text="Buscar Carta", command=mostrar_datos)
        Buscar.pack(pady = 10)
        
        Menup = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
        Menup.pack(pady = 10)

def Eliminar_Carta(tipo):
    global Deck
    for widget in ventana.winfo_children():
        widget.destroy()

    global carta_a_eliminar
    carta_a_eliminar = None
        
    def eliminar():
            global carta_a_eliminar
            if carta_a_eliminar:
                Deck.remove(carta_a_eliminar)
                messagebox.showinfo("Eliminado", "La carta ha sido eliminada con éxito")
                carta_a_eliminar = None

    if tipo == "Monstruo":
        Nom = tk.Label (ventana, text = "Ingrese el nombre del monstruo")
        Nom.pack(side = tk.TOP)
        Nombre = tk.Entry(ventana, width = 40)
        Nombre.pack(pady = 10)

        def mostrar_datos():
            global carta_a_eliminar
            nombre_carta = Nombre.get()
            for Monstruo in Deck:
                if Monstruo['name'] == nombre_carta:

                    carta_a_eliminar = Monstruo

                    Name = tk.Label(ventana, text = Monstruo['name'])
                    Name.pack(pady = 5)
                    Tipo = tk.Label(ventana, text = Monstruo['type'])
                    Tipo.pack(pady = 5)
                    Atk = tk.Label(ventana, text = Monstruo['ATK'])
                    Atk.pack(pady = 5)
                    Def = tk.Label(ventana, text = Monstruo['DEF'])
                    Def.pack(pady = 5)
                    Est = tk.Label(ventana, text = Monstruo['status'])
                    Est.pack(pady = 5)
                    N = tk.Label(ventana, text = Monstruo['level'])
                    N.pack(pady = 5)
                    Ef = tk.Label(ventana, text = Monstruo['effect'])
                    Ef.pack(pady = 5)
                    Texto = tk.Label(ventana, text = "¿Es esta la carta a eliminar?")
                    Texto.pack(pady = 5)
                    
                    Elim = tk.Button(ventana, text="Eliminar", command = eliminar)
                    Elim.pack(pady = 5)

        
        Buscar = tk.Button(ventana, text="Buscar Carta", command = mostrar_datos)
        Buscar.pack(pady=10)
        Otra = tk.Button(ventana, text="Buscar Otra", command=Borra)
        Otra.pack(pady=5)


    elif tipo == "Trampa":
        Nom = tk.Label(ventana, text="Ingrese el nombre de la carta")
        Nom.pack(side=tk.TOP)
        Nombre = tk.Entry(ventana, width=40)
        Nombre.pack(pady=10)

        def mostrar_datos():
            global carta_a_eliminar
            nombre_carta = Nombre.get()
            for Trampa in Deck:
                if Trampa['name'] == nombre_carta:

                    carta_a_eliminar = Trampa
                    Name = tk.Label(ventana, text=Trampa['name'])
                    Name.pack(pady=5)
                    Tipo = tk.Label(ventana, text=Trampa['type'])
                    Tipo.pack(pady=5)
                    Ef = tk.Label(ventana, text=Trampa['effect'])
                    Ef.pack(pady=5)
                    Texto = tk.Label(ventana, text="¿Es esta la carta a eliminar?")
                    Texto.pack(pady=5)

                    Elim = tk.Button(ventana, text="Eliminar", command=eliminar)
                    Elim.pack(pady=5)
                    Otra = tk.Button(ventana, text="Buscar Otra", command=Borra)
                    Otra.pack(pady=5)
            
        Buscar = tk.Button(ventana, text="Buscar Carta", command=mostrar_datos)
        Buscar.pack(pady=10)


    elif tipo == "Magia":
        Nom = tk.Label(ventana, text="Ingrese el nombre de la carta")
        Nom.pack(side=tk.TOP, pady = 5)
        Nombre = tk.Entry(ventana, width=40)
        Nombre.pack(pady=10)

        def mostrar_datos():
            global carta_a_eliminar
            nombre_carta = Nombre.get()
            for Magia in Deck:
                if Magia['name'] == nombre_carta:
                    carta_a_eliminar = Magia
                    Name = tk.Label(ventana, text=Magia['name'])
                    Name.pack(pady=5)
                    Tipo = tk.Label(ventana, text=Magia['type'])
                    Tipo.pack(pady=5)
                    Ef = tk.Label(ventana, text=Magia['effect'])
                    Ef.pack(pady=5)
                    Texto = tk.Label(ventana, text="¿Es esta la carta a eliminar?")
                    Texto.pack(pady=5)

                    Elim = tk.Button(ventana, text="Eliminar", command=eliminar)
                    Elim.pack(pady=5)
                    Otra = tk.Button(ventana, text="Buscar Otra", command=Borra)
                    Otra.pack(pady=5)
        
        Buscar = tk.Button(ventana, text="Buscar Carta", command=mostrar_datos)
        Buscar.pack(pady=10)
    
    MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
    MenuP.pack(pady = 10)
    
def Modificar_Carta(tipo,nombre):
    global Deck
    for widget in ventana.winfo_children():
        widget.destroy()
    
    def Cambiar_carta():
        global Deck
        if tipo == "Monstruo":
            for Monstruo in Deck:
                if Monstruo['name'] == nombre:

                    Monstruo['attribute'] = Atr.get()
                    Monstruo['type'] = Tip.get()
                    Monstruo['ATK'] = At.get()
                    Monstruo['DEF'] = Df.get()
                    Monstruo['status'] = Es.get()
                    Monstruo['level'] = Nv.get()
                    Monstruo['effect'] = Ef.get("1.0", tk.END).strip()

                    messagebox.showinfo("Información", "Carta Agregada")
                    return
        
        elif tipo == "Trampa":
            for Trampa in Deck:
                if Trampa['name'] == nombre:

                    Trampa['type'] = Tip.get()
                    Trampa['effect'] = Ef.get("1.0", tk.END).strip()
            
                    messagebox.showinfo("Información", "Carta agregada")
        
        elif tipo == "Magia":
            for Magia in Deck:
                if Magia['name'] == nombre:

                    Magia['type'] = Tip.get()
                    Magia['effect'] = Ef.get("1.0", tk.END).strip()
            
                    messagebox.showinfo("Información", "Carta agregada")
        
        else:
            Registro.config(text="Opción no válida")

    if not Deck:
        Texto = tk.Label(ventana, text="No hay cartas registradas aun")
        Texto.pack(pady = 5)

    else:
        if tipo == "Monstruo":
            for Monstruo in Deck:
                if Monstruo['name'] == nombre:
                    Texto1 = tk.Label(ventana, text = "Nombre del monstruo")
                    Texto1.pack(pady = 5)
                    Nm = tk.Label(ventana, text = Monstruo['name'])
                    Nm.pack(pady = 5)

                    Texto7 = tk.Label(ventana, text = "Atributo del monstruo")
                    Texto7.pack(pady = 5)
                    Atr = tk.Entry(ventana)
                    Atr.insert(0, Monstruo['attribute'])
                    Atr.pack(pady = 5)

                    Texto2 = tk.Label(ventana, text = "Tipo de monstruo")
                    Texto2.pack(pady = 5)
                    Tip = tk.Entry(ventana)
                    Tip.insert(0, Monstruo['type'])
                    Tip.pack(pady = 5)

                    Texto = tk.Label(ventana, text = "Estado del monstruo")
                    Texto.pack(pady = 5)
                    Es = tk.StringVar(ventana)
                    Es.set(Monstruo['status'])
                    Mons = ["Normal","Efecto","Fusión","Sincronía","Xyz","Péndulo","Enlace"]
                    status = tk.OptionMenu(ventana, Es, *Mons)
                    status.pack(pady = 10)
                    
                    Texto4 = tk.Label(ventana, text = "Ataque")
                    Texto4.pack(pady = 5)
                    At = tk.Entry(ventana)
                    At.insert(0, Monstruo['ATK'])
                    At.pack(pady = 5)
                    
                    Texto5 = tk.Label(ventana, text = "Defensa")
                    Texto5.pack(pady = 5)
                    Df = tk.Entry(ventana)
                    Df.insert(0, Monstruo['DEF'])
                    Df.pack(pady = 5)

                    Texto6 = tk.Label(ventana, text = "Nivel")
                    Texto6.pack(pady = 5)
                    Nv = tk.Entry(ventana)
                    Nv.insert(0, Monstruo['level'])
                    Nv.pack(pady = 5)

                    Texto3 = tk.Label(ventana, text = "Efecto")
                    Texto3.pack(pady = 5)
                    effect_frame = tk.Frame(ventana)
                    effect_frame.pack(pady=5)
                    Ef = tk.Text(effect_frame, height=5, width=60)
                    Ef.insert(tk.END, Monstruo['effect'])
                    Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                    Cambio = tk.Button(ventana, text = "Cambiar", command = Cambiar_carta)
                    Cambio.pack(pady = 5)

        elif tipo == "Trampa":
            for Trampa in Deck:
                if Trampa['name'] == nombre:
                    Texto1 = tk.Label(ventana, text = "Nombre de la trampa")
                    Texto1.pack(pady = 5)
                    Nm = tk.Label(ventana, text = Trampa['name'])
                    Nm.pack(pady = 5)

                    Texto = tk.Label(ventana, text = "Tipo de carta")
                    Texto.pack(pady = 5)
                    Tip = tk.StringVar(ventana)
                    Tip.set(Trampa['type'])
                    Mons = ["Normal","Contraefecto","Continua"]
                    status = tk.OptionMenu(ventana, Tip, *Mons)
                    status.pack(pady = 10)
                    
                    Texto3 = tk.Label(ventana, text = "Efecto")
                    Texto3.pack(pady = 5)
                    effect_frame = tk.Frame(ventana)
                    effect_frame.pack(pady=5)
                    Ef = tk.Text(effect_frame, height=5, width=60)
                    Ef.insert(tk.END, Trampa['effect'])
                    Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                    Cambio = tk.Button(ventana, text = "Cambiar", command = Cambiar_carta)
                    Cambio.pack(pady = 5)

        elif tipo == "Magia":
            for Magia in Deck:
                if Magia['name'] == nombre:
                    Texto1 = tk.Label(ventana, text = "Nombre de la carta")
                    Texto1.pack(pady = 5)
                    Nm = tk.Label(ventana, text = Magia['name'])
                    Nm.pack(pady = 5)

                    Texto = tk.Label(ventana, text = "Tipo de carta")
                    Texto.pack(pady = 5)
                    Tip = tk.StringVar(ventana)
                    Tip.set(Magia['type'])
                    Mons = ["Normal","Continua","Juego Rapido","Equipo","Campo","Ritual"]
                    status = tk.OptionMenu(ventana, Tip, *Mons)
                    status.pack(pady = 10)

                    Texto3 = tk.Label(ventana, text = "Efecto")
                    Texto3.pack(pady = 5)
                    effect_frame = tk.Frame(ventana)
                    effect_frame.pack(pady=5)
                    Ef = tk.Text(effect_frame, height=5, width=50)
                    Ef.insert(tk.END, Magia['effect'])
                    Ef.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                    Cambio = tk.Button(ventana, text = "Cambiar", command = Cambiar_carta)
                    Cambio.pack(pady = 5)
    
    MenuP = tk.Button(ventana, text="Volver al menu", command=Mostrar_Menu)
    MenuP.pack(pady = 10)

def Mostrar_Deck():
    Muestra = tk.Toplevel(ventana)
    Muestra.title("Deck")

    main_frame = tk.Frame(Muestra)
    main_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not Deck:
        Texto = tk.Label(scrollable_frame, text="No hay cartas en el deck")
        Texto.pack(pady=5)
        return

    Texto1 = tk.Label(scrollable_frame, text="Cartas de Monstruo:", font=("Helvetica", 14, "bold"))
    Texto1.pack(pady=5)

    hay_monstruos = False
    for carta in Deck:
        if 'attribute' in carta:
            monster_frame = tk.Frame(scrollable_frame, bd=2, relief=tk.SUNKEN)
            monster_frame.pack(pady=5, padx=10, fill=tk.X)

            texto_monstruo = f"Nombre: {carta['name']}, Tipo: {carta['type']}, ATK: {carta['ATK']}, DEF: {carta['DEF']}, Estado: {carta['status']}, Nivel: {carta['level']}"
            Label = tk.Label(monster_frame, text=texto_monstruo, wraplength=600)
            Label.pack(side=tk.TOP, fill=tk.X)

            effect_text = tk.Text(monster_frame, height=3, width=70)
            effect_text.insert(tk.END, carta['effect'])
            effect_text.config(state=tk.DISABLED)
            effect_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            effect_scrollbar = tk.Scrollbar(monster_frame, command=effect_text.yview)
            effect_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            effect_text.config(yscrollcommand=effect_scrollbar.set)

            hay_monstruos = True

    if not hay_monstruos:
        TextoNoMonstruos = tk.Label(scrollable_frame, text="No hay monstruos en el deck")
        TextoNoMonstruos.pack(pady=5)

    Texto2 = tk.Label(scrollable_frame, text="Cartas de Trampa:", font=("Helvetica", 14, "bold"))
    Texto2.pack(pady=10)

    hay_trampas = False
    for Trampa in Deck:
        if 'type' in Trampa and Trampa['type'] in ["Normal", "ContraEfecto", "Continua"]:
            trap_frame = tk.Frame(scrollable_frame, bd=2, relief=tk.SUNKEN)
            trap_frame.pack(pady=5, padx=10, fill=tk.X)

            texto_trampa = f"Nombre: {Trampa['name']}, Tipo: {Trampa['type']}"
            Label = tk.Label(trap_frame, text=texto_trampa, wraplength=600)
            Label.pack(side=tk.TOP, fill=tk.X)

            effect_text = tk.Text(trap_frame, height=3, width=70)
            effect_text.insert(tk.END, Trampa['effect'])
            effect_text.config(state=tk.DISABLED)
            effect_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            effect_scrollbar = tk.Scrollbar(trap_frame, command=effect_text.yview)
            effect_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            effect_text.config(yscrollcommand=effect_scrollbar.set)

            hay_trampas = True

    if not hay_trampas:
        TextoNoTrampas = tk.Label(scrollable_frame , text="No hay cartas de trampa en el deck")
        TextoNoTrampas.pack(pady=5)

    Texto3 = tk.Label(scrollable_frame, text="Cartas de Magia:", font=("Helvetica", 14, "bold"))
    Texto3.pack(pady=10)

    hay_magias = False
    for Magia in Deck:
        if 'type' in Magia and Magia['type'] in ["Normal", "Continua", "Ritual", "Campo"]:
            magic_frame = tk.Frame(scrollable_frame, bd=2, relief=tk.SUNKEN)
            magic_frame.pack(pady=5, padx=10, fill=tk.X)

            texto_magia = f"Nombre: {Magia['name']}, Tipo: {Magia['type']}"
            Label = tk.Label(magic_frame, text=texto_magia, wraplength=600)
            Label.pack(side=tk.TOP, fill=tk.X)

            effect_text = tk.Text(magic_frame, height=3, width=70)
            effect_text.insert(tk.END, Magia['effect'])
            effect_text.config(state=tk.DISABLED)
            effect_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            effect_scrollbar = tk.Scrollbar(magic_frame, command=effect_text.yview)
            effect_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            effect_text.config(yscrollcommand=effect_scrollbar.set)

            hay_magias = True

    if not hay_magias:
        TextoNoMagias = tk.Label(scrollable_frame, text="No hay cartas de magia en el deck")
        TextoNoMagias.pack(pady=5)

    Muestra.mainloop()

Saludo = tk.Label(ventana, text="Bienvenido a tu deck")
Saludo.grid(row = 0, column = 0, pady = 10)
Texto1 = tk.Label(ventana, text = "¿Qué le gustaria realizar?")
Texto1.grid(row = 1, column = 0, pady = 10)
Registro = tk.Button(ventana, text = "Registrar carta nueva", command = lambda: Registra1(ventana, Registrar_Carta))
Registro.grid(row = 2, column = 0, pady = 10)
Busqueda = tk.Button(ventana, text = "Buscar una carta", command = lambda: Consulta(ventana, Buscar_Carta))
Busqueda.grid(row = 3, column = 0, pady = 10)
Borrar = tk.Button(ventana, text = "Eliminar una carta", command = lambda: Borra(ventana, Eliminar_Carta))
Borrar.grid(row = 4, column = 0, pady = 10)
Cambio = tk.Button(ventana, text = "Modificar carta", command = lambda: Cambiar(ventana, Modificar_Carta))
Cambio.grid(row = 5, column = 0, pady = 10)
Baraja = tk.Button(ventana, text = "Estado de la baraja", command = Mostrar_Deck)
Baraja.grid(row = 6, column = 0, pady = 10)
Salida = tk.Button(ventana, text="Cerrar", command=ventana.quit)
Salida.grid(row = 7, column = 0, pady = 10)

ventana.columnconfigure(0, weight = 1)
ventana.mainloop()