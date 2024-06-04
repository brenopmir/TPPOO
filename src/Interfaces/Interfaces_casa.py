from abc import ABC,abstractmethod

class InterfaceCasa(ABC):
   
    @abstractmethod
    def Nome(self)->str:
        pass

    @abstractmethod
    def SetNome(self,nomenovo:str)->None:
        pass
   
    @abstractmethod
    def AdicionarComodo(self,nomedocomodo:str)->None:
        pass

    @abstractmethod
    def RemoverComodo(self,nomedocomodo:str)->None:
        pass

    @abstractmethod
    def ListarComodos(self)->None:
        pass

    @abstractmethod
    def VerificarDuplicado(self, nomedocomodo: str) -> bool:
        pass

    @abstractmethod
    def SalvarComodo(self)->None:
        pass 
