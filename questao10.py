num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

media = (num1+num2+num3+num4)/4
print(f"A média é: {media}")
      
if media >= 6:
    print("Situação: Aprovado(a)!")
else:
    print("Situação: Reprovado(a)")
