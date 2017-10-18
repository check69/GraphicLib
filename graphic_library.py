import kivy
kivy.require('1.10.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout

class MyWidget(Widget):
    pass

class CustomWidget(Widget):
    pass


class MyApp(App):

    def build(self):
        #self.load_kv('MyApp.kv')
        self.title = "Graphic Test Framework"
        return MyWidget()
        return PageLayout()
        return StackLayout()
        return BoxLayout()
        return GridLayout()
        return FloatLayout()
        return CustomWidget()


if __name__ == '__main__':
    MyApp().run()
