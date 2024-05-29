from abc import ABC,abstractmethod

class InterfaceLampadas(ABC):
   
    @abstractmethod
    def Cor(self)->str:
        pass

#PRECONDIÇÃO: Devem ser inseridas somente cores válidas, como amarelo,vermelho, azul,branco,laranja,verde ou roxo
    @abstractmethod
    def SetCor(self,cornova:str)->None:
        pass
    
    @abstractmethod
    def Intensidade(self)->int:
        pass 

    @abstractmethod
    def SetIntensidade(self,intensidadenova:int)->None:
        pass  