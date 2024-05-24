from abc import ABC,abstractmethod

class Lampadas(ABC):
   
    @abstractmethod
    def Cor(self)->str:
        pass

    @abstractmethod
    
    def SetCor(self,cor:str)->None:
        pass
    
    @abstractmethod
    def ListarCores(self)->None:
        pass

    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidade:int)->None:
        pass  