from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKmApp().run()
