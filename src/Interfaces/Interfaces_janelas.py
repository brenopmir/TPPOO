from abc import ABC,abstractmethod

class InterfaceJanela(ABC):
   
    @abstractmethod
    def Abertura(self)->int:
        pass

    @abstractmethod
    def SetAbertura(self,aberturanova:int)->None:
        pass
    
   
    @abstractmethod
    def Tranca(self)->bool:
        pass

    @abstractmethod
    def SetTranca(self,trancanova:bool)->None:
        pass  