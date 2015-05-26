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

class Mapa(Screen):
    pass

class Calendario(Screen):
    pass

class Professores(Screen):
    pass

class Sair(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:

    transition: FadeTransition()

    Calendario:
    Mapa:
    Professores:
    Sair:

<Calendario>:
    name: 'Calendario'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Calendario'
            font_size: 30
            size_hint: [1,.1]

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
                on_release: app.root.current = 'Sair'

<Mapa>:
    name: 'Mapa'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Mapa'
            font_size: 30
            size_hint: [1,.1]

        BoxLayout:
            Image:
                source: 'LAYOUT REVISADO 07-11-page-001.jpg'
                size_hint: [1,1]

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
                on_release: app.root.current = 'Sair'

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
                on_release: app.root.current = 'Sair'

<Sair>:
    name: 'Sair'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Sair'
            font_size: 30
            size_hint: [1,.1]

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
                on_release: app.root.current = 'Sair'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()

