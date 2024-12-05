import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Obtener la resolución de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Ajustar el tamaño de la ventana a la resolución de la pantalla
root.geometry(f"{screen_width}x{screen_height}")

# Crear un frame (y ajustarlo al tamaño de la ventana)
frame = tk.Frame(root, width=screen_width, height=screen_height)
frame.pack(fill=tk.BOTH, expand=True)

# Mostrar la ventana
root.mainloop()