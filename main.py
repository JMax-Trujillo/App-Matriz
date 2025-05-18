'''
Aqui se tendra la info de la estructura para el main

configurar el tamaño para celular

class MainApp(App):
    def build(self):
        aqui colocar la pantalla general
        sm = ScreenManager()
        aqui añadir las pantallas que se agregaran a la principal
        pagina_login = .......-> login.py()
        pagina_menú = .........> menu.py(){  -----> solo los botones del menú
            2 opciones principales:
            Opcion{ 
                Suma-------> Cuando esté en esta opcion, que lleve a un screen de operacion.py
                Resta
                Multiplicacion
                Determinante
                Traspuesta
                Inversa
            }
            Historial{
                Suma--------> Cuando esté en esta opcion, que lleve a un screen de vista de historial
                Resta
                Multiplicacion
                Determinante
                Traspuesta
                Inversa
            }
        }
        pagina_operacion = ......> operacion.py(
            Screen principal {
                boxlayout{
                    Color de la operacion correspondiente
                    label = titulo (nombre de la operacion)
                    gridlayout{
                        matriz_respuesta(boxlayout), ocupa 2 filas{
                            label = resultado
                            boxlayout{
                                orientacion vertical
                                canvas before rectangulo, diseño de matriz
                                label = matriz[0]
                                label = matriz[1]
                                label = matriz[2]
                            }
                        }
                        matriz_A(boxlayout){
                            label = resultado
                            boxlayout{
                                orientacion vertical
                                canvas before rectangulo, diseño de matriz
                                label = matriz[0]
                                label = matriz[1]
                                label = matriz[2]
                            }
                        }
                        matriz_B(boxlayout){
                            label = resultado
                            boxlayout{
                                orientacion vertical
                                canvas before rectangulo, diseño de matriz
                                label = matriz[0]
                                label = matriz[1]
                                label = matriz[2]
                            }
                        }
                    }
                    butones_2(boxlayout){
                        button{
                            text = 'Editar'
                            Añadir logoca
                        }
                        button{
                            text = 'Resultados'
                            Añadir logoca
                        }
                    num_buttons(griddlayoud){
                        columnas 4
                        filas 3
                        button{
                            text = '1'
                            Añadir logoca
                        }
                        button{
                            text = '2'
                            Añadir logoca
                        }
                        button{
                            text = '3'
                            Añadir logoca
                        }
                        button{
                            text = '4'
                            Añadir logoca
                        }
                        button{
                            text = '5'
                            Añadir logoca
                        }
                        button{
                            text = '6'
                            Añadir logoca
                        }
                        button{
                            text = '7'
                            Añadir logoca
                        }
                        button{
                            text = '8'
                            Añadir logoca
                        }
                        button{
                            text = '9'
                            Añadir logoca
                        }
                        button{
                            text = '0'
                            Añadir logoca
                        }
                        button{
                            text = '.'
                            Añadir logoca
                        }
                        button{
                            text = '+-'   # Cambia de signo
                            Añadir logoca
                        }
                        button{
                            text = 'Derecha'
                            Añadir logoca
                        }
                        button{
                            text = 'Izquierda'
                            Añadir logica
                        }
                        button{
                            text = 'Igual'
                            Añadir logica
                        }
                    }
                    }
                    Widget --> Este sera solo pa ocupar espacio
                }
                
                
            }
        )
        sm.addwidget(pagina1)
        return principal

if __name__ == '__main__':
    MainApp().run()
'''

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


