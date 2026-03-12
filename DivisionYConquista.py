def integer_sqrt(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz entera de un número negativo")
    elif n < 2:
        return n
    def binary_search(left, right, target):
        while left <= right:
            mid = (left + right) // 2
            mid_square = mid * mid
            if mid_square == target:
                return mid
            elif mid_square < target:
                left = mid + 1
            else:
                right = mid - 1
        return right  # Devuelve el valor más cercano por debajo de la raíz cuadrada

    return binary_search(0, n, n)

class DivisionYConquista:
    @staticmethod
    def parte_entera_raiz(n):
        return integer_sqrt(n)