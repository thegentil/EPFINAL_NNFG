from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='nicolas eh nome de gay')

TestApp().run()