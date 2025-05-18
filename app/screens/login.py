'''
Estructura del trabajo

login.py -> Login{
    Screen (principal){
        BackGround(boxtlayout){
        centrado
            label -> titulo, letra mas grande
            label -> subtitulo, text = 'Choose a user to start
            button {
                placeholder = 'Username',
                icon = person.icon
                border = algo, ya le añades luego
        }
        button {
            placeholder = 'Password',
            icon = padlock.icon
            border = algo, ya le añades luego
        }
        label{
            'Or continue with: ',
            lado izquierdo,
            añadir un canvas para dibujar una linea blanca al lado, supongo q un rectangulo superpequeño
        }
        boxlayout{
            orientation = 'horizontal'
            padding = 10
            button {
                icon = unab.icon
                agregar funcionalidad para enviar a una pagina web de la UNAB
            }
            button {
                icon = github.icon
                agregar funcionalidad para enviar a mi github
            }
            button {
                icon = episi.icon
                agregar funcionalidad para enviar a una pagina web de la carrera
            }
        }
        button {
            text='login',
            color azul, texto blanco
        }
    }
    }
}
'''
import os
ruta_base = os.path.dirname(__file__)
ruta_img = os.path.join(ruta_base, '..', 'src', 'img', 'login.jpg')

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import webbrowser

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '0')


# TODO: Estilos de figuras
class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.5)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
        self.background_color = (0, 0, 0, 0)
        self.foreground_color = (0, 0, 0, 1)
        self.hint_text_color = (0.3, 0.3, 0.3, 1)
        self.padding = [10, 10, 10, 10]
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.3)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[40])
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class BackGround(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.size_hint = (0.8, 0.8)
        with self.canvas.before:
            # TODO Definir el color de fondo
            Color(0.4, 0.4, 0.4, 0.8)
            # Definir el rectangulo que cubre el fondo del login
            self.rect = Rectangle(
                # source='app/assets/img/login.jpg',
                size=self.size,
                pos=self.pos)
        self.bind(size=self._update, pos=self._update)

        # Añadir las variables de la pantalla de login
        titulo = Label(
            text='Login',
            font_size=32,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        sub_titulo = Label(
            text='Choose a user to start',
            font_size=16,
            color=(1, 1, 1, 1),
            size_hint = (1, 0.2),
            pos_hint={'x': 0, 'y': 0}
        )
        username_input = RoundedTextInput(
            hint_text='Username',
            size_hint=(1, 0.2),
            pos_hint={'x': 0, 'y': 0},
            multiline=False,
            background_color=(1, 1, 1, 0.5),
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.3, 0.3, 0.3, 1)
        )
        password_input = RoundedTextInput(
            hint_text='Password',
            password=True,
            size_hint=(1, 0.2),
            pos_hint={'x': 0, 'y': 0},
            multiline=False,
            background_color=(1, 1, 1, 0.5),
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.3, 0.3, 0.3, 1)
        )
        continue_label = Label(
            text='Or continue with:',
            size_hint=(1, 0.12),
            pos_hint={'x': 0, 'y': 0},
            color=(1, 1, 1, 1)
        )

        # Añadir un contenedor para los botones
        button_container = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.2),
            pos_hint={'x': 0, 'y': 0},
            padding=[10, 10, 10, 10],
            spacing=10
        )

        # Crar los botones del contenedor
        unab_button = RoundedButton(
            text='UNAB',
            size_hint=(0.2, 1),
            pos_hint={'x': 0, 'y': 0},
            background_color=(1, 1, 1, 0.5),
            color=(0, 0, 0, 1)
        )
        unab_button.bind(on_release=lambda x: webbrowser.open('https://www.portal.unab.edu.pe/'))
        github_button = RoundedButton(
            text='GitHub',
            size_hint=(0.2, 1),
            pos_hint={'x': 0, 'y': 0},
            background_color=(1, 1, 1, 0.5),
            color=(0, 0, 0, 1)
        )
        github_button.bind(on_release=lambda x: webbrowser.open('https://github.com/JMax-Trujillo'))
        episi_button = RoundedButton(
            text='EPISI',
            size_hint=(0.2, 1),
            pos_hint={'x': 0, 'y': 0},
            background_color=(1, 1, 1, 0.5),
            color=(0, 0, 0, 1)
        )
        episi_button.bind(on_release=lambda x: webbrowser.open('https://frabjous-kelpie-f088da.netlify.app/'))

        # Añadir los botones al contenedor

        button_container.add_widget(unab_button)
        button_container.add_widget(github_button)
        button_container.add_widget(episi_button)

        login_button = RoundedButton(
            text='Login',
            size_hint=(1, 0.2),
            pos_hint={'x': 0, 'y': 0},
            background_color=(0.0, 0.4, 1.0, 1),
            color=(1, 1, 1, 1)
            # on_press=self.
        )
        login_button.bind(on_release=self.next_page)

        # Añadir los widgets de la pantalla de login
        self.add_widget(titulo)
        self.add_widget(sub_titulo)
        self.add_widget(username_input)
        self.add_widget(password_input)
        self.add_widget(continue_label)
        self.add_widget(button_container)
        self.add_widget(login_button)

    def next_page(self, instance):
        self.parent.manager.current = 'menu'

    def _update(self, *args):
        # Actualizar el tamaño y la posicion del rectangulo
        self.rect.pos = self.pos
        self.rect.size = self.size

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        '''with self.canvas.before:
            # Define el background color
            Color(1, 0, 0.14, 1)
            # Define el rectangulo que cubre toda la pantalla
            self.rect = Rectangle(
                source='../src/img/login.jpg',
                size=self.size,
                pos=self.pos)'''
        fondo = Image(
            source=ruta_img,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        # self.bind(size=self._update, pos=self._update)

        # Variables de la pantalla de login
        login = BackGround()
        self.add_widget(fondo)
        self.add_widget(login)

    # def _update(self, *args):
    #         # Actualiza el tamaño y la posicion del rectangulo
    #         self.rect.pos = self.pos
    #         self.rect.size = self.size
    
    
    
