from Dispositivos_de_Entrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contador_de_teclado = 0

    @classmethod
    def contador(cls):
        cls.contador_de_teclado += 1
        return cls.contador_de_teclado

    def __init__(self, marca, tipoEntrada) -> None:
        super().__init__(marca, tipoEntrada)
        self._id_teclado = Teclado.contador()
    
    @property
    def id_teclado(self):
        return self._id_teclado
    
    @id_teclado.setter
    def id_teclado(self, nuevo_id):
        self._id_teclado = nuevo_id
    
    def __str__(self) -> str:
        return f'id: {self._id_teclado}, {super().__str__()}'

if __name__ == '__main__':
    teclado1 = Teclado('Weibo', 'USB')
    print(teclado1)
    # id: 1, Marca: Weibo, Tipo de Entrada: USB
    print(teclado1.id_teclado)
    # 1
    print(teclado1.marca)
    # Weibo
    print(teclado1.tipoEntrada)
    # USB

    teclado1.id_teclado = 221
    print(teclado1)
    # id: 221, Marca: Weibo, Tipo de Entrada: USB

    # El metodo set de marca y tipo de entrada ya comprobamos que funcionan en el modulo Dispositivos_de_Entrada