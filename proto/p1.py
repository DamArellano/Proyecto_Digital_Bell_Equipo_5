import tkinter as tk 
def op_reg():
    frame1.pack_forget()
    frame3.pack(fill="both", expend=True)
def reg1():
    frame3.pack_forget()
    frame1.pack(fill="both", expand=True)
def op_is():
    frame1.pack_forget()
    frame3.pack(fill="both", expand=True)
root = tk.Tk()
root.title("Digital Bell")
root.geometry("1920x1080")
root.config(bg="black")
frame1= tk.Frame(root, bg="gray", padx=63, pady=75)
frame1.pack(padx=400, pady=100, fill="both", expand=True)
label1=tk.Label(frame1, text="Digital Bell", width=28, height=-2, bg="gray", font=("Myanmar Khyay", 20))
label1.grid(pady=2)
button1 = tk.Button(frame1, text="Iniciar Sesion", width=32, height=3, bg="darkgreen", font=("arial", 15), command=op_is)
button1.grid(pady=70)
button2 = tk.Button(frame1, text="Registrarse", width=32, height=3, bg="green", font=("arial", 15), command=op_reg)
button2.grid(pady=1)
frame1.pack(fill="both", expand=True)
frame3=tk.Frame(root, bg="grey", padx=45, pady=60)
frame3.pack(padx=400, pady=100, fill="both", expand=True)
label3=tk.Label(frame3, text="Registro", width=28, height=-2, bg="gray", font=("Myanmar Khyay", 25))
label3.grid(pady=2)
button1 = tk.Button(frame3, text="Habitante", width=32, height=3, bg="darkgreen", font=("arial", 15))
button1.grid(pady=70)
button2 = tk.Button(frame3, text="Empleado", width=32, height=3, bg="green", font=("arial", 15))
button2.grid(pady=1)
button3 = tk.Button(frame3, text="Regresar", width=27, height=2, bg="darkgreen", font=("arial", 15), command=reg1)
button3.grid(pady=70)
frame3.pack(fill="both", expand=True)
root.mainloop()
