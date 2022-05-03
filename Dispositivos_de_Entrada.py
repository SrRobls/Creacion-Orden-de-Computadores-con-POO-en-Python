class DispositivosEntrada():
    def __init__(self, marca, tipoEntrada) -> None:
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    
    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, nuevo_tipo):
        self._tipoEntrada = nuevo_tipo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca
    
    def __str__(self) -> str:
        return f'Marca: {self._marca}, Tipo de Entrada: {self._tipoEntrada}'

if __name__ == '__main__':
    teclado = DispositivosEntrada('USB', 'HP')
    print(teclado)
    # Marca: HP, Tipo de Entrada: USB
    print(teclado.marca)
    # HP
    print(teclado.tipoEntrada)
    # USB
    teclado.marca = 'ACER'
    teclado.tipoEntrada = 'Inalambrico'
    print(teclado)
    # Marca: ACER, Tipo de Entrada: Inalambrico

