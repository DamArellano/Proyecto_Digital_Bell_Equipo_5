<<<<<<< HEAD
import Logica_Empleado
import Logica_Habitante
import Logica_Administrador
import Interfaz

def main():
    #Diccionario con la la logica del programa
    logica_programa = {
        "Registro_Habitante": Logica_Habitante.Registrar_Habitante,
        "Enviar_Queja": Logica_Habitante.QuejaHa,
        "Mostrar_Horarios": Logica_Empleado.Mostrar_Horarios,
        "Registro_Empleado": Logica_Empleado.Registrar_Empleado,
        "Horarios": Logica_Administrador.AsH,
        "Ac_Ubicacion": Logica_Administrador.Ubicacion
    }

    Interfaz.crear_interfaz(logica_programa)

=======
import Logica_Empleado
import Logica_Habitante
import Logica_Administrador
import Interfaz

def main():
    #Diccionario con la la logica del programa
    logica_programa = {
        "Registro_Habitante": Logica_Habitante.Registrar_Habitante,
        "Enviar_Queja": Logica_Habitante.QuejaHa,
        "Mostrar_Horarios": Logica_Empleado.Mostrar_Horarios,
        "Registro_Empleado": Logica_Empleado.Registrar_Empleado,
        "Ac_Ubicacion": Logica_Administrador.Ubicacion,
        "Horarios": Logica_Administrador.AsH,
    }

    Interfaz.crear_interfaz(logica_programa)

>>>>>>> 50ff8ac17f2339123c6fb408087a9b286b846b1d
main()