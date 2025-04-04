# Validador de CPF

- O número de dígitos (11 após remoção de formatação)
- Verificação de dígitos repetidos
- Cálculo dos dígitos verificadores

## Arquivos do Projeto

- `validador_cpf.py`: Contém a função principal de validação
- `teste_cpf.py`: Testes unitários para a função de validação
- `main.py`: Interface simples para uso do validador

## Como Executar

### Validação de CPF via Interface de Linha de Comando

```bash
python main.py
```

### Executar Testes Unitários

```bash
python teste_cpf.py
```

## Regras de Validação

O validador segue as seguintes regras:

1. O CPF deve ter 11 dígitos (caracteres de formatação como ponto e hífen são removidos)
2. O CPF não pode ser composto apenas por dígitos repetidos (ex: 111.111.111-11)
3. Os dígitos verificadores são calculados e validados de acordo com o algoritmo padrão para CPFs brasileiros 