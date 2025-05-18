import os
import webbrowser
from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
import app.utils.globals as g

# Configuración para vista móvil
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '0')

# Ruta del fondo
ruta_base = os.path.dirname(__file__)
ruta_img = os.path.join(ruta_base, '..', 'src', 'img', 'login.jpg')


# Estilos personalizados
class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.25)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.background_color = (0, 0, 0, 0)
        self.foreground_color = (1, 1, 1, 1)
        self.hint_text_color = (0.8, 0.8, 0.8, 1)
        self.padding = [40, 10, 10, 10]
        self.font_size = 16
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.3)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[25])
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = 14
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


# Contenido principal de login
class LoginContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 12
        self.padding = [20, 20, 20, 20]
        self.size_hint = (0.85, 0.85)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        with self.canvas.before:
            Color(0.2, 0.2, 0.3, 0.85)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Widgets
        self.add_widget(Label(text="Login", font_size=28, color=(1, 1, 1, 1), size_hint=(1, 0.15)))
        self.add_widget(Label(text="Choose a user to start", font_size=14, color=(1, 1, 1, 0.9), size_hint=(1, 0.1)))

        self.username_input = RoundedTextInput(hint_text="Username", multiline=False, size_hint=(1, 0.15))
        self.password_input = RoundedTextInput(hint_text="Password", password=True, multiline=False, size_hint=(1, 0.15))

        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.add_widget(Label(text="Or continue with", font_size=12, color=(1, 1, 1, 0.8), size_hint=(1, 0.1)))

        self.add_widget(self.build_third_party_buttons())

        login_btn = RoundedButton(text="Log in", size_hint=(1, 0.18))
        login_btn.background_color = (0.0, 0.4, 1.0, 1)
        login_btn.bind(on_release=self.next_page)
        self.add_widget(login_btn)

    def build_third_party_buttons(self):
        container = BoxLayout(orientation='horizontal', spacing=12, size_hint=(1, 0.15))

        btns = [
            ("UNAB", 'https://www.portal.unab.edu.pe/'),
            ("GitHub", 'https://github.com/JMax-Trujillo'),
            ("EPISI", 'https://frabjous-kelpie-f088da.netlify.app/')
        ]
        for name, url in btns:
            b = RoundedButton(text=name)
            b.size_hint = (1 / len(btns), 1)
            b.bind(on_release=lambda x, u=url: webbrowser.open(u))
            container.add_widget(b)
        return container

    def next_page(self, instance):
        g.current_user = self.username_input.text
        g.current_password = self.password_input.text
        self.parent.manager.current = 'menu'
        self.parent.manager.transition.direction = 'left'

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


# Pantalla de Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fondo = Image(source=ruta_img, allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        content = LoginContent()
        self.username_input = content.username_input
        self.password_input = content.password_input
        self.add_widget(fondo)
        self.add_widget(content)
