import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de tk.Text")

# Crear un widget Text
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Agregar algo de texto inicial
text_widget.insert(tk.END, "Escribe aquí tu texto...\n")

# Iniciar el bucle principal
root.mainloop()