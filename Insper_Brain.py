from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import time
import random
from Dic_turmas import *
from Classes_dos_objetos import *

#======================================================================================================================#

#CRIANDO OS PROFESSORES:

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

aluno = None

#======================================================================================================================#

#CRIANDO A INTERFACE:


class Usuario(Screen):
    pass

class Mapa(Screen):
    pass

class Calendario(Screen):
    pass

class Professores(Screen):
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


class MyScreenManager(ScreenManager):

    def checa_usuario(self, *args):
        input = self.screens[0].ids["text_input"]
        input = input.text.lower()

        status = self.screens[0].ids["status_label"]

        if input in dic_A:

            global aluno

            nome = dic_A[input]

            aluno = Aluno(nome, input, turma_A)

            status.text = "Ola {0}".format(dic_A[input][0])
            status.color = [0,1,0,1]

            root_widget.current = 'Calendario'


        elif input in dic_B:

            global aluno

            nome = dic_B[input]

            aluno = Aluno(nome, input, turma_B)

            status.text = "Ola {0}".format(dic_B[input][0])
            status.color = [0,1,0,1]

            root_widget.current = 'Calendario'




        elif input in dic_C:

            global aluno

            nome = dic_C[input]

            aluno = Aluno(nome, input, turma_C)

            status.text = "Ola {0}".format(dic_C[input][0])
            status.color = [0,1,0,1]

            root_widget.current = 'Calendario'


        else:

            status.text = "Usuario Invalido"
            status.color = [1,0,0,1]

            pass


        def teste():

            try:
                for e in aluno.nome:
                    print(e)

            except:

                print('inexistente')

        #teste()

root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:

    transition: FadeTransition()

    Usuario:

    Calendario:
    Mapa:
    Professores:
    Sair:

    Segunda:
    Terca:
    Quarta:
    Quinta:
    Sexta:

<Usuario>:
    name: 'Usuario'
    FloatLayout:
        Label:
            text: 'Bem Vindo ao INSPERBRAIN'
            font_size: 50
            size_hint_y: 1.7
            size_hint_x: .95
        GridLayout:
            size_hint_y: 0.08
            size_hint_x: .8
            height: 80
            pos_hint: {'center_x': .5, 'center_y':.6}
            cols: 3
            Label:
                text: "Login"
                font_size: 30
            TextInput:
                id: text_input
                font_size: 30
                multiline: False
            Label:
                id: status_label
                text: ""
                font_size: 15
                color: [1,0,0,1]

        Button:
            text: 'Ir'
            font_size: 30
            size_hint_y: .1
            size_hint_x: .1
            pos_hint: {'center_x': .5, 'center_y':.4}
            on_release: root.manager.checa_usuario()

<Calendario>:
    name: 'Calendario'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.1]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:

            Button:
                font_size: 20
                size_hint: [1,.1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,.1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,.1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,.1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Segunda>:
    name: 'Segunda'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.11]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'Segunda_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Terca>:
    name: 'Terca'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.11]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'Terca_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Quarta>:
    name: 'Quarta'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.11]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'Quarta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Quinta>:
    name: 'Quinta'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.11]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'Quinta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Sexta>:
    name: 'Sexta'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:

            size_hint: [1,.11]

            Button:
                text: 'Seg'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Segunda'
            Button:
                text: 'Ter'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Terca'

            Button:
                text: 'Qua'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quarta'

            Button:
                text: 'Qui'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Quinta'

            Button:
                text: 'Sex'
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sexta'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'Sexta_B.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.11]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Mapa>:
    name: 'Mapa'

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint: [1,1]
            Image:
                source: 'mapa_insper.png'
                size_hint: [1,1]

        BoxLayout:
            size_hint: [1,.1]

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,1]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Professores>:
    name: 'Professores'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Professores'
            font_size: 30
            size_hint: [1,.1]

        BoxLayout:

        BoxLayout:

            Button:
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Mapa'
                Image:
                    source: 'mapa.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True
            Button:
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Calendario'
                Image:
                    source: 'calendario.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Professores'
                Image:
                    source: 'professores.png'
                    size_hint: [1,1]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

            Button:
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Sair'
                Image:
                    source: 'sair.png'
                    size_hint: [.3,.3]
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    allow_stretch: True

<Sair>:
    name: 'Sair'

    FloatLayout:
        Label:
            text: 'Tem certeza que deseja sair?'
            font_size: 50
            size_hint_y: 1.7
            size_hint_x: .95
        Button:
            text: 'SIM'
            font_size: 30
            size_hint_y: .15
            size_hint_x: .2
            pos_hint: {'center_x': 0.4, 'center_y':.4}
            on_release: app.root.current = 'Usuario'
        Button:
            text: 'NAO'
            font_size: 30
            size_hint_y: .15
            size_hint_x: .2
            pos_hint: {'center_x': 0.6, 'center_y':.4}
            on_release: app.root.current = 'Calendario'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()

