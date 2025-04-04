from validador_cpf import validar_cpf

def main():
    print("=== Validador de CPF ===")
    
    while True:
        cpf = input("\nDigite um CPF para validar (ou 'sair' para encerrar): ")
        
        if cpf.lower() == 'sair':
            break
            
        resultado = validar_cpf(cpf)
        
        if resultado:
            print(f"O CPF {cpf} é VÁLIDO.")
        else:
            print(f"O CPF {cpf} é INVÁLIDO.")
    
    print("\nPrograma encerrado.")

if __name__ == "__main__":
    main() 