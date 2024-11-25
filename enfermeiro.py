from pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, nome, idade, coren, setor):
        super().__init__(nome, idade)
        self.__coren = coren
        self.__setor = setor

    def getCoren(self):
        return self.__coren

    def setCoren(self, coren):
        self.__coren = coren

    def getSetor(self):
        return self.__setor

    def setSetor(self, setor):
        self.__setor = setor

    def mostrar(self):
        return f"Enfermeiro: {self.getNome()}, Idade: {self.getIdade()}, COREN: {self.getCoren()}, Setor: {self.getSetor()}"
