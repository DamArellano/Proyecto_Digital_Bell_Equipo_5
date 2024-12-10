import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Lista de Diccionarios")

# Crear el Treeview
tree = ttk.Treeview(ventana, columns=("Nombre", "Edad", "Ciudad"), show='headings')
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.heading("Ciudad", text="Ciudad")
tree.column("Nombre", anchor="center")
tree.column("Edad", anchor="center")
tree.column("Ciudad", anchor="center")

# Agregar el Treeview a la ventana
tree.pack(pady=20)

# Ejemplo de lista de diccionarios
lista_diccionarios = [
    {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 25, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 28, "Ciudad": "Valencia"}
]

# Insertar datos en el Treeview
for diccionario in lista_diccionarios:
    tree.insert("", tk.END, values=(diccionario["Nombre"], diccionario["Edad"], diccionario["Ciudad"]))

# Ejecutar el bucle principal
ventana.mainloop()