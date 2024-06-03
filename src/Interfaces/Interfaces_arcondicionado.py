from abc import ABC,abstractmethod

class InterfaceAr_Condicionado(ABC):
   
    @abstractmethod
    def Ligado(self)->bool:
        pass

    @abstractmethod
    def SetLigado(self,ligarnovo:bool)->None:
        pass

    @abstractmethod
    def Temperatura(self)->int:
        pass 
    
    @abstractmethod
    def SetTemperatura(self,temperaturanova:int)->None:
        pass

    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidadenova:int)->None:
        pass  