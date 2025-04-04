import unittest
from validador_cpf import validar_cpf

class TestValidarCPF(unittest.TestCase):

    def test_valid_cpf(self):
        cpfs_validos = [
            "529.982.247-25",  # CPF conhecido como válido
            "12345678909",     # Outro exemplo válido
        ]
        for cpf in cpfs_validos:
            with self.subTest(cpf=cpf):
                self.assertTrue(validar_cpf(cpf), f"CPF {cpf} deveria ser válido")

    def test_invalid_cpf(self):
        cpfs_invalidos = [
            "111.111.111-11",  # Dígitos repetidos
            "123.456.789-00",  # Dígitos verificadores inválidos
            "52998224724",     # CPF com dígitos verificadores incorretos
            "5299822472",      # CPF com quantidade insuficiente de dígitos
            "529982247252",    # CPF com quantidade excessiva de dígitos
        ]
        for cpf in cpfs_invalidos:
            with self.subTest(cpf=cpf):
                self.assertFalse(validar_cpf(cpf), f"CPF {cpf} deveria ser inválido")

if __name__ == '__main__':
    unittest.main() 