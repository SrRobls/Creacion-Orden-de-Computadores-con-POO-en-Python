from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computador import Computadora

class Orden():
    contador_orden = 0

    @classmethod
    def contador(cls):
        cls.contador_orden += 1
        return cls.contador_orden
    
    def __init__(self, listaOrden = []) -> None:
        self._id_orden = Orden.contador()
        self._listaOrden = listaOrden
    
    @property
    def id_orden(self):
        return self._id_orden
    
    @id_orden.setter
    def id_orden(self, nuevo_id):
        self._id_orden = nuevo_id
    
    @property
    def listaOrden(self):
        return self._listaOrden
    
    @listaOrden.setter
    def listaOrden(self, nueva_orden):
        self._listaOrden = nueva_orden
    
    def agragarComputadora(self, computadora):
        if isinstance(computadora, Computadora):
            self._listaOrden.append(computadora)
        else:
            print('Error: El parametro dado NO es un obejeto Computadora')
    
    def __str__(self) -> str:
        string =  f'Orden {self._id_orden}: Computadoras\n'
        for computador in self._listaOrden:
            string += f'  {computador.__str__()}\n\n'
        return string
if __name__ == '__main__':
    orden1 = Orden()

    # Computador 1:
    teclado1 = Teclado('Weibo', 'USB')
    monitor1 = Monitor('Acer', '1080x720')
    mouse1 = Raton('Weibo', 'USB')
    computador1 = Computadora('Pc Personal', monitor1, teclado1, mouse1)

    # Computador 2:
    teclado2 = Teclado('Asus', 'USB')
    monitor2 = Monitor('Lenovo', '1080x720')
    mouse2 = Raton('Asus', 'USB')
    computador2 = Computadora('Pc Gamer', monitor2, teclado2, mouse2)

    orden1.agragarComputadora(computador1)
    orden1.agragarComputadora(computador2)
    print(orden1)
    '''
    Orden 1: Computadoras
        Pc Personal: 1
                Monitor: Id: 1, Marca: Acer, Tamaño: 1080x720
                Teclado: id: 1, Marca: Weibo, Tipo de Entrada: USB
                Raton: Id: 1, Marca: Weibo, Tipo de Entrada: USB

        Pc Gamer: 2
                Monitor: Id: 2, Marca: Lenovo, Tamaño: 1080x720
                Teclado: id: 2, Marca: Asus, Tipo de Entrada: USB
                Raton: Id: 2, Marca: Asus, Tipo de Entrada: USB
    '''

    monitor3 = Monitor('HP', '2450X2980')
    computador1.obj_monitor = monitor3
    print(orden1)
    '''
    Orden 1: Computadoras
        Pc Personal: 1
                Monitor: Id: 3, Marca: HP, Tamaño: 2450X2980
                Teclado: id: 1, Marca: Weibo, Tipo de Entrada: USB
                Raton: Id: 1, Marca: Weibo, Tipo de Entrada: USB

        Pc Gamer: 2
                Monitor: Id: 2, Marca: Lenovo, Tamaño: 1080x720
                Teclado: id: 2, Marca: Asus, Tipo de Entrada: USB
                Raton: Id: 2, Marca: Asus, Tipo de Entrada: USB
    '''

    computador1.obj_raton = Raton('HP', 'Inalambrica')
    print(orden1)
    '''
    Orden 1: Computadoras
        Pc Personal: 1
                Monitor: Id: 3, Marca: HP, Tamaño: 2450X2980
                Teclado: id: 1, Marca: Weibo, Tipo de Entrada: USB
                Raton: Id: 3, Marca: HP, Tipo de Entrada: Inalambrica

        Pc Gamer: 2
                Monitor: Id: 2, Marca: Lenovo, Tamaño: 1080x720
                Teclado: id: 2, Marca: Asus, Tipo de Entrada: USB
                Raton: Id: 2, Marca: Asus, Tipo de Entrada: USB
    '''