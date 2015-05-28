from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import time
import random

class Mapa(Screen):
    pass

class Calendario(Screen):
    pass

class Professores(Screen):
    pass

class Sair(Screen):
    pass

class Usuario(Screen):
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

<Usuario>:
    name: 'Usuario'
    FloatLayout:
        Label:
            text: 'Usuario'
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
            text: 'go'
            font_size: 30
            size_hint_y: .1
            size_hint_x: .1
            pos_hint: {'center_x': .5, 'center_y':.4}
            on_release: app.root.current = 'Calendario'



<Calendario>:
    name: 'Calendario'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Calendario'
            font_size: 30
            size_hint: [1,.2]

        BoxLayout:

        BoxLayout:
            Button:
                text: 'Mapa'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Mapa'
            Button:
                text: 'Calendario'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Calendario'

            Button:
                text: 'Professores'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Professores'

            Button:
                text: 'Sair'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Usuario'

<Mapa>:
    name: 'Mapa'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Mapa'
            font_size: 30
            size_hint: [1,.2]

        BoxLayout:

        BoxLayout:
            Button:
                text: 'Mapa'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Mapa'
            Button:
                text: 'Calendario'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Calendario'

            Button:
                text: 'Professores'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Professores'

            Button:
                text: 'Sair'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Usuario'

<Professores>:
    name: 'Professores'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Professores'
            font_size: 30
            size_hint: [1,.2]

        BoxLayout:

        BoxLayout:
            Button:
                text: 'Mapa'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Mapa'
            Button:
                text: 'Calendario'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Calendario'

            Button:
                text: 'Professores'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Professores'

            Button:
                text: 'Sair'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Usuario'

<Sair>:
    name: 'Sair'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Sair'
            font_size: 30
            size_hint: [1,.2]

        BoxLayout:

        BoxLayout:
            Button:
                text: 'Mapa'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Mapa'
            Button:
                text: 'Calendario'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Calendario'

            Button:
                text: 'Professores'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Professores'

            Button:
                text: 'Sair'
                font_size: 20
                size_hint: [1,.2]
                on_release: app.root.current = 'Usuario'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()