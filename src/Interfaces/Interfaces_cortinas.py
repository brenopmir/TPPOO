from abc import ABC,abstractmethod

class Cortinas(ABC):
   
    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidade:int)->None:
        pass  