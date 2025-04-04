import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida o CPF com base nas regras brasileiras:
      - Deve conter 11 dígitos (após remoção de formatação);
      - Não pode ser composto por dígitos repetidos;
      - Os dígitos verificadores são calculados conforme o algoritmo padrão.
    """
    # Remove qualquer caractere não numérico
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex.: "11111111111")
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = (soma * 10) % 11
    d1 = d1 if d1 < 10 else 0
    if d1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = (soma * 10) % 11
    d2 = d2 if d2 < 10 else 0
    if d2 != int(cpf[10]):
        return False

    return True 