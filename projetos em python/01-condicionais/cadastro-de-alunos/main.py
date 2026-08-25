
print (" Cadastro de Alunos ")

print("Digite o nome completo do aluno: ")
nome = input()

print("Digite a data de nascimento do aluno: ")
data_de_nascimento = input()

print("digite o CPF do aluno ")
Cpf = input() 

print("digite o numero do aluno (ou responsavel legal)")
numero=input()

import random

matricula = random.randint(10000000, 99999999)

print(
      f"Cadastro realizado.\n"
      f"o nome do aluno(A) é: {nome}\n"
      f"o numero da matricula é: {matricula}\n"
      f"a data de nacimento é: {data_de_nascimento}\n"
      f"o CPF do aluno é: {Cpf}\n"
      f"o telefone de contato é: {numero}"
)

finally
