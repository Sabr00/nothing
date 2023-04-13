import kivy
kivy.require('2.1.0')

from kivy.lang.builder import Builder
Builder.load_file('my.kv')    #nazwa pliku kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class Kalkulator(BoxLayout):  #mozesz zmienic nazwe klasy

    def number(self, value):  #funkcja ktora wypisuje na label wartosc (spojrz na plik kivy)
        self.ids.ekran.text += value

    def wynik(self, *args):  #funkcja ktora robi kazde dzialanie z ekranu (funkcja eval), a jesli jest blad to wypisuje blad
        wynik = self.ids.ekran.text
        if wynik != '':
            try:
                self.ids.ekran.text = str(eval(wynik))
            except Exception as error:
                self.ids.ekran.text = "BŁĄD"

    def clear(self, *args):  #czyli no czysci przy AC
        self.ids.ekran.text = ''
        
class Aplikacja(App):  #a to jest glowna klasa aplikacji, ktora sklada sie z kalkulatora. mozesz zmienic nazwy, we wszystkim mozeszz na dobra sprawe
    def build(self):
        return Kalkulator()


if __name__ == '__main__':
    Aplikacja().run()
