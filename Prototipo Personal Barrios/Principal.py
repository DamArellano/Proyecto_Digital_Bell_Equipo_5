import Interfaz
import Logica_Empleado
import Logica_Habitante

Usuario = []
Queja = []
Horario = []
nomos = ""

def main():
    global nomos, Usuario, Queja, nomos

    #Diccionario con la la logica del programa
    logica_programa = {
        "Registro_Habitante": Logica_Habitante.Registrar_Habitante,
        "Enviar_Queja": Logica_Habitante.QuejaHa,
        "Registro_Empleado": Logica_Empleado.Registrar_Empleado,
    }

    Interfaz.crear_interfaz(logica_programa)

main()