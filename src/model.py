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
    bateria: float = 100.0
    
    @abstractmethod
    def _consumo_energia(self, energia: float):
        pass

class LuzInteligente(Dispositivo):
    
    def _consumo_energia(self, energia):
        self.bateria -= 2.5
        return self.bateria
    
class AireAcondicionado(Dispositivo):
    
    def _consumo_energia(self, temperatura):
        self.bateria = self.bateria*temperatura/1000
        return self.bateria
    
# --------------Central HUB ----------------------------

class CentralHub:
    def __init__(self, name: str, room: str, direc_mac:str, frecu_ghz: float):
        self.name = name
        self.room = room
        self._dispositivos = []
        self.TarjetaR = TarjetaRed(direc_mac, frecu_ghz)
    
    def Añadir_dispositivo(self, dispositivo):
        if len(self._dispositivos) >= 4:
            raise ValueError("Capacidad de la central agotada.")
        self._dispositivos.append(dispositivo)
        
    def iniciar_ciclo(self, energia: float):
        promedioBateria = 0
        for dispo in self._dispositivos:
            promedioBateria += dispo._consumo_energia(energia)
        promedioBateria /= len(self._dispositivos)
        print(promedioBateria)
            
    def desvincular_dispositivo(self, name):
        if not self._dispositivos:
            print("La lista está vacia")
            return
        for d in self._dispositivos:
            if(d.name == name):
                self._dispositivos.remove(d)
                return
        print(f"Dispositivo {name} no encontrado")
            
    @property
    def dispositivos(self):
        return tuple(self._dispositivos)
        
    

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

CH01.iniciar_ciclo(45)