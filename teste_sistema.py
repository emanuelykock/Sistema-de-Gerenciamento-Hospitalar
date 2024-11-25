import unittest
from paciente import Paciente  # Importando a classe Paciente (ajuste o caminho conforme necessário)
from enfermeiro import Enfermeiro  # Se você precisar de enfermeiros nos testes

class TestPaciente(unittest.TestCase):
    
    def test_inicializacao_paciente(self):
        # Criando um enfermeiro fictício para atribuir ao paciente
        enfermeiro = Enfermeiro("João", 30, "123456", "Emergência")
        paciente = Paciente("Maria", 45, "Gripe", "Internado", enfermeiro)
        
        # Testando se a inicialização do paciente foi correta
        self.assertEqual(paciente.getNome(), "Maria")
        self.assertEqual(paciente.getIdade(), 45)
        self.assertEqual(paciente.getEnfermidade(), "Gripe")
        self.assertEqual(paciente.getStatus(), "Internado")
        self.assertEqual(paciente.getEnfermeiroResponsavel().getNome(), "João")

    def test_status_paciente(self):
        # Criando um paciente com status "Alta"
        paciente = Paciente("Carlos", 50, "Pneumonia", "Alta", None)
        self.assertEqual(paciente.getStatus(), "Alta")

if __name__ == "__main__":
    unittest.main()
