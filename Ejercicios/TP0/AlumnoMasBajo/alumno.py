def indice_mas_bajo(alumnos):
    return _indice_mas_bajo_auxiliar(alumnos, 0, len(alumnos) - 1)

def validar_mas_bajo(alumnos, indice):
    return alumnos[indice].altura <= alumnos[indice+1].altura and alumnos[indice].altura <= alumnos[indice - 1].altura

def _indice_mas_bajo_auxiliar(alumnos, inicio, fin):
    mitad = (inicio + fin) //2

    if (validar_mas_bajo(alumnos, mitad)):
        return mitad
    elif alumnos[mitad - 1].altura < alumnos[mitad].altura:
        return _indice_mas_bajo_auxiliar(alumnos, inicio, mitad - 1)
    else:
        return _indice_mas_bajo_auxiliar(alumnos, mitad + 1, fin)

class Alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura