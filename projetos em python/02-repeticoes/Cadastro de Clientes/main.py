print("bem vindo ao cadastro de clientes,gostaria de cadastrar um cliente?")
if input().lower() == 'sim':
    print("Ótimo! Vamos começar o cadastro.")
else:
    print("Tudo bem! Até a próxima. obrigada por utilizar nosso sistema.")
    exit()

while True:
    nome = input("\ndigite o nome do(a) cliente: ")
    Nascimento = input("digite a data de nascimento do(a) cliente: ")
    cpf = input("digite o cpf do(a) cliente: ")
    endereço = input("digite o endereço do(a) cliente: ")
    Telefone = input("digite o telefone do(a) cliente: ")

    print("\nCadastro realizado com sucesso!, deseja cadastrar outro cliente?")
    resposta = input().lower()
    
    if resposta == 'sim' or resposta == 'SIM' or resposta == 'Sim':
        continue
    elif resposta == 'não' or resposta == 'NAO' or resposta == 'NÃO' or resposta == 'nao' or resposta == 'Nao' or resposta == 'Não':
        print("Tudo bem! Até a próxima.") 
        break;

print("\ngosteria de ver os dados dos clientes cadastrados?")
if input().lower() == 'sim':
     
     print("\nde qual cliente você gostaria de ver os dados?")
     cliente = input("\ndigite o nome do cliente: ")
     nome = cliente

     print(f"Nome: {nome}")
     print(f"Data de nascimento: {Nascimento}")
     print(f"CPF: {cpf}")
     print(f"Endereço: {endereço}")
     print(f"Telefone: {Telefone}")

if input().lower() == 'não' or input().lower() == 'NAO' or input().lower() == 'NÃO' or input().lower() == 'nao' or input().lower() == 'Nao' or input().lower() == 'Não':
    print("Tudo bem! Até a próxima. obrigada por utilizar nosso sistema.")
    exit()

