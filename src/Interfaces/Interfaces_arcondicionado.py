from abc import ABC,abstractmethod

class Ar_Condicionado(ABC):
   
    @abstractmethod
    def Ligado(self)->bool:
        pass

    @abstractmethod
    
    def SetLigado(self,Ligar:bool)->None:
        pass
    
   
    @abstractmethod
    def Modo(self)->str:
        pass

    @abstractmethod
    def SetModo(self,modo:str)->None:
        pass
    
   
    @abstractmethod
    def Temperatura(self)->int:
        pass 
    
    @abstractmethod
    def SetTemperatura(self,temperatura:int)->None:
        pass

    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidade:int)->None:
        pass  