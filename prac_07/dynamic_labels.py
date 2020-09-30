
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Josh', 'Chris', 'James', 'Tim']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.list_names()
        return self.root

    def list_names(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.labels.add_widget(temp_label)


DynamicLabelsApp().run()
