#_*_ coding: UTF8 _*_
from App.Controllers.Controller import View

class SettingController():
    
    def index(self):
        print('Controller : SettingsController => index')
        return View("settings")

if __name__=='__index__':
    SettingController().index()