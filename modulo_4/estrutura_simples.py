A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))

if(A > B):
    aux = A
    A = B
    B = aux

print("O valor de A agora é:", A)
print("O valor de B agora é:", B)