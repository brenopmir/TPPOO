from abc import ABC,abstractmethod

class InterfaceCasa(ABC):
   
    @abstractmethod
    def Nome(self)->str:
        pass

    @abstractmethod
    def SetNome(self,nomenovo:str)->None:
        pass
   
    @abstractmethod
    def AdicionarComodo(self,comodonovo:str)->None:
        pass

    @abstractmethod
    def RemoverComodo(self,comodo:str)->None:
        pass

    @abstractmethod
    def ListarComodo(self)->None:
        pass 
    
    @abstractmethod
    def AtivarModos(self,modo:str)->None:
        pass
