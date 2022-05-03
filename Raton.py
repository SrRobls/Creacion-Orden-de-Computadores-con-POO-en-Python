from Dispositivos_de_Entrada import DispositivosEntrada

class Raton(DispositivosEntrada):
    contador_Raton = 0

    @classmethod
    def contador(cls):
        cls.contador_Raton += 1
        return cls.contador_Raton
    
    def __init__(self, marca, tipoEntrada) -> None:
        super().__init__(marca, tipoEntrada)
        self._id_raton = Raton.contador()

    @property
    def id_raton(self):
        return self._id_raton
    
    @id_raton.setter
    def id_raton(self, nuevo_id):
        self._id_raton = nuevo_id
    
    def __str__(self) -> str:
        return f'Id: {self._id_raton}, {super().__str__()}'

if __name__ == '__main__':
    mouse1 = Raton('Weibo', 'USB')
    print(mouse1)
    # id: 1, Marca: Weibo, Tipo de Entrada: USB
    print(mouse1.id_raton)
    # 1
    print(mouse1.marca)
    # Weibo
    print(mouse1.tipoEntrada)
    # USB

    mouse1.id_raton = 221
    print(mouse1)
    # id: 221, Marca: Weibo, Tipo de Entrada: USB