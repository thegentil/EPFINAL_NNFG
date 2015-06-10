# -*- coding: utf-8 -*-

""" Exercício-Programa Final

autors: Nícolas Fonteyne, Gabriel Olanda, Felipe Giardini e Nícolas Gentil

Descrição breve: desenvolvimento do aplicativo  INSPERBRAIN
"""

from __future__ import print_function, division
import codecs

#======================================================================================================================#
""" ABRINDO OS ARQUIVOS E LIMPANDO-OS """

#ABRINDO OS ARQUIVOS:

arquivo_A = codecs.open("turma_A.csv", encoding='latin1')
linhas_arquivo_A = arquivo_A.readlines()


arquivo_B = codecs.open("turma_B.csv", encoding='latin1')
linhas_arquivo_B = arquivo_B.readlines()


arquivo_C = codecs.open("turma_C.csv", encoding='latin1')
linhas_arquivo_C = arquivo_C.readlines()


#LIMPANDO OS ARQUIVOS:

arquivo_limpo_A = []        #limpando o arquivo_A e dando split pelo ponto e virgula para assim formar uma matriz,
for e in linhas_arquivo_A:         #em que cada um dos elementos eh uma lista com o primeiro nome da pessoa, seus sobrenomes e o usuario
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_A.append(n)


arquivo_limpo_B = []        #mesmo para o arquivo_B
for e in linhas_arquivo_B:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_B.append(n)


arquivo_limpo_C = []        #mesmo para arquivo_C
for e in linhas_arquivo_C:
    n = e.strip()
    n = n.split(';')
    arquivo_limpo_C.append(n)


del arquivo_limpo_A[0]      #deletando os primeiros elementos das matrizes arquivo_limpo_A & B que eram despreziveis
del arquivo_limpo_B[0]
del arquivo_limpo_C[0]


#CRIANDO OS DICIONARIOS:

dic_A = {}

for e in arquivo_limpo_A:           #adicionando os elementos do arquivo_limpo_A ao dic_A, sendo a chave o login
    dic_A[e[2]] = [e[0], e[1]]      #e os valores o primeiro nome e os sobrenomes do usuario


dic_B = {}

for e in arquivo_limpo_B:           #mesmo para o dic_B
    dic_B[e[2]] = [e[0], e[1]]


dic_C = {}

for e in arquivo_limpo_C:           #mesmo para o dic_C
    dic_C[e[2]] = [e[0], e[1]]


dic_profs = {"FABIO ORFALI": ["MODELAGEM E SIMULACAO DO MUNOD FISICO", ['A']],
             "FREDERICO AUGUSTO ALEM BARBIERI": ["INSTRUMENTACAO E MEDICAO", ['A', 'B']],
             "HELOISA MARIA DOMINGUES NEVES": ["A NATUREZA DO DESIGN", ['A', 'C']],
             "VINICIUS LICKS": ["GRANDES DESAFIOS DA ENGENHARIA", ['A', 'B', 'C']],
             "FABIO ROBERTO DE MIRANDA": ["DESIGN DE SOFTWARE", ['A', 'B']],
             "LEONIDAS SANDOVAL JUNIOR": ["A NATUREZA DO DESIGN", ['B']],
             "PAULINA ACHURRA": ["MODELAGEM E SIMULACAO DO MUNOD FISICO", ['B']],
             "LUCIANO PEREIRA SOARES": ["DESIGN DE SOFTWARE", ['C']],
             "FERNANDO MOYA ORSATTI": ["MODELAGEM E SIMULACAO DO MUNOD FISICO", ['C']],
             "MAURICIO SILVA FERREIRA": ["INSTRUMENTACAO E MEDICAO", ['C']]}

dicionarios = [dic_A, dic_B, dic_C]

for e in dicionarios:
    print(e)
    print('')
