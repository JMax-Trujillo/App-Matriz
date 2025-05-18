import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from app.screens.login import LoginScreen
from app.screens.menu import MenuScreen
from app.screens.operation import OperationScreen

from kivy.core.window import Window


from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '0')


class MainApp(App):
    def build(self):
        # Crear el Screen Manager
        Window.size = (360, 640)
        sm = ScreenManager()
        
        # Crear las pantallas
        pagina_login = LoginScreen(name='login')
        pagina_menu = MenuScreen(name='menu')
        pagina_operation = OperationScreen(name='operation')
        
        # Añadir las pantallas al Screen Manager
        sm.add_widget(pagina_login)
        sm.add_widget(pagina_menu)
        sm.add_widget(pagina_operation)
        
        # Retornar el Screen Manager
        return sm

if __name__ == '__main__':
    MainApp().run()


