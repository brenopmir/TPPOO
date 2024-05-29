from ..Interfaces.Interfaces_dispositivo import InterfaceDispositivo
from abc import ABC,abstractmethod

class Dispositivo(ABC,InterfaceDispositivo):
    def __init__(self,nome:str)->None:
        self.__nome=nome

    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo
        
    @abstractmethod
    def SalvarDispositivo(self, nomearquivo: str) -> None:
        pass
