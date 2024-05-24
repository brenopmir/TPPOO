from abc import ABC,abstractmethod

class Janela(ABC):
   
    @abstractmethod
    def Abertura(self)->int:
        pass

    @abstractmethod
    
    def SetAbertura(self,abertura:int)->None:
        pass
    
   
    @abstractmethod
    def Tranca(self)->bool:
        pass

    @abstractmethod
    def SetTranca(self,tranca:bool)->None:
        pass  