from abc import ABC,abstractmethod

class InterfaceCortinas(ABC):
   
    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidadenova:int)->None:
        pass  