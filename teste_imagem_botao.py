__author__ = 'Gabriel Olanda'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
    orientation: "horizontal"
    Button:
        text: "B1"
        size_hint: [.2, .17]
        Image:
            source: 'mapa.jpg'
            size_hint: [.9,.9]
            center_x: self.parent.center_x
            center_y: self.parent.center_y
            allow_stretch: True

""")

class ButtonsApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ButtonsApp().run()
