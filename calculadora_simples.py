#Calculadora simples em Python, iniciando o aprendizado na linguagem.
#Autor: Jefferson Martins, 20/08/2024

num1 = 0
num2 = 0
op = ""
resultado = 0

print("Olá, tudo bom? Por favor digite o primeiro numero da operação")

num1 = int(input())

print("Valor inserido:",num1)
print(" ")

print("Insira o segundo numero da operação")

num2 = int(input())

print("Valor inserido:",num2)
print(" ")

print("Insira agora o sinal da operação (+, -, *, /)")

op = input()

print("operacao escolhida:",op)
print(" ")

if op == "+":
    
    resultado = num1 + num2
    print("Resultado:",resultado) 

if op == "-":
    
    resultado = (num1-num2)
    print("Resultado:",resultado)  

if op == "*":
    
    resultado = (num1*num2)
    print("Resultado:",resultado)  

if op == "/":
    
    resultado = (num1/num2)
    print("Resultado:",resultado)  

