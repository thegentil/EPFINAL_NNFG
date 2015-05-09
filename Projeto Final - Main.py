
#=============================================================================#
""" ABRINDO OS ARQUIVOS E LIMPANDO-OS"""

arquivo_A = open("turma_A.csv")
arquivo_A = arquivo_A.readlines()

arquivo_limpo_A = []
for e in arquivo_A:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_A.append(n)

arquivo_B = open("turma_B.csv")
arquivo_B = arquivo_B.readlines()

arquivo_limpo_B = []
for e in arquivo_B:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_B.append(n)

#=============================================================================#
"""ORGANIZANDO OS NOMES, SOBRENOMES E LOGINS"""

dic_A = {}
dic_B = {}

for e in arquivo_limpo_A:
    dic_A[e[0]] = [e[1], e[2]]
        
print(dic_A)

for e in arquivo_limpo_B:
    dic_B[e[0]] = [e[1], e[2]]

print('')        
print(dic_B)
        
