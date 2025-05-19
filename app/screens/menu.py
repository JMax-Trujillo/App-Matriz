from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
import app.utils.globals as g
from app.screens.login import RoundedButton


class MenuScreen(Screen):
    user_name = StringProperty("")

    def __init__(self, **kw):
        super().__init__(**kw)
        self.username = g.current_user
        self.password = g.current_password

        # ---- COLORES DE LOS BOTONES PRINCIPALES ---- #
        self.buttons = {
            'Suma': (0.95, 0.6, 0.2, 1),           # Naranja
            'Resta': (0.2, 0.6, 1, 1),             # Azul claro
            'Multiplicacion': (1, 0.4, 0.7, 1),    # Rosado
            'Determinante': (0, 0.6, 0.3, 1),      # Verde
            'Traspuesta': (0.3, 0.8, 1, 1),        # Celeste
            'Inversa': (0.5, 1, 0.6, 1),           # Verde claro
        }

        self.build_ui()

    def build_ui(self):
        # --- CONTENEDOR PRINCIPAL ---
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=15)

        # --- MENSAJE DE BIENVENIDA ---
        self.label_usuario = Label(
            text=f'Bienvenido {self.username}',
            font_size=26,
            color=(1, 1, 1, 1),
            size_hint_y=0.12
        )

        # --- BOTONES SUPERIORES ---
        button_top = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.12)

        btn_opcion = RoundedButton(
            text='Opciones',
            background_color=(0.2, 0.6, 0.8, 1),
        )
        btn_historial = RoundedButton(
            text='Historial',
            background_color=(0.2, 0.6, 0.8, 1),
        )

        button_top.add_widget(btn_opcion)
        button_top.add_widget(btn_historial)

        # --- BOTONES PRINCIPALES DE OPERACIONES ---
        button_grid = GridLayout(cols=2, spacing=12, size_hint=(1, 0.60), padding=10)

        self.operation_suma = RoundedButton(
            text='Suma',
            background_color=(0.95, 0.6, 0.2, 1),
            on_release=self.go_to_operation_suma
        )
        self.operation_resta = RoundedButton(
            text='Resta',
            background_color=(0.2, 0.6, 1, 1),
            on_release=self.go_to_operation_resta
        )
        self.operation_multiplicacion = RoundedButton(
            text='Multiplicacion',
            background_color=(1, 0.4, 0.7, 1),
            on_release=self.go_to_operation_multiplicacion
        )
        self.operation_determinante = RoundedButton(
            text='Determinante',
            background_color=(0, 0.6, 0.3, 1),
            on_release=self.go_to_operation_determinante
        )
        self.operation_traspuesta = RoundedButton(
            text='Traspuesta',
            background_color=(0.3, 0.8, 1, 1),
            on_release=self.go_to_operation_traspuesta
        )
        self.operation_inversa = RoundedButton(
            text='Inversa',
            background_color=(0.5, 1, 0.6, 1),
            on_release=self.go_to_operation_inversa
        )
        
        # Agregamos los botones al grid
        button_grid.add_widget(self.operation_suma)
        button_grid.add_widget(self.operation_resta)
        button_grid.add_widget(self.operation_multiplicacion)
        button_grid.add_widget(self.operation_determinante)
        button_grid.add_widget(self.operation_traspuesta)
        button_grid.add_widget(self.operation_inversa)

        # --- ESPACIO Y BOTÓN DE CERRAR SESIÓN ---
        spacer = Widget(size_hint_y=0.05)

        logout_btn = RoundedButton(
            text='Cerrar sesión',
            background_color=(1, 0.3, 0.3, 1),
            size_hint_y=0.12,
            on_release=self.logout
        )

        # --- AGREGAR TODO AL CONTENEDOR ---
        main_layout.add_widget(self.label_usuario)
        main_layout.add_widget(button_top)
        main_layout.add_widget(button_grid)
        main_layout.add_widget(spacer)
        main_layout.add_widget(logout_btn)

        self.add_widget(main_layout)

    def on_pre_enter(self, *args):
        self.label_usuario.text = f'Bienvenido {g.current_user}'

    def go_to_operation_suma(self, instance):
        g.title_operation = "Suma"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_suma'

    def go_to_operation_resta(self, instance):
        g.title_operation = "Resta"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_resta'

    def go_to_operation_multiplicacion(self, instance):
        g.title_operation = "Multiplicacion"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_multiplicacion'

    def go_to_operation_determinante(self, instance):
        g.title_operation = "Determinante"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_determinante'

    def go_to_operation_traspuesta(self, instance):
        g.title_operation = "Traspuesta"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_traspuesta'

    def go_to_operation_inversa(self, instance):
        g.title_operation = "Inversa"
        self.manager.transition.direction = 'left'
        self.manager.current = 'operation_inversa'

    def logout(self, instance):
        g.current_user = ""
        g.current_password = ""
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
