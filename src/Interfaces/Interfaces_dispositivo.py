from abc import ABC, abstractmethod

class InterfaceDispositivo(ABC):
   
    @abstractmethod
    def Nome(self) -> str:
        pass

    @abstractmethod
    def SetNome(self, nomenovo: str) -> None:
        pass

    @abstractmethod
    def SalvarDispositivo(self,nomearquivo:str)->None:
        pass