import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from app.screens.login import LoginScreen
from app.screens.menu import MenuScreen
from app.screens.operation_suma import Operation_Suma_Screen
from app.screens.operation_resta import Operation_Resta_Screen
from app.screens.operation_multiplicacion import Operation_Multiplicacion_Screen
from app.screens.operation_determinante import Operation_Determinante_Screen
from app.screens.operation_traspuesta import Operation_Traspuesta_Screen
from app.screens.operation_inversa import Operation_Inversa_Screen

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
        pagina_suma = Operation_Suma_Screen(name='operation_suma')
        pagina_resta = Operation_Resta_Screen(name='operation_resta')
        pagina_multiplicacion = Operation_Multiplicacion_Screen(name='operation_multiplicacion')
        pagina_determinante = Operation_Determinante_Screen(name='operation_determinante')
        pagina_traspuesta = Operation_Traspuesta_Screen(name='operation_traspuesta')
        pagina_inversa = Operation_Inversa_Screen(name='operation_inversa')
        
        # Añadir las pantallas al Screen Manager
        sm.add_widget(pagina_login)
        sm.add_widget(pagina_menu)
        sm.add_widget(pagina_suma)
        sm.add_widget(pagina_resta)
        sm.add_widget(pagina_multiplicacion)
        sm.add_widget(pagina_determinante)
        sm.add_widget(pagina_traspuesta)
        sm.add_widget(pagina_inversa)
        
        # Retornar el Screen Manager
        return sm

if __name__ == '__main__':
    MainApp().run()


