# -*- coding: utf-8 -*-

from __future__ import print_function, division
import codecs

__author__ = 'nicolasfonteyne'

#======================================================================================================================#

from Classes_dos_objetos import *
from Dic_turmas import *

#======================================================================================================================#


# CRIANDO OS OBJETOS DOS ALUNOS:

lista_dos_dics = [dic_A, dic_B, dic_C]

alunos = []


for dic in lista_dos_dics:          # adicionando os objetos criados `as listas

    for u in dic:

        if dic == dic_A:
            u = Aluno(dic_A[u][0]+' '+dic_A[u][1], u, Turma("A", "401"))
            alunos.append(u)

        elif dic == dic_B:
            u = Aluno(dic_B[u][0]+' '+dic_B[u][1], u, Turma("B", "402"))
            alunos.append(u)

        elif dic == dic_C:
            u = Aluno(dic_C[u][0]+' '+dic_C[u][1], u, Turma("C", "403"))
            alunos.append(u)

        else:
            pass


# CRIANDO OS OBJETOS DAS TURMAS:


materias = []       # criando a lista de materias

for p in dic_profs:         #limpando as materias excedentes da lista
    materias.append(dic_profs[p])

for m in materias:
    n = materias.count(m)

    if n > 1:

        for i in range(n-1):
            materias.remove(m)


alunos_A = []
alunos_B = []
alunos_C = []

for a in alunos:

    if a.turma.nome == "A":

        alunos_A.append(a)

    elif a.turma.nome == "B":

        alunos_B.append(a)

    elif a.turma.nome == "C":

        alunos_C.append(a)

    else:
        pass


