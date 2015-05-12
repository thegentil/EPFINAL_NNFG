""" Exercício-Programa Final

autors: Nícolas Fonteyne, Gabriel Olanda, Felipe Giardini e Nícolas Gentil

Descrição breve: desenvolvimento do aplicativo  INSPERBRAIN
"""



#=============================================================================#
""" ABRINDO OS ARQUIVOS E LIMPANDO-OS"""

arquivo_A = open("turma_A.csv")
arquivo_A = arquivo_A.readlines()

arquivo_limpo_A = []        #limpando o arquivo_A e dando split pelo ponto e vírgula para assim formar uma matriz,
for e in arquivo_A:         #em que cada um dos elementos é uma lista com o primeiro nome da pessoa, seus sobrenomes e o usuário
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_A.append(n)


arquivo_B = open("turma_B.csv")
arquivo_B = arquivo_B.readlines()

arquivo_limpo_B = []        #mesmo para o arquivo_B
for e in arquivo_B:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_B.append(n)


arquivo_C = open("turma_C.csv")
arquivo_C = arquivo_C.readlines()

arquivo_limpo_C = []        #mesmo para arquivo_C
for e in arquivo_C:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_C.append(n)


del arquivo_limpo_A[0]      #deletando os primeiros elementos das matrizes arquivo_limpo_A & B que eram desprezíveis
del arquivo_limpo_B[0]
del arquivo_limpo_C[0]

#======================================================================================================================#
"""ORGANIZANDO OS NOMES, SOBRENOMES E LOGINS"""

dic_A = {}

for e in arquivo_limpo_A:           #adicionando os elementos do arquivo_limpo_A ao dic_A, sendo a chave o login
    dic_A[e[2]] = [e[0], e[1]]      #e os valores o primeiro nome e os sobrenomes do usuário


dic_B = {}

for e in arquivo_limpo_B:           #mesmo para o dic_B
    dic_B[e[2]] = [e[0], e[1]]


dic_C = {}

for e in arquivo_limpo_C:           #mesmo para o dic_C
    dic_C[e[2]] = [e[0], e[1]]

#======================================================================================================================#

def revisão():          #caso precise printar os dics
    print('')
    print(dic_A)
    print('')
    print(dic_B)
    print('')
    print(dic_C)

#revisão()

#======================================================================================================================#
"""CRIANDO E RELACIONANDO O INPUT DO USUÁRIO DO PROGRAMA COM OS LOGINS LIDOS PELO PROGRAMA ACIMA"""

def user_verification():            #func de verificação do usuário

    tentativas = 0                  #criando a variável que conta quantas vezes o user errou o login

    while True:

        repetir = False             #criando a variável que diz se vai repetir ou não

        print('')
        user = input('Seu login INSPER: ')

        if user in dic_A:
            print('Bem Vindo ao INSPERBRAIN,\n'+dic_A[user][0])     #dando resposta ao input do usuário

        elif user in dic_B:
            print('Bem Vindo ao INSPERBRAIN,\n'+dic_B[user][0])

        elif user in dic_C:
            print('Bem Vindo ao INSPERBRAIN,\n'+dic_C[user][0])

        else:
            print('USUÁRIO INVÁLIDO')
            tentativas += 1             #soma um no núemro de tentativas do user de logar
            repetir = True              #faz com que o processo se repita


        if repetir == False:        #faz com que o processo pare de se repetir caso o usuário acerte o login
            break


        if tentativas >= 3:         #DAQUI PRA BAIXO É O MODO DE "ESQUECEU SEU LOGIN"
            print('')
            r = input('Esqueceu seu login? ')

            if r == 'sim' or 's' or 'Sim' or 'SIM' or 'S':
                print('')
                r2 = input('Digite seu nome completo por favor: ')
                name_in_dic = 0
                tentativas = 0

                for vA in dic_A:
                    if r2.upper() == str(dic_A[vA][0] + ' ' + dic_A[vA][1]):
                        break
                        print('Bem Vindo ao INSPERBRAIN,\n'+dic_A[vA][0])
                        name_in_dic += 1

                for vB in dic_B:
                    if r2.upper() == str(dic_B[vB][0] + ' ' + dic_B[vB][1]):
                        break
                        print('Bem Vindo ao INSPERBRAIN,\n'+dic_B[vB][0])
                        name_in_dic += 1

                for vC in dic_C:
                    if r2.upper() == str(dic_C[vC][0] + ' ' + dic_C[vC][1]):
                        break
                        print('Bem Vindo ao INSPERBRAIN,\n'+dic_C[vC][0])
                        name_in_dic += 1

                if name_in_dic == 0:
                    print('Desculpe, mas seu nome não consta no cadastro')

user_verification()

#======================================================================================================================#
