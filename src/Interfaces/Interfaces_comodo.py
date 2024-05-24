from abc import ABC,abstractmethod

class Comodo(ABC):
   
    @abstractmethod
    def Nome(self)->str:
        pass

    @abstractmethod
    
    def SetNome(self,nome:str)->None:
        pass
    # Cria um  dispositivo de um tipo, sendo Lampada,Cortina,Arcondicionado,Camera de segurança e Janela, 1,2,3,4 e 5 respectivamente e com o nome que o usuario escolher
    @abstractmethod
    def AdicionarDispositivo(self,tipo:int,nome:str)->None:
        pass

    # remove o dispositivo de um tipo, sendo Lampada,Cortina,Arcondicionado,Camera de segurança e Janela, 1,2,3,4 e 5 respectivamente, que possui determinado nome 
    @abstractmethod
    def RemoverDispositivo(self,tipo:int,nome:str)->None:
        pass

    # Lista todos os dispositivos de um tipo, sendo Lampada,Cortina,Arcondicionado,Camera de segurança e Janela, 1,2,3,4 e 5 respectivamente
    @abstractmethod
    def ListarDispositivos(self)->None:
        pass 
    
    @abstractmethod
    def ConfigurarTodos(self,tipo:int,nome:str)->None:
        pass

   