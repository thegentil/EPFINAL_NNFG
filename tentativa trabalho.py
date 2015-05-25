# -*- coding: utf-8 -*-

__author__ = 'felipegiardini'
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from tentativa_trabalho_2 import *

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.username.bind(on_text_validate=faz_login)


def faz_login(value):
    if value.text in dic_A or dic_B or dic_C:
        print('evento aconteceu')
    #print("Evento aconteceu " + value.text)
    #turma = turma_aluno(value.text)
    # Muda a tela

    # Avisa que nao achou login


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()