# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter

import time
import random

from Dic_turmas import *
from Classes_dos_objetos import *

#======================================================================================================================#

#CRIANDO A LISTA DOS PROFESSORES:

professores = []
for p in dic_profs:
    p = Professor(p, dic_profs[p][0], dic_profs[p][1])
    professores.append(p)

#======================================================================================================================#

#CRIANDO AS TURMAS:

    #CRIANDO A TURMA A:

turma_A = Turma('A', 401)
for u in dic_A:
    turma_A.adiciona_aluno(dic_A[u][0] + ' ' + dic_A[u][1])

for p in professores:
    if 'A' in p.turmas:
        turma_A.adiciona_professor(p)

    #CRIANDO A TURMA B:

turma_B = Turma('B', 402)
for u in dic_B:
    turma_B.adiciona_professor(dic_B[u][0] + ' ' + dic_B[u][1])

for p in professores:
    if 'B' in p.turmas:
        turma_B.adiciona_professor(p)

    #CRIANDO A TURMA C:

turma_C = Turma('C', 403)
for u in dic_C:
    turma_C.adiciona_professor(dic_C[u][0] + ' ' + dic_C[u][1])

for p in professores:
    if 'C' in p.turmas:
        turma_C.adiciona_professor(p)

#======================================================================================================================#

#CRIANDO O USUARIO:

aluno = None    # armazena os dados do usuario

#======================================================================================================================#

#CLASSES QUE DETERMINAM TELAS


class Usuario(Screen):
    pass

class Bem_Vindo(Screen):
    pass

class Mapa(Screen):
    pass

class Calendario(Screen):
    pass

class Professores(Screen):
    pass


class Heloisa(Screen):
    pass

class Leonidas(Screen):
    pass

class Mauricio (Screen):
    pass

class FabioO (Screen):
    pass

class Paulina (Screen):
    pass

class Fernando (Screen):
    pass

class FabioM (Screen):
    pass

class Luciano (Screen):
    pass

class Vinicius (Screen):
    pass

class Lourenco (Screen):
    pass


class Sair(Screen):
    pass


class Segunda(Screen):
    pass

class Terca(Screen):
    pass

class Quarta(Screen):
    pass

class Quinta(Screen):
    pass

class Sexta(Screen):
    pass


#======================================================================================================================#

#CLASSE QUE COORDENA AS TELAS:

class MyScreenManager(ScreenManager):


#CRIANDO AS VARIAVEIS A SEREM USADAS:

    user_input = None
    status = None
    imagem_segunda = None
    imagem_terca = None
    imagem_quarta = None
    imagem_quinta = None
    imagem_sexta = None
    user_screen_grid_layout = None
    button_go = None
    bem_vindo_label = None
    select_color = [0,0.9,1,1]

    def variaveis(self):

        global user_input
        global status
        global imagem_segunda
        global imagem_terca
        global imagem_quarta
        global imagem_quinta
        global imagem_sexta
        global user_screen_grid_layout
        global button_go
        global bem_vindo_label


        #TELA USUARIO:

        user_input = self.screens[0].ids["text_input"]
        status = self.screens[0].ids["status_label"]
        button_go = self.screens[0].ids["button_go"]
        user_screen_grid_layout = self.screens[0].ids["grid_layout_user_screen"]


        #TELA BEM_VINDO:

        bem_vindo_label = self.screens[1].ids["bem_vindo_label"]


        #TELA CALENDARIO:

        imagem_segunda = self.screens[5].ids["image_segunda"]
        imagem_terca = self.screens[6].ids["image_terca"]
        imagem_quarta = self.screens[7].ids["image_quarta"]
        imagem_quinta = self.screens[8].ids["image_quinta"]
        imagem_sexta = self.screens[9].ids["image_sexta"]

#CRIANDO A FUNCAO QUE CHECA SE O USUARIO DIGITADO EXISTE:

    def checa_usuario(self):

        text_user_input = user_input.text.lower()

        if text_user_input in dic_A:

            global aluno

            nome = dic_A[text_user_input]

            aluno = Aluno(nome, text_user_input, turma_A)

            root_widget.current = 'Segunda'

        elif text_user_input in dic_B:

            global aluno

            nome = dic_B[text_user_input]

            aluno = Aluno(nome, text_user_input, turma_B)

            root_widget.current = 'Segunda'

        elif text_user_input in dic_C:

            global aluno

            nome = dic_C[text_user_input]

            aluno = Aluno(nome, text_user_input, turma_C)

            root_widget.current = 'Segunda'

        else:

            status.text = u"Usuário Inválido"
            status.color = [1,0,0,1]


#CRIANDO A FUNCAO QUE ASSIMILA AS IMAGENS DOS HORARIOS:

    def horarios(self):

        try:
            if aluno.turma == turma_A:

                imagem_segunda.source = "segunda_A.png"
                imagem_terca.source = "terca_A.png"
                imagem_quarta.source = "quarta_A.png"
                imagem_quinta.source = "quinta_A.png"
                imagem_sexta.source = "sexta_A.png"

            elif aluno.turma == turma_B:

                imagem_segunda.source = "segunda_B.png"
                imagem_terca.source = "terca_B.png"
                imagem_quarta.source = "quarta_B.png"
                imagem_quinta.source = "quinta_B.png"
                imagem_sexta.source = "sexta_B.png"

            elif aluno.turma == turma_C:

                imagem_segunda.source = "segunda_C.png"
                imagem_terca.source = "terca_C.png"
                imagem_quarta.source = "quarta_C.png"
                imagem_quinta.source = "quinta_C.png"
                imagem_sexta.source = "sexta_C.png"

            else:
                pass

        except AttributeError:
            pass

#CRIANDO A FUNCAO QUE RESETA A TELA 'USUARIO' SE O USUARIO SAIR:

    def reset_user_screen(self):

        global aluno

        aluno = None

        user_input.text = ""

        status.color = [0,0,0,1]

        root_widget.current = 'Usuario'

#CRIANDO UMA FUNCAO DE DELAY:

    def delay(self, t):

        time.sleep(t)

#CRIANDO A FUNCAO QUE RETORNARA O NOME DO USUARIO NA TELA:

    def nome_usuario(self):

        bem_vindo_label.text = aluno.nome


#======================================================================================================================#

#STRING QUE CONSTROI O PROGRAMA:


root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:

    transition: FadeTransition()

    Usuario:
    Bem_Vindo:
    Mapa:
    Professores:
    Sair:

    Segunda:
    Terca:
    Quarta:
    Quinta:
    Sexta:

    Heloisa:
    Leonidas:
    Mauricio:
    FabioO:
    Paulina:
    Fernando:
    FabioM:
    Luciano:
    Vinicius:
    Lourenco:

<Usuario>:
    name: 'Usuario'

    FloatLayout:

        Button:
            text: "FREE_ENTER"
            size_hint: .1,.1
            pos_hint: {'center_x': .1, 'center_y': .8}
            on_release: app.root.current = 'Segunda'

        Label:
            pos_hint: {'center_x': .5, 'center_y':.85}
            text: 'INSPERBRAIN'
            font_size: 50
            size_hint_y: 1.7
            size_hint_x: 1

        GridLayout:
            id: grid_layout_user_screen
            size_hint_y: .08
            size_hint_x: .8
            height: 80
            pos_hint: {'center_x': .5, 'center_y':.6}
            cols: 2

            Label:
                text: "Login"
                font_size: 20
                pos_hint: {'center_x': .5, 'center_y':.5}
                size_hint: [.3,1]

            TextInput:
                id: text_input
                size_hint: [1,1]
                font_size: 30
                multiline: False
                on_text: root.manager.variaveis()
                on_text_validate: root.manager.checa_usuario(), root.manager.horarios()

        Label:
            id: status_label
            text: ""
            font_size: 15
            color: [0,0,0,1]
            size_hint: [1,.15]
            pos_hint: {'center_x': .5, 'center_y':.5}


        Button:
            id: button_go
            text: 'Go!'
            font_size: 40 if self.state == 'normal' else 30
            size_hint_y: .3
            size_hint_x: 1
            pos_hint: {'center_x': .5, 'center_y':.15}
            on_press: root.manager.checa_usuario()
            on_release: root.manager.horarios()
            background_normal: ''
            background_color: [0.9, 0.1, 0.2, 1] if self.state == 'normal' else [0.9, 0.1, 0.2, .7]


<Bem_Vindo>:
    name: "Bem_Vindo"

    BoxLayout:
        orientation: 'vertical'
        size_hint: [1,1]

        Label:
            text: "Bem Vindo,"
            font_size: 30
            color: [0,1,0,1]

        Label:
            id: bem_vindo_label
            text: ""
            font_size: 50
            color: [0,1,0,1]


<Segunda>:
    name: 'Segunda'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,.11]

            Button:
                text: 'Seg'
                color: [0,0.9,1,1] if root.manager.current == 'Segunda' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Segunda' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Ter'
                color: [0,0.9,1,1] if root.manager.current == 'Terca' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Terca' else 20
                on_release: app.root.current = 'Terca'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qua'
                color: [0,0.9,1,1] if root.manager.current == 'Quarta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quarta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qui'
                color: [0,0.9,1,1] if root.manager.current == 'Quinta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quinta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Sex'
                color: [0,0.9,1,1] if root.manager.current == 'Sexta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Sexta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

        Image:
            id: image_segunda
            source: 'Segunda_B.png'
            size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Terca>:
    name: 'Terca'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,.11]

            Button:
                text: 'Seg'
                color: [0,0.9,1,1] if root.manager.current == 'Segunda' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Segunda' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Ter'
                color: [0,0.9,1,1] if root.manager.current == 'Terca' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Terca' else 20
                on_release: app.root.current = 'Terca'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qua'
                color: [0,0.9,1,1] if root.manager.current == 'Quarta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quarta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qui'
                color: [0,0.9,1,1] if root.manager.current == 'Quinta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quinta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Sex'
                color: [0,0.9,1,1] if root.manager.current == 'Sexta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Sexta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

        Image:
            id: image_terca
            source: 'Terca_B.png'
            size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]
            spacing: [5,5]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Quarta>:
    name: 'Quarta'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,.11]

            Button:
                text: 'Seg'
                color: [0,0.9,1,1] if root.manager.current == 'Segunda' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Segunda' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Ter'
                color: [0,0.9,1,1] if root.manager.current == 'Terca' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Terca' else 20
                on_release: app.root.current = 'Terca'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qua'
                color: [0,0.9,1,1] if root.manager.current == 'Quarta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quarta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qui'
                color: [0,0.9,1,1] if root.manager.current == 'Quinta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quinta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Sex'
                color: [0,0.9,1,1] if root.manager.current == 'Sexta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Sexta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

        BoxLayout:
            size_hint: [1,1]

            Image:
                id: image_quarta
                source: 'Quarta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Quinta>:
    name: 'Quinta'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,.11]

            Button:
                text: 'Seg'
                color: [0,0.9,1,1] if root.manager.current == 'Segunda' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Segunda' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Ter'
                color: [0,0.9,1,1] if root.manager.current == 'Terca' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Terca' else 20
                on_release: app.root.current = 'Terca'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qua'
                color: [0,0.9,1,1] if root.manager.current == 'Quarta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quarta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qui'
                color: [0,0.9,1,1] if root.manager.current == 'Quinta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quinta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Sex'
                color: [0,0.9,1,1] if root.manager.current == 'Sexta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Sexta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

        BoxLayout:
            size_hint: [1,1]

            Image:
                id: image_quinta
                source: 'Quinta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Sexta>:
    name: 'Sexta'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,.11]

            Button:
                text: 'Seg'
                color: [0,0.9,1,1] if root.manager.current == 'Segunda' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Segunda' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Ter'
                color: [0,0.9,1,1] if root.manager.current == 'Terca' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Terca' else 20
                on_release: app.root.current = 'Terca'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qua'
                color: [0,0.9,1,1] if root.manager.current == 'Quarta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quarta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Qui'
                color: [0,0.9,1,1] if root.manager.current == 'Quinta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Quinta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

            Button:
                text: 'Sex'
                color: [0,0.9,1,1] if root.manager.current == 'Sexta' else [1,1,1,1]
                font_size: 30 if root.manager.current == 'Sexta' else 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'
                background_normal: ''
                background_down: ''
                background_color: [0, 0, 0, 1]

        BoxLayout:
            size_hint: [1,1]
            Image:
                id: image_sexta
                source: 'Sexta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Mapa>:
    name: 'Mapa'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]

            do_rotation: False
			do_translation: False

            Image:
                source: 'mapa_insper.png'

                size_hint: [1,1]

                width: root.width
				height: root.height
				allow_stretch: True

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Heloisa>:
    name: 'Heloisa'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'heloisa.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Leonidas>:
    name: 'Leonidas'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'leo.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True


<Mauricio>:
    name: 'Mauricio'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'mauricio.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True


<FabioO>:
    name: 'FabioO'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'fabio_orfali.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Paulina>:
    name: 'Paulina'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'paulina.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True


<Fernando>:
    name: 'Fernando'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'fernando_orsatti.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<FabioM>:
    name: 'FabioM'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'fabio_miranda.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Luciano>:
    name: 'Luciano'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'luciano.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Vinicius>:
    name: 'Vinicius'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'vinicius.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Lourenco>:
    name: 'Lourenco'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'loureco.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Professores>:
    name: 'Professores'

    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        GridLayout:
            cols: 2
            spacing: 1
            orientation: 'vertical'
            size_hint: [1,1]
            pos_hint:{'y' : .1}

            Button:
                text: 'Heloisa Neves'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Heloisa'

            Button:
                text: 'Leonidas Junior'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Leonidas'

            Button:
                text: 'Mauricio Ferreira'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Mauricio'

            Button:
                text: 'Fabio Orfali'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'FabioO'

            Button:
                text: 'Paulina Achurra'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Paulina'

            Button:
                text: 'Fernando Orsatti'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Fernando'

            Button:
                text: 'Fabio Miranda'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'FabioM'

            Button:
                text: 'Luciano Soares'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Luciano'

            Button:
                text: 'Vinicius Licks'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Vinicius'

            Button:
                text: 'Francisco Lourenço'
                font_size: 20
                size_hint: [.01,.01]
                on_release: app.root.current = 'Lourenco'

        BoxLayout:
            orinetation: 'horizontal'
            size_hint: [1, .1]

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Mapa'

                Image:
                    source: 'mapa.png' if root.manager.current != 'Mapa' else 'mapa_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Segunda'

                Image:
                    source: 'calendario.png' if root.manager.current != 'Segunda' and root.manager.current != 'Terca' and root.manager.current != 'Quarta' and root.manager.current != 'Quinta' and root.manager.current != 'Sexta' else 'calendario_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Professores'

                Image:
                    source: 'professores.png' if root.manager.current != 'Professores' else 'professores_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                background_normal: ''
                background_down: ''
                background_color: [0.9, 0.1, 0.2, 1]
                on_release: app.root.current = 'Sair'

                Image:
                    source: 'sair.png' if root.manager.current != 'Sair' else 'sair_2.png'
                    size: 50,50
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Sair>:
    name: 'Sair'

    canvas:
        Color:
            rgba: 0,0,0,1

        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        Button:
            text: 'SIM'
            font_size: 40 if self.state == 'normal' else 30
            size_hint_y: .5
            size_hint_x: 1
            pos_hint: {'center_x': 0.5, 'center_y':.75}
            on_release: root.manager.reset_user_screen()
            background_color: [0,255,0,1] if self.state == 'normal' else [0,255,0,.7]

        Label:
            pos_hint: {'center_x': .5, 'center_y':.5}
            text: 'Quer mesmo sair?'
            color: [1,1,1,1]
            font_size: 40
            size_hint_y: .1
            size_hint_x: 1


        Button:
            text: 'NÃO'
            font_size: 40 if self.state == 'normal' else 30
            size_hint_y: .5
            size_hint_x: 1
            pos_hint: {'center_x': 0.5, 'center_y':.25}
            on_release: app.root.current = 'Segunda'
            background_color: [255,0,0,1] if self.state == 'normal' else [255,0,0,.7]

''')

class InsperBrain(App):
    def build(self):
        return root_widget

InsperBrain().run()
