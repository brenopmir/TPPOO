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
    def VerificarDuplicado(self, nomedocomodo: str) -> bool:
        pass

#basicamente essa função deve ser chamada apos adicionar todos ou algum dispositivo pois ela que contabiliza a quantidade de dispositivos
    @abstractmethod
    def SalvarQuantidadeDeDispositivosComodo(self)-> None:
      pass
