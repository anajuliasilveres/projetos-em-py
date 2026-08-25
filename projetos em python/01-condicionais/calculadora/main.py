print("digite um número: ")
numero1 = float(input())

print("digite outro número: ")
numero2 = float(input())

print("Escolha a operação: ")
operação = input()

if operação == "+":
    resultado = numero1 + numero2
    print ("o resultado é ", f"{resultado:2.2f}") 

elif operação == "-":
    resultado = numero1 - numero2
    print ("o resultado é ", f"{resultado:2.2f}") 

elif operação == "*":
    resultado = numero1 * numero2
    print ("o resultado é ", f"{resultado:2.2f}")

elif operação == "/":
        resultado = numero1 / numero2
        print ("o resultado é ", f"{resultado:2.2f}") 

finally
