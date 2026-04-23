from unittest import TestCase

import Ejercicios.RPL04_PD.E11_Operaciones_k as pd


class TestRPL04OperacionesK(TestCase):
	def _resolver_funcion_objetivo(self):
		if hasattr(pd, "operaciones"):
			return pd.operaciones
		if hasattr(pd, "operaciones_k"):
			return pd.operaciones_k
		self.fail("No se encontro la funcion objetivo. Defini operaciones(k) u operaciones_k(k)")

	def _resolver(self, k):
		funcion = self._resolver_funcion_objetivo()
		return funcion(k)

	def _aplicar_operaciones(self, operaciones):
		valor = 0
		for op in operaciones:
			if op == "mas1":
				valor += 1
			elif op == "por2":
				valor *= 2
			else:
				self.fail("Operacion invalida: solo se permite 'mas1' o 'por2'")
		return valor

	def _min_operaciones_optimo(self, k):
		if k == 0:
			return 0

		dp = [0] * (k + 1)
		for n in range(1, k + 1):
			dp[n] = dp[n - 1] + 1
			if n % 2 == 0:
				dp[n] = min(dp[n], dp[n // 2] + 1)
		return dp[k]

	def _assert_solucion_optima(self, k):
		operaciones = self._resolver(k)

		self.assertIsNotNone(operaciones)
		self.assertEqual(k, self._aplicar_operaciones(operaciones))
		self.assertEqual(self._min_operaciones_optimo(k), len(operaciones))

	def test_k_cero_retorna_lista_vacia(self):
		self.assertEqual([], self._resolver(0))

	def test_k_uno_requiere_una_operacion(self):
		self._assert_solucion_optima(1)

	def test_k_dos_requiere_dos_operaciones(self):
		self._assert_solucion_optima(2)

	def test_k_tres_requiere_tres_operaciones(self):
		self._assert_solucion_optima(3)

	def test_k_potencia_de_dos(self):
		self._assert_solucion_optima(16)

	def test_k_impar_grande(self):
		self._assert_solucion_optima(31)

	def test_k_par_no_potencia_de_dos(self):
		self._assert_solucion_optima(18)

	def test_k_cien(self):
		self._assert_solucion_optima(100)
