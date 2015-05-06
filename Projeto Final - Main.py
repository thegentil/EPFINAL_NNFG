# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:30:22 2015

@author: Nicolas Gentil, Nicolas Fonteyne, Gabriel Olanda e Felipe Giardini

Projeto Final - Mapa virtual

"""

Arquivo_Nomes_A = open("Turma_A_Nomes.txt", encoding="utf-8")
Arquivo_Usuários_A = open("Turma_A_Usuários.txt", encoding="utf-8")

Arquivo_Nomes_B = open("Turma_B_Nomes.txt", encoding="utf-8")
Arquivo_Usuários_B = open("Turma_B_Usuários.txt", encoding="utf-8")

Nomes_A = Arquivo_Nomes_A.readlines()
Usuários_A = Arquivo_Usuários_A.readlines()
Nomes_B = Arquivo_Nomes_B.readlines()
Usuários_B = Arquivo_Usuários_B.readlines()

print(Nomes_A)
print("")
print(Usuários_A)
print("")
print(Nomes_B)
print("")
print(Usuários_B)

Limpa_Nomes_A = []

for p in Nomes_A[1:]:
    n = p.strip()
    
    if n != " ":
        Limpa_Nomes_A.append(n)
        
print(Limpa_Nomes_A)        
        
Limpa_Usuários_A = []

for p in Usuários_A[1:]:
    n = p.strip()
    
    if n != " ":
        Limpa_Usuários_A.append(n)   
        
print(Limpa_Usuários_A)          
        
        
    

