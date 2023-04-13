import kivy
kivy.require('2.1.0')

from kivy.lang.builder import Builder
Builder.load_file('my.kv')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class Kalkulator(BoxLayout):

    def number(self, value):
        self.ids.ekran.text += value

    def wynik(self, *args):
        wynik = self.ids.ekran.text
        if wynik != '':
            try:
                self.ids.ekran.text = str(eval(wynik))
            except Exception as error:
                self.ids.ekran.text = "BŁĄD"

    def clear(self, *args):
        self.ids.ekran.text = ''
        
class Aplikacja(App):
    def build(self):
        return Kalkulator()


if __name__ == '__main__':
    Aplikacja().run()