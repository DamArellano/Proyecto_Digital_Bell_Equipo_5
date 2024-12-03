import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Digital Bell")
ventana.geometry("500x500")
Usuario = []
Queja = []
Horario = []
global nomos
def Menu_Habitante():
    global Usuario,nomos

    for widget in ventana.winfo_children():
        widget.destroy()
    
    Texto = tk.Label(ventana, text = ("Bienvenido ",nomos), font = ("Myanmar Khyay", 15))
    Texto.pack(side = tk.TOP)

    Sugerencias = tk.Button(ventana, text = "Quejas y Sugerencias", command = Quejas_Habitante, font = ("Myanmar Sans Pro", 10))
    Sugerencias.pack(side = tk.TOP, pady = 10,padx = 10)

    Horarios = tk.Button(ventana, text = "Horarios y rutas del día", command = Horario_Habitante)
    Horarios.pack(side = tk.TOP, pady = 10,padx = 10)

    Cerrar = tk.Button(ventana, text = "Cerrar Sesión", command = Cerrar_Sesion)
    Cerrar.pack(side = tk.TOP)

def Quejas_Habitante():
    global Usuario,nomos

    for widget in ventana.winfo_children:
        widget.destroy()
    
    def Guardar_Queja():
        global nomos
        Sug = Sugerencia.get()
        Usuario = nomos
        Sugerencia = {
            "Usuario": Usuario,
            "Queja": Sug
        }
        Queja.append(Sugerencia)
        messagebox

    Texto = tk.Label(ventana, text = ("Quejas y sugerencias"), font = ("Myanmar Khyay", 15))
    Texto.pack(side = tk.TOP, pady = 10)
    Sugerencia = tk.Text(ventana, height = 20, width = 50)
    Sugerencia.pack(side = tk.TOP, pady = 10)
    Enviar = tk.Button(ventana, text = "Enviar queja", command = lambda: Guardar_Queja(Sugerencia))
    Enviar.pack(side = tk.TOP, pady = 10)
    Regresar = tk.Button(ventana, text = "Volver al menu", command = "Menu_Habitante")
    Regresar.pack(side = tk.TOP, pady = 10)

def Horario_Habitante():
    global Usuario,nomos

    for widget in ventana.winfo_children:
        widget.destroy()
    
    if not Horario:
        Horario = tk.Label(ventana, text = "No hay horarios asignados aún")
        Horario.pack(side = tk.TOP,pady = 20)
    else:
        for ruta in Horario:
            Direccion = tk.Label(ventana, text = ruta)
            Direccion.pack(side = tk.TOP,pady = 10)
    #Debo repasar grafos para esto

def Cerrar_Sesion():
    global nomos
    Cerrar_Sesion = messagebox.askyesno("Digital Bell", "¿Desea cerrar sesión?")
    if Cerrar_Sesion:
        nomos = ""
        Menu()
    else:
        messagebox.showinfo("Digital Bell", "No se pudo cerrar sesión")
