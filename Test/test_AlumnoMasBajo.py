from unittest import TestCase
from AlumnoMasBajo import Alumno
from AlumnoMasBajo import AlumnoMasBajo
class TestAlumnoMasBajo(TestCase):

    _alturas = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23]

    def setUp(self):
        self.alumnos = []
        for i in range(len(self._alturas)):
            self.alumnos.append(Alumno(f"alumno_{i}", self._alturas[i]))
    def test_indice_mas_bajo(self):
        indice = AlumnoMasBajo.indice_mas_bajo(self.alumnos)

        self.assertTrue(AlumnoMasBajo.validar_mas_bajo(self.alumnos, indice))
    def test_validar_mas_bajo(self):
        self.assertFalse(AlumnoMasBajo.validar_mas_bajo(self.alumnos, 0))

        self.assertTrue(AlumnoMasBajo.validar_mas_bajo(self.alumnos, 5))

        self.assertFalse(AlumnoMasBajo.validar_mas_bajo(self.alumnos, 4))

        self.assertFalse(AlumnoMasBajo.validar_mas_bajo(self.alumnos, 6))


