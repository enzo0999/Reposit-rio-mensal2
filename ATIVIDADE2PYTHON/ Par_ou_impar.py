def verificar_paridade(valor):
    try:
        numero = int(valor)
        return numero % 2 == 0   #Retorna True se for par, False se for ímpar
    except ValueError:
        return "Valor informado é inválido. Por favor, informe um número inteiro."
valor_informado = input("Digite um número: ")
resultado = verificar_paridade(valor_informado)
print(resultado)
