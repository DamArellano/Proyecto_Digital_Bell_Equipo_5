import tkinter as tk
from tkinter import messagebox
import Habitante2
import Empleado2
import Administrador2
ventana = tk.Tk()
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.title("Digital Bell")
ventana.geometry(f"{screen_width}x{screen_height}")
Usuario = []
Queja = []
Horario = []
nomos = ""

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

def Registro(ventana,callback):
    Registro = tk.Toplevel(ventana)
    Registro.title("Digital Bell")
    Texto = tk.Label(Registro, text = "Elija su tipo de usuario", font = ("Myanmar Sans Pro",10))
    Texto.pack(pady = 5)

    Variable = tk.StringVar(Registro)
    Variable.set("Usuario")
    Opciones = ["Habitante","Empleado"]
    Menu = tk.OptionMenu(Registro, Variable, *Opciones)
    Menu.pack(pady = 5)

    def Seleccion():
        tipo = Variable.get()
        if tipo:
            callback(tipo) 
            Registro.destroy()
    
    EnviarO = tk.Button(Registro, text = "Siguiente", command = Seleccion)
    EnviarO.pack(pady=10)

def Registrar_Usuario(tipo):
    global Usuario

    for widget in ventana.winfo_children():
        widget.destroy()

    def Agregar():
        global Usuario,nomos
        if tipo == "Usuario":
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
            messagebox.showinfo("Digital Bell", "Se ha agregado un nuevo usuario")
            nomos = Nombre
            Habitante2.Menu_Habitante()
        
        elif tipo == "Empleado":
            Nombre = Nom.get()
            Telefono = Num.get()
            Numero_Empleado = Con.get()

            Empleado = {
                "Nombre": Nombre,
                "Telefono" : Telefono,
                "Contraseña": Numero_Empleado
            }

            Usuario.append(Empleado)
            messagebox.showinfo("Digital Bell", "Se ha agregado un empleado")
            nomos = Nombre
            Empleado2.Menu_Empleado()
        
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
    global Usuario

    for widget in ventana.winfo_children():
        widget.destroy()
       
    def Verificar(Nom, Con, Tipo):
        global Usuario, nomos
        if Tipo == "Usuario":
            for Habitante in Usuario:
                if Habitante['Nombre'] == Nom.get() and Habitante['Contraseña'] == Con.get():
                    nomos = Nom.get()
                    messagebox.showinfo("Digital Bell", "Bienvenido " + Nom.get())
                    Habitante2.Menu_Habitante()
            

        elif Tipo == "Empleado":
            if Nom.get() == "Arellano" and Con.get() == "1234":
                nomos = Nom.get()
                messagebox.showinfo("Digital Bell", "Bienvenido administrador")
                Administrador2.Menu_Admin()
            else:
                for Empleado in Usuario:
                    if Empleado['Nombre'] == Nom.get() and Empleado['Contraseña'] == Con.get():
                        nomos = Nom.get()
                        messagebox.showinfo("Digital Bell", "Bienvenido " + Nom.get())
                        Empleado2.Menu_Empleado()

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

Texto = tk.Label(ventana, text = "Bienvenid@ a Digital Bell", font = ("Myanmar Khyay",20))
Texto.pack(side = tk.TOP, pady = 10)
Registra = tk.Button(ventana, text = "Crear cuenta", command = lambda: Registro(ventana,Registrar_Usuario), font = ("Myanmar Sans Pro", 15))
Registra.pack(side = tk.TOP, pady = 10,padx = 10)
Sesion = tk.Button(ventana, text = "Iniciar Sesión", command = Iniciar_Sesion, font = ("Myanmar Sans Pro", 15))
Sesion.pack(side = tk.TOP, pady = 10,padx = 10)
Salir = tk.Button(ventana, text = "Salir", command = ventana.quit, font = ("Myanmar Sans Pro", 15))
Salir.pack(pady = 5)

if __name__ == "__main__":
    ventana.mainloop()