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
    
del arquivo_limpo_A[0]      #deletando os primeiros elementos das matrizes arquivo_limpo_A & B que eram desprezíveis
del arquivo_limpo_B[0]

#=============================================================================#
"""ORGANIZANDO OS NOMES, SOBRENOMES E LOGINS"""

dic_A = {}

for e in arquivo_limpo_A:
    dic_A[e[0]+ ' '+e[1]] =  e[2]
        
print(dic_A)


dic_B = {}

for e in arquivo_limpo_B:
    dic_B[e[0]+ ' '+e[1]] = e[2]

print('')        
print(dic_B)
        
