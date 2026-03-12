
class Alumno:
    nombre = ""
    altura = 0

    def __init__(self, _nombre, _altura):
        self.nombre = _nombre
        self.altura = _altura

class AlumnoMasBajo:

    @staticmethod
    def _indice_mas_bajo(alumnos : list[Alumno], indice_actual, indice_final):
        #Condicion de corte
        if (indice_actual >= indice_final):
            return indice_actual

        if (AlumnoMasBajo.validar_mas_bajo(alumnos, indice_actual)):
            return indice_actual

        mitad = (indice_final + indice_actual) // 2

        if (alumnos[mitad - 1].altura > alumnos[mitad].altura):
            return AlumnoMasBajo._indice_mas_bajo(alumnos, mitad, indice_final)
        elif (alumnos[mitad -1].altura < alumnos[mitad].altura):
            return AlumnoMasBajo._indice_mas_bajo(alumnos, indice_actual, mitad)
    @staticmethod
    def indice_mas_bajo(alumnos : list[Alumno]):
        return AlumnoMasBajo._indice_mas_bajo(alumnos, 0, len(alumnos))
    @staticmethod
    def validar_mas_bajo(alumnos : list[Alumno], indice):
        cantidadDeAlumnos = len(alumnos)
        if (cantidadDeAlumnos == 1): return True

        if (indice + 1 < cantidadDeAlumnos and indice - 1 >= 0):
            return alumnos[indice - 1].altura > alumnos[indice].altura and alumnos[indice + 1].altura > alumnos[indice].altura

        elif (indice + 1 == cantidadDeAlumnos): return alumnos[indice].altura < alumnos[indice - 1].altura

        elif (indice - 1 < 0): return alumnos[indice].altura < alumnos[indice + 1].altura

