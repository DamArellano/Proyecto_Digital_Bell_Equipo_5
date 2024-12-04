import tkinter as tk
from tkinter import messagebox
from MenuPrincipal import nomos,Usuario,Queja,Horario

def Administrador():
    ventana = tk.Tk()
    ventana.title("Digital Bell")
    ventana.geometry("500x500")
    from MenuPrincipal import Menu

    def Menu_Admin():
        global Usuario,nomos

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

    #Para horarios se requiere: Grafos
    def Ingresar_Horarios():
        global Horario

        for widget in ventana.winfo_children:
            widget.destroy()
        def Asignar_Horarios():
            global Horario
            Empleado = Num.get()
            Comienzo = Partida.get()
            Dir1 = Calle1.get()
            Dir2 = Calle2.get()
            Dir3 = Calle3.get()

            Ruta = {
                "Empleado": Empleado,
                "Direccion": Dir1 + " " + Dir2 + " " + Dir3,
                "Ubicacion": Comienzo
            }
            Horario.append(Ruta)
            messagebox.showinfo("Horarios", "Horario asignado con éxito")
            Menu_Admin

        Texto = tk.Label(ventana, text = "Horarios y rutas")
        Texto.pack(side = tk.TOP, pady = 10)
        Texto1 = tk.Label(ventana, text = "Número de Empleado")
        Texto1.pack(side = tk.TOP, pady = 10)
        Num = tk.Entry(ventana)
        Num.pack(side = tk.TOP, pady = 10)
        Texto5 = tk.Label(ventana, text = "¿Por donde va a empezar el recorrido?")
        Texto5.pack(side = tk.TOP, pady = 10)
        Partida = tk.Entry(ventana)
        Partida.pack(side = tk.TOP, pady = 10)
        Texto2 = tk.Label(ventana, text = "Ingrese la primer dirección")
        Texto2.pack(side = tk.TOP, pady = 10)
        Calle1 = tk.Entry(ventana)
        Calle1.pack(side = tk.TOP, pady = 10)
        Texto3 = tk.Label(ventana, text = "Ingrese la segunda dirección")
        Texto3.pack(side = tk.TOP, pady = 10)
        Calle2 = tk.Entry(ventana)
        Calle2.pack(side = tk.TOP, pady = 10)
        Texto4 = tk.Label(ventana, text = "Ingrese la tercer dirección")
        Texto4.pack(side = tk.TOP, pady = 10)
        Calle3 = tk.Entry(ventana)
        Calle3.pack(side = tk.TOP, pady = 10)

        Asignar = tk.Button(ventana, text = "Asignar horarios", command = lambda: Asignar_Horarios())
        Asignar.pack(side = tk.TOP, pady = 10)
        Regresar = tk.Button(ventana, text = "Regresar", command = Menu_Admin)
        Regresar.pack(side = tk.TOP, pady = 10)
        #¿Cómo se tomaran las rutas?

    def Actualizar_Ubicacion():
        global Horario

        for widget in ventana.winfo_children:
            widget.destroy()
        
        Texto = tk.Label(ventana, text = "Ingrese el número de empleado")
        Texto.pack(side = tk.TOP, pady = 10)
        Num = tk.Entry(ventana)
        Num.pack(side = tk.TOP, pady = 10)
        

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
    
    ventana.mainloop()