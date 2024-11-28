import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Cuadros de Entrada en 4 Columnas")

# Crear un marco para contener los cuadros de entrada
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear cuadros de entrada con tamaños individuales
entry1 = tk.Entry(frame, width=30)  # Ancho 30
entry1.grid(row=0, column=0, padx=5, pady=5, sticky='w')

entry2 = tk.Entry(frame, width=20)  # Ancho 20
entry2.grid(row=0, column=1, padx=5, pady=5, sticky='w')

entry3 = tk.Entry(frame, width=10)  # Ancho 10
entry3.grid(row=0, column=2, padx=5, pady=5, sticky='w')

entry4 = tk.Entry(frame, width=15)  # Ancho 15
entry4.grid(row=0, column=3, padx=5, pady=5, sticky='w')

# Ajustar el tamaño de las columnas
frame.grid_columnconfigure(0, minsize=100)  # Asegurar que la columna 0 tenga un tamaño mínimo
frame.grid_columnconfigure(1, minsize=80)   # Asegurar que la columna 1 tenga un tamaño mínimo
frame.grid_columnconfigure(2, minsize=60)   # Asegurar que la columna 2 tenga un tamaño mínimo
frame.grid_columnconfigure(3, minsize=90)   # Asegurar que la columna 3 tenga un tamaño mínimo

# Iniciar el bucle principal
root.mainloop()