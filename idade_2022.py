print("Insira eu Nome Completo")
nome = input()
cont = True
while(cont):
    print("Insira o seu ano de Nascimento")
    try:
        ano = int(input())
        if(ano < 1922) or (ano > 2021):
            print("Data invalida")
        else:
            idade = 2022 - ano
            print("Seu nome é "+ nome)
            print("Sua idade é: ", idade)
            cont = False
    except:
        print("Dado informado está incorreto!")