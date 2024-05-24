from abc import ABC, abstractmethod

class Dispositivo(ABC):
   
    @abstractmethod
    def Nome(self) -> str:
        pass

    @abstractmethod
    def SetNome(self, nome: str) -> None:
        pass