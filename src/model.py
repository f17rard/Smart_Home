from dataclasses import dataclass
from typing import Optional, Set
from datetime import date
from abc import ABC, abstractmethod

@dataclass
class TarjetaRed:
    direccion_mac: str
    frecuencia_ghz: float
    
@dataclass
class Dispositivo(ABC):
    name: str
    bateria = 100
    
    @abstractmethod
    def consumo_energia(energia: int):
        pass

class LucesInteligentes(Dispositivo):
    
    def consumo_energia(self):
        self.bateria -= 2.5
        return self.bateria
    
class AireAcondicionado(Dispositivo):
    
    def consumo_energia(self, energia):
        self.bateria -= self.bateria*energia

class CentralHub:
    def __init__(self, name: str, room: str, direc_mac:str, frecu_ghz: float):
        self.name = name
        self.room = room
        self._dispositivios = []
        self.TarjetaR = TarjetaRed(direc_mac, frecu_ghz)
    
    def __pos__init__(self): #verificar que no hayan más de 4 dispositivos
        if(len(self._dispositivios) == 4):
            raise ValueError("Capacidad de la central agotada.")
        
    

# LI01 = LucesInteligentes("Luz_cuarto")
# consumo = LI01.consumo_energia()
# print(consumo)
