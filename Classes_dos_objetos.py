# -*- coding: utf-8 -*-

""" Exercício-Programa Final

autors: Nícolas Fonteyne, Gabriel Olanda, Felipe Giardini e Nícolas Gentil

Descrição breve: desenvolvimento do aplicativo  INSPERBRAIN
"""

from __future__ import print_function, division
import codecs

#======================================================================================================================#
""" CRIANDO AS CLASSES A SEREM UTILIZADAS NA TELA_PROFESSORES """

class Aluno:

    def __init__(self, nome, usuario, turma):
        self.nome = nome
        self.usuario = usuario
        self.turma = turma


class Turma:

    def __init__(self, nome, materias, sala):
        self.nome = nome
        self.materias = materias
        self.sala = sala


class Materia:

    def __init__(self, turma, horarios):
        self.turma = turma
        self.horario = horarios


class Professor:

    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia