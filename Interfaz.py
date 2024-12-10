import tkinter as tk
from tkinter import messagebox

def verificar_campos():
    # Obtener el contenido de los campos de texto
    campo1 = entry1.get()
    campo2 = entry2.get()
    
    # Verificar si alguno de los campos está vacío
    if not campo1 or not campo2:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    else:
        messagebox.showinfo("Éxito", "Todos los campos están llenos. Procediendo...")
        # Aquí puedes agregar la lógica para proceder

# Crear la ventana principal
root = tk.Tk()
root.title("Verificación de Campos")

# Crear campos de texto
entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

# Crear un botón para verificar los campos
boton_verificar = tk.Button(root, text="Verificar Campos", command=verificar_campos)
boton_verificar.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()