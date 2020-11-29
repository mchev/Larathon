#_*_ coding: UTF8 _*_
from App.Controllers.Controller import View

class HomeController():
    
    def index(self):
        print('Controller : HomeController => index')
        return View("traitement")

if __name__=='__index__':
    HomeController().index()