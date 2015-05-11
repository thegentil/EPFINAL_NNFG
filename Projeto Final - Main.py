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

#=============================================================================#
"""ORGANIZANDO OS NOMES, SOBRENOMES E LOGINS"""

dic_A = {}

for e in arquivo_limpo_A:
    dic_A[e[2]] =  [e[0], e[1]]

print('')
print(dic_A)


dic_B = {}

for e in arquivo_limpo_B:
    dic_B[e[2]] = [e[0], e[1]]

print('')        
print(dic_B)


dic_C = {}

for e in arquivo_limpo_C:
    dic_C[e[2]] = [e[0], e[1]]

print('')
print(dic_C)
#=============================================================================#
"""CRIANDO E RELACIONANDO O INPUT DO USUÁRIO DO PROGRAMA COM OS LOGINS LIDOS PELO PROGRAMA ACIMA"""

print('')
user = input('Seu nome de usuário INSPER:')

if user in dic_A:
    print('Bem Vindo ao INSPERBRAIN,\n'+dic_A[user][0])

elif user in dic_B:
    print('Bem Vindo ao INSPERBRAIN,\n'+dic_B[user][0])

elif user in dic_C:
    print('Bem Vindo ao INSPERBRAIN,\n'+dic_C[user][0])
