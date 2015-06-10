# -*- coding: utf-8 -*-

""" Exercício-Programa Final

autors: Nícolas Fonteyne, Gabriel Olanda, Felipe Giardini e Nícolas Gentil

Descrição breve: desenvolvimento do aplicativo  INSPERBRAIN
"""

from __future__ import print_function, division
import codecs

#======================================================================================================================#
""" CRIANDO AS CLASSES A SEREM UTILIZADAS """

class Aluno:

    def __init__(self, nome, usuario, turma):
        self.nome = nome
        self.usuario = usuario
        self.turma = turma


class Turma:

    def __init__(self, nome, sala):
        self.nome = nome
        self.sala = sala
        self.alunos = []
        self.professores = []

    def adiciona_aluno(self, aluno):
        self.alunos.append(aluno)

    def adiciona_professor(self, professor):
        self.professores.append(professor)


class Professor:

    def __init__(self, nome, materia, turmas):
        self.nome = nome
        self.materia = materia
        self.turmas = turmas

    def adiciona_sala(self, sala):
        self.salas.append(sala)
