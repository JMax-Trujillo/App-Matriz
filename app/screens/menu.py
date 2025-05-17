'''
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
'''

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class RoundedBox(Button):
    def __init__(self,title, color,**kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.title = title
        size_hint=(0.45, 0.3)
        with self.canvas.before:
            Color(1, 1, 1, 0.3)  
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # lista con los botones
        self.buttons={
            'Suma': (0.1, 0.5, 0.5, 0.3),
            'Resta': (0.1, 0.5, 0.5, 0.3),
            'Multiplicacion': (0.1, 0.5, 0.5, 0.3),
            'Determinante': (0.1, 0.5, 0.5, 0.3),
            'Traspuesta': (0.1, 0.5, 0.5, 0.3),
            'Inversa': (0.1, 0.5, 0.5, 0.3),
        }
        
        # agregar widgets
        super_container = BoxLayout(
            orientation='vertical',
        )
        upper = Label(
            text = 'Usuario',
            font_size=32,
            size_hint_y=0.10
        )
        button_up_container = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.10,
            padding=10,
            spacing=10
        )
        button_up_option = Button(
            text='Opcion',
            size_hint=(0.5, 0.90)
        )
        button_up_historial = Button(
            text='Historial',
            size_hint=(0.5, 0.90)
        )
        button_up_container.add_widget(button_up_option)
        button_up_container.add_widget(button_up_historial)


        button_main_container = GridLayout(
            cols=2,
            rows=3,
            size_hint=(1, 0.70),
            padding=[10, 10, 10, 10],
            spacing = 10,
        )
        for i in self.buttons:
            button= Button(
                text=i,
                size_hint=(0.5,0.3),
                color=self.buttons[i]
            )
            button_main_container.add_widget(button)
        down = Widget(
            size_hint_y=0.10
        )
        
        # Agregar los widgets al contenedor principal
        super_container.add_widget(upper)
        super_container.add_widget(button_up_container)
        super_container.add_widget(button_main_container)
        super_container.add_widget(down)
        self.add_widget(super_container)