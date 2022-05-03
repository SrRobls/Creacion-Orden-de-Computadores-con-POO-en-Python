
class Monitor():
    contador_monitor = 0

    @classmethod
    def contador(cls):
        cls.contador_monitor += 1
        return cls.contador_monitor
    
    def __init__(self, marca, tamaño) -> None:
        self._id_monitor = Monitor.contador()
        self._marca = marca
        self._tamaño = tamaño
    
    @property
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño
    
    @property
    def id_monitor(self):
        return self._id_monitor
    
    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca
    
    @tamaño.setter
    def tamaño(self, nueva_tamaño):
        self._tamaño = nueva_tamaño
    
    @id_monitor.setter
    def id_monitor(self, nuevo_id):
        self._id_monitor = nuevo_id
    

    def __str__(self) -> str:
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'

if __name__ == '__main__':
    monitor1 = Monitor('Acer', '1080x720')
    print(monitor1)
    # Id: 1, Marca: Acer, Tamaño: 1080x720
    print(monitor1.marca)
    # Acer
    print(monitor1.tamaño)
    # 1080x720
    print(monitor1.id_monitor)
    # 1

    monitor1.marca = 'HP'
    print(monitor1)
    # Id: 1, Marca: HP, Tamaño: 1080x720