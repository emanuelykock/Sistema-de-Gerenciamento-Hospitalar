from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, enfermidade, status, enfermeiro_responsavel = None):
        super().__init__(nome, idade)
        self.__enfermidade = enfermidade
        self.__status = status
        self.__enfermeiro_responsavel = enfermeiro_responsavel

    def getEnfermidade(self):
        return self.__enfermidade
    def getStatus(self):
        return self.__status
    def getEnfermeiroResponsavel(self):
        return self.__enfermeiro_responsavel

    def setenfermidade(self, enfermidade):
        self.__enfermidade = enfermidade
    def setStatus(self, status):
        self.__status = status
    def setEnfermeiroResponsavel(self, enfermeiro):
        self.__enfermeiro_responsavel = enfermeiro

    def mostrar(self):
        enfermeiro = self.getEnfermeiroResponsavel()
        return f"Paciente: {self.getNome()}, Idade: {self.getIdade()}, Enfermidade: {self.getEnfermidade()}, Status: {self.getStatus()}, Enfermeiro Responsável: {enfermeiro.getNome() if enfermeiro else 'N/A'}"