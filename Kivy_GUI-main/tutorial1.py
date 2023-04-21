import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class MyApp(App):
    def buid(self):
        return Label(text="Sagar world")

MyApp().run()

# /workspaces/Kivy_GUI/kivy/share/kivy-examples