"""
CP1404 Practical 7
Joshua Dubbeld
29/09/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """App to convert miles to kilometers"""
    miles_output = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")

        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.miles_output = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
