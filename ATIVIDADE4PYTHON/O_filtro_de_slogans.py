produto = input("Digite o nome do produto: ")
slogan = input("Digite o slogan: ")
palavra_chave = input("Digite a palavra-chave: ")
#Verificação se a palavra chave está no slogan:
if palavra_chave in slogan:
    print(f"Slogan adequado (palavra-chave {palavra_chave} está no slogan).")
else:
    print(f"Slogan inadequado (palavra-chave {palavra_chave} não está no slogan).")
#verificando se o número de letras na palavra chave está entre 7 e 10:
#if=adequdo
num_palavras = len(slogan.split())
if num_palavras >= 7 and num_palavras <= 10:
    print("Slogan adequado (número de palavras).")
#else=inadequado
else:
    print("Slogan inadequado (número de palavras).")
#Verificando se  a palavraa chave inicia e termina com letras:
if slogan[0].isalpha() and slogan[-1].isalpha():
    print("Slogan adequado (início/fim com letra).")
else:
    print("Slogan inadequado (início/fim com letra).")
#Aqui para finalizar o código está verificando se todos os requisitos do slogan e da palavra chave estão certo adequados (if) ou inadequados (else)
if (palavra_chave in slogan and
    num_palavras >= 7 and num_palavras <= 10 and
    slogan[0].isalpha() and slogan[-1].isalpha()):
    print(f'O slogan "{slogan}" cumpre os requisitos de slogan para o produto "{produto}".')
