num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media = (num1+num2+num3+num4)/4
menor = min(num1, num2, num3, num4)
maior = max(num1, num2, num3, num4)
diferença = maior - menor

print(f"A média aritmética é: {media}")
print(f"A diferença entre o maior e o menor valor é: {diferença}")