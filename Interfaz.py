import tkinter as tk

def mostrar_elementos():
    # Limpiar el contenido previo
    texto.delete(1.0, tk.END)
    
    # Obtener los elementos del arreglo
    for elemento in arreglo:
        texto.insert(tk.END, str(elemento) + "\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Elementos de un Arreglo con Scrollbar")

# Crear un arreglo (lista)
arreglo = [i for i in range(1, 101)]  # Ejemplo de 100 elementos

# Crear un marco para contener el Text y la Scrollbar
frame = tk.Frame(ventana)
frame.pack()

# Crear un widget Text para mostrar los elementos
texto = tk.Text(frame, height=10, width=30)
texto.pack(side=tk.LEFT)

# Crear una scrollbar
scrollbar = tk.Scrollbar(frame, command=texto.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar el Text para usar la scrollbar
texto.config(yscrollcommand=scrollbar.set)

# Crear un botón para mostrar los elementos
boton = tk.Button(ventana, text="Mostrar Elementos", command=mostrar_elementos)
boton.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()