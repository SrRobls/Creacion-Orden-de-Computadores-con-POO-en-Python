# from Dispositivos_de_Entrada import DispositivosEntrada
from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor

class Computadora():
    contador_computador = 0

    @classmethod
    def contador(cls):
        cls.contador_computador += 1
        return cls.contador_computador

    def __init__(self, nombre, obj_monitor, obj_teclado, obj_raton) -> None:
        self._id_computador = Computadora.contador()
        self._nombre = nombre
        self._obj_monitor = obj_monitor
        self._obj_teclado = obj_teclado
        self._obj_raton = obj_raton
    
    @property
    def id_computador(self):
        return self._id_computador
    
    @id_computador.setter
    def id_computador(self, nueva_id):
        self._id_computador = nueva_id
    
    @property
    def obj_monitor(self):
        return self._obj_monitor
    
    @obj_monitor.setter
    def obj_monitor(self, nuevo_monitor):
        self._obj_monitor = nuevo_monitor
    
    @property
    def obj_teclado(self):
        return self._obj_teclado
    
    @obj_teclado.setter
    def obj_teclado(self, nuevo_teclado):
        self._obj_teclado = nuevo_teclado
    
    @property
    def obj_raton(self):
        return self._obj_raton
    
    @obj_raton.setter
    def obj_raton(self, nuevo_raton):
        self._obj_raton = nuevo_raton
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def __str__(self) -> str:
        return f'{self._nombre}: {self._id_computador}\n\t Monitor: {self._obj_monitor}\n\t Teclado: {self._obj_teclado}\n\t Raton: {self._obj_raton}'



if __name__ == '__main__':
    teclado1 = Teclado('Weibo', 'USB')
    monitor1 = Monitor('Acer', '1080x720')
    mouse1 = Raton('Weibo', 'USB')
    computador1 = Computadora('Pc Personal', monitor1, teclado1, mouse1)

    print(computador1)
    '''
    Pc Personal: 1
         Monitor: Id: 1, Marca: Acer, Tamaño: 1080x720
         Teclado: id: 1, Marca: Weibo, Tipo de Entrada: USB
         Raton: Id: 1, Marca: Weibo, Tipo de Entrada: USB
    '''
    print(computador1.nombre)
    print(computador1.id_computador)
    print(computador1.obj_monitor)
    print(computador1.obj_teclado)
    print(computador1.obj_raton)
    '''
    Pc Personal
    1
    Id: 1, Marca: Acer, Tamaño: 1080x720
    id: 1, Marca: Weibo, Tipo de Entrada: USB
    Id: 1, Marca: Weibo, Tipo de Entrada: US
    '''
    computador1.nombre = 'Pc Gamer'
    computador1.id_computador = 777
    computador1.obj_monitor = Monitor('Lenovo', '1920x1080')
    computador1.obj_teclado = Teclado('Asus', 'Bluethoo')
    computador1.obj_raton = Raton('Asus', 'Bluehtoo')

    print(computador1)
    '''
    Pc Gamer: 777
         Monitor: Id: 2, Marca: Lenovo, Tamaño: 1920x1080
         Teclado: id: 2, Marca: Asus, Tipo de Entrada: Bluethoo
         Raton: Id: 2, Marca: Asus, Tipo de Entrada: Bluehtoo
    '''