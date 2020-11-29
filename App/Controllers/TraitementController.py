#_*_ coding: UTF8 _*_
from App.Controllers.Controller import View
from App.Models.Palette import Palette

class TraitementController():
    
    def index(self):
        print('Controller : TraitementController => index')
        return View("traitement")

if __name__=='__index__':
    TraitementController().index()