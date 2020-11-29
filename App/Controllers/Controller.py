import pathlib
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class View(BoxLayout):

    def __init__(self, view, **kwargs):
        print('View : pages/' + view + '.kv')
        super(View, self).__init__(**kwargs)
        self.clear_widgets()
        self.orientation = "vertical"
        self.add_widget(Builder.load_file("App/Views/partials/header.kv"))
        p = pathlib.Path('App/Views/pages/'+view+'.kv')
        if p.is_file():
            self.add_widget(Builder.load_file("App/Views/pages/"+view+".kv"))
            print("Chargement de la vue ok.")
        else:
            print("La vue " + view + " est introuvable.")
        self.add_widget(Builder.load_file("App/Views/partials/footer.kv"))


'''
    def render(self, **kwargs):
        print('Info : Rendu de la vue ' + view)
        super(Controller, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Builder.load_file("App/Views/partials/header.kv"))
        self.add_widget(self.pageTemplate)
        self.add_widget(Builder.load_file("App/Views/partials/footer.kv"))
'''