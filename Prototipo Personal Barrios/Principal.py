import Logica_Empleado
import Logica_Habitante
import Logica_Administrador
import Interfaz

def main():
    #Diccionario con la la logica del programa
    logica_programa = {
        "Registro_Habitante": Logica_Habitante.Registrar_Habitante,
        "Enviar_Queja": Logica_Habitante.QuejaHa,
        "Ver_Horarios": Logica_Habitante.Mostrar_Horarios,
        "Mostrar_Horarios": Logica_Empleado.Mostrar_Horarios,
        "Registro_Empleado": Logica_Empleado.Registrar_Empleado,
        "Horarios": Logica_Administrador.AsH,
    }

    Interfaz.crear_interfaz(logica_programa)

main()