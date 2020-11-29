import kivy
import runpy
import re
import pathlib
from kivy.app import App
from libraries.env import env
from App.Controllers.Controller import View

#Default view
#view = Controller.View('home')
#view = runpy.run_path("App/Controllers/TraitementController.py", run_name='__index__')

#Load the main layout with the default view
'''
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Builder.load_file("App/Views/partials/header.kv"))
        self.add_widget(view)
        self.add_widget(Builder.load_file("App/Views/partials/footer.kv"))
'''

class App(App):

    route = ""
    params = {}

    def build(self):
        return View('home')

    #Parse routes.py and load the required controller
    def route(self, route, params=None):
        filepath = 'routes.py'
        controller = ""
        controllerClass = ""
        action = ""
        with open(filepath) as fp:
            for line_num, line in enumerate(fp):
                splitted = re.split('=|@', line)
                if splitted[0] == route :
                    controller = splitted[1].replace('"', '')
                    controllerClass = controller.split('/')[-1]
                    action = splitted[2].replace('"', '').replace('\n', '')
        if controller:
            runpy.run_path(controller + '.py', run_name='__index__')
        else:
            print("Le controller pour la route " + route + " est introuvable.")


if __name__ == '__main__':
    App().run()