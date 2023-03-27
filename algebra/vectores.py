"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: RAfael A. Echevarria Silva
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other

    def __mul__(self, other):
        """
        Multiplicación de los elementos de dos vectores, o de un vector * un escalar.
        """
        if isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.data, other.data)])
        elif isinstance(other, (int, float, complex)):
            return Vector([other * x for x in self.data])


    def __rmul__(self, other):
        """
        
        """
        return self.__mul__(other)
    
    def __matmul__(self, other):
        if isinstance(other, Vector):
           return sum([a * b for a, b in zip(self, other)])
        
    def __rmatmul__(self, other):
        return self.__matmul__(other)
    
    def __floordiv__(self, other):
        """
        
        """     
        if isinstance(other, Vector):
            magnitud_self = sum([x ** 2 for x in self]) ** 0.5
            magnitud_other = sum([x ** 2 for x in other]) ** 0.5
            producto_punto = sum([a * b for a, b in zip(self, other)])
            return Vector([producto_punto / (magnitud_self * magnitud_other) * x for x in other])
        elif isinstance(other, (int, float, complex)):
            magnitud = sum([x ** 2 for x in self]) ** 0.5
            return Vector([other * x / magnitud for x in self])