
COEFICIENTE_CORRECCION_NORTE = 1
COEFICIENTE_CORRECCION_SUR = 0.5 
COEFICIENTE_CORRECCION_TECHO = 1.5

def conductividad(cerramiento):
    if cerramiento.tipo != 'Techo':

        if cerramiento.orientacion == 'N':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_NORTE
        elif cerramiento.orientacion == 'S':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_SUR
        elif cerramiento.orientacion == 'E':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_NORTE
        elif cerramiento.orientacion == 'O':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_NORTE
        elif cerramiento.orientacion == 'NO':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_NORTE
        elif cerramiento.orientacion == 'SE':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_SUR
        elif cerramiento.orientacion == 'NE':
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_NORTE
        else:
            conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_SUR
    else:
        conductividad = cerramiento.material.conductividad*COEFICIENTE_CORRECCION_TECHO

    return conductividad
    

def hay_techo(cerramientos):
    for cerramiento in cerramientos:
        if cerramiento.tipo == 'Techo':
            return True
    return False


