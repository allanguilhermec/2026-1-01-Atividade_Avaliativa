num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

produto = num1*num2*num3*num4
print(f"O produto dos 4 números é: {produto}")
if produto <  0: 
    print("O produto não é positivo.")
else:
    print("O produto é positivo.")