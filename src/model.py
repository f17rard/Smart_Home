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
    def _consumo_energia(energia: int):
        pass

class LuzInteligente(Dispositivo):
    
    def _consumo_energia(self, energia):
        self.bateria -= 2.5
        return self.bateria
    
class AireAcondicionado(Dispositivo):
    
    def _consumo_energia(self, energia):
        self.bateria -= self.bateria*energia/1000
        return self.bateria

class CentralHub:
    def __init__(self, name: str, room: str, direc_mac:str, frecu_ghz: float):
        self.name = name
        self.room = room
        self.__dispositivos = []
        self.TarjetaR = TarjetaRed(direc_mac, frecu_ghz)
        self.Cbateria = 100
    
    def Añadir_dispositivo(self, dispositivo):
        if len(self.__dispositivos) >= 4:
            raise ValueError("Capacidad de la central agotada.")
        self.__dispositivos.append(dispositivo)
        
    def iniciar_ciclo(self, energia: int):
        consumo = 0
        for dispo in self.__dispositivos:
            consumo = dispo._consumo_energia(energia)
            self.Cbateria -= consumo/len(self.__dispositivos)
        
        print(consumo)
            
    def lista_dispositivos(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.name)
        
    

LI01 = LuzInteligente("Luz_cuarto")
LI02 = LuzInteligente("Luz_escitorio")
AC01 = AireAcondicionado("AC_cuarto")
LI03 = LuzInteligente("luz_nocturna")
LI04 = LuzInteligente("luz luz")

CH01 = CentralHub("HUB-01", "habitación", "direc_mac", 5.0)

CH01.Añadir_dispositivo(LI01)
CH01.Añadir_dispositivo(LI02)
CH01.Añadir_dispositivo(LI03)
CH01.Añadir_dispositivo(AC01)

CH01.iniciar_ciclo(50)