nota_A = float(input("Digite a primeira nota: "))
nota_B = float(input("Digite a segunda nota: "))

mediafinal = (nota_A + nota_B) / 2

if(mediafinal >= 7):
    print("Aprovado com média: %.1f" % mediafinal)
else:
    print("Reprovado com média: %.1f" % mediafinal)