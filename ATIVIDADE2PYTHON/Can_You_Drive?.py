def classificar_idade():
    idade = input("Digite sua idade: ")

    if not idade.isdigit():  # Verifica se a entrada é numérica
        print("Valor informado é inválido.")
        return

    idade = int(idade)

    if idade < 0:
        print("Valor informado é inválido.")
    elif idade < 18:
        print("Você é menor de idade.")
    elif idade <= 59:
        print("Você é adulto.")
    else:
        print("Você é idoso.")

classificar_idade()