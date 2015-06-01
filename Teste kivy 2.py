from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import time
import random
from kivy.uix.image import Image
from kivy.uix.widget import Widget

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
    pass

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
            size_hint_x: .6
            height: 80
            pos_hint: {'center_x': .5, 'center_y':.6}
            cols: 2
            Label:
                text: "Login"
                font_size: 30
            TextInput:
                font_size: 30
                multline: False

        Button:
            text: 'Ir'
            font_size: 30
            size_hint_y: .1
            size_hint_x: .1
            pos_hint: {'center_x': .5, 'center_y':.4}
            on_release: app.root.current = 'Calendario'

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

<Terca>:
    name: 'Terca'

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

<Quarta>:
    name: 'Quarta'

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

<Quinta>:
    name: 'Quinta'

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

<Sexta>:
    name: 'Sexta'

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

