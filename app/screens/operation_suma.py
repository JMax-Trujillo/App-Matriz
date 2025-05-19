from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle, Line
from kivy.metrics import dp, sp
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from app.logic.operation_sum import sumar_matrices
from app.logic.operation_resta import restar_matrices
from app.logic.operation_multiplicacion import multiplicar_matrices
import app.utils.globals as g
from kivy.properties import StringProperty

# --- COMPONENTES BÁSICOS ---



class MatrixLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, 1)
        self.labels = []

        with self.canvas.before:
            Color(0.2, 0.8, 0.2, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

        for i in range(9):
            label = TextInput(text='0', font_size=sp(8))
            self.labels.append(label)
            self.add_widget(label)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
class AnswerLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, 1)
        self.labels = []

        with self.canvas.before:
            Color(0.2, 0.8, 0.2, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

        for i in range(9):
            label = Label(text='0', font_size=sp(15))
            self.labels.append(label)
            self.add_widget(label)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


# --- COMPONENTE PRINCIPAL ---

class Operation_Suma_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.operacion_actual = 'suma'
        print(g.title_operation)
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Layout principal
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title = Label(text="Suma", size_hint=(1, 0.1), font_size='20sp', color=(1, 0, 1, 1))
        self.main_layout.add_widget(self.title)

        self.operation_container = BoxLayout(orientation='vertical', size_hint=(1, 0.8), spacing=10)
        self._decorar_fondo(self.operation_container, Color(1, 1, 0, 1), 'rect3')

        self._crear_panel_matrices()
        self._crear_botones_edicion_resultado()
        self._crear_section_screen()

        self.main_layout.add_widget(self.operation_container)
        self.main_layout.add_widget(self._crear_pie())

        self.add_widget(self.main_layout)

    def _crear_panel_matrices(self):
        self.matrix_container = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(300), spacing=10)
        self._decorar_fondo(self.matrix_container, Color(0, 1, 1, 1), 'rect2')

        # Matrices A y B
        self.input_matrix_container = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(10), spacing=10)

        self.matrix_A = self._crear_matriz('A')
        self.matrix_B = self._crear_matriz('B')

        self.input_matrix_container.add_widget(self.matrix_A)
        self.input_matrix_container.add_widget(self.matrix_B)

        # Respuesta
        self.matrix_answer = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(140))
        self._decorar_fondo(self.matrix_answer, Color(0, 1, 0, 1), 'rect_answer')

        answer_label = Label(text='Answer', size_hint=(1, 0.3))
        self.matrix_answer_output = AnswerLayout()
        self.matrix_answer.add_widget(answer_label)
        self.matrix_answer.add_widget(self.matrix_answer_output)

        self.matrix_container.add_widget(self.input_matrix_container)
        self.matrix_container.add_widget(self.matrix_answer)
        self.operation_container.add_widget(self.matrix_container)

    def _crear_matriz(self, nombre):

        if nombre == 'A':
            box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(110))
            self._decorar_fondo(box, Color(0.3, 0.9, 0.3, 1), f'rect{nombre}')

            label = Label(text=f'Matriz {nombre}', size_hint=(1, 0.3))
            layout = MatrixLayout()
            self.matrix_A_output = layout
            self.matrix_A_labels = layout.labels
            self.current_matrix = 'A'
            self.current_index = 0
        else:
            box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(110))
            self._decorar_fondo(box, Color(0.3, 0.9, 0.3, 1), f'rect{nombre}')

            label = Label(text=f'Matriz {nombre}', size_hint=(1, 0.3))
            layout = MatrixLayout()
            self.matrix_B_output = layout
            self.matrix_B_labels = layout.labels

        box.add_widget(label)
        box.add_widget(layout)
        return box

    def _crear_botones_edicion_resultado(self):
        self.button_container_ER = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=10)
        self._decorar_fondo(self.button_container_ER, Color(0.5, 0.8, 0.5, 1), 'rect4')

        edit_button = Button(text='Editar', on_release=self.modo_edicion)
        edit_A = Button(text='A', on_release=lambda x: self.switch_matrix('A'))
        edit_B = Button(text='B', on_release=lambda x: self.switch_matrix('B'))

        edit_box = BoxLayout()
        edit_box.add_widget(edit_A)
        edit_box.add_widget(edit_B)

        self.button_container_ER.add_widget(edit_button)
        self.button_container_ER.add_widget(edit_box)
        self.operation_container.add_widget(self.button_container_ER)

    def _crear_section_screen(self):
        self.section_screen = ScreenManager()
        self.add_edition_screen()
        self.add_result_screen()
        self.operation_container.add_widget(self.section_screen)

    def _crear_pie(self):
        pie = BoxLayout(size_hint=(1, 0.05))
        back_button = Button(text='Volver al Menú', on_release=self.volver_al_menu)
        result_button = Button(text='Resultados', on_release=self.modo_resultados)
        pie.add_widget(back_button)
        pie.add_widget(result_button)
        return pie

    def _decorar_fondo(self, widget, color_cmd, attr):
        with widget.canvas.before:
            color_cmd
            setattr(self, attr, RoundedRectangle(size=widget.size, pos=widget.pos, radius=[20]))
        widget.bind(size=self._make_update(attr), pos=self._make_update(attr))

    def _make_update(self, attr):
        def updater(*args):
            rect = getattr(self, attr)
            widget = args[0]
            rect.size = widget.size
            rect.pos = widget.pos
        return updater

    def volver_al_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def add_edition_screen(self):
        edition_screen = Screen(name='edition')
        edition_screen.add_widget(Num_buttons(self))
        self.section_screen.add_widget(edition_screen)

    def add_result_screen(self):
        result_screen = Screen(name='resultados')
        result_screen.add_widget(Label(text='Resultados de la operación'))
        self.section_screen.add_widget(result_screen)

    def modo_edicion(self, instance):
        self.section_screen.current = 'edition'
        self.section_screen.transition.direction = 'right'

    def modo_resultados(self, instance):
        self.section_screen.current = 'resultados'
        self.section_screen.transition.direction = 'left'

    def switch_matrix(self, name):
        self.current_matrix = name
        self.current_index = 0

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def obtener_matriz(self, matriz_name):
        matriz = []
        if matriz_name == 'A':
            labels = self.matrix_A_labels
        elif matriz_name == 'B':
            labels = self.matrix_B_labels
        else:
            return []

        for i in range(0, len(labels), 3):
            fila = []
            for j in range(3):
                try:
                    valor = float(labels[i + j].text)
                except ValueError:
                    valor = 0  # Valor por defecto si hay error
                fila.append(valor)
            matriz.append(fila)
        return matriz

    def ejecutar_operacion(self):
        A = self.obtener_matriz('A')
        B = self.obtener_matriz('B')

        
        try:
            if self.operacion_actual == 'suma':
                resultado = sumar_matrices(A, B)
            else:
                resultado = None

            if resultado:
                self.mostrar_resultado(resultado)
        except Exception as e:
            print(f"Error en operación: {e}")

    def mostrar_resultado(self, matriz_resultado):
        layout = self.matrix_answer_output
        layout.clear_widgets()

        layout.rows = len(matriz_resultado)
        layout.cols = len(matriz_resultado[0]) if matriz_resultado else 0

        for fila in matriz_resultado:
            for valor in fila:
                etiqueta = Label(text=str(valor), halign='center', valign='middle')
                etiqueta.bind(size=etiqueta.setter('text_size'))
                layout.add_widget(etiqueta)

class Num_buttons(BoxLayout):
    def __init__(self, parent_screen, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.parent_screen = parent_screen
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Teclado dividido en filas
        layout = GridLayout(cols=4, spacing=5, padding=5)
        botones = [
            ('1', self.agregar_numero), ('2', self.agregar_numero), ('3', self.agregar_numero), ('->', self.apuntador_derecha),
            ('4', self.agregar_numero), ('5', self.agregar_numero), ('6', self.agregar_numero), ('<-', self.apuntador_izquierda),
            ('7', self.agregar_numero), ('8', self.agregar_numero), ('9', self.agregar_numero), ('±', self.cambio_signo),
            ('0', self.agregar_numero), ('.', self.agregar_punto), ('C', self.borrar), ('=', self.apuntador_igual),
        ]

        for texto, accion in botones:
            layout.add_widget(Button(
                text=texto,
                on_release=accion
            ))

        self.add_widget(layout)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def _get_current_label(self):
        labels = (self.parent_screen.matrix_A_labels if self.parent_screen.current_matrix == 'A'
                else self.parent_screen.matrix_B_labels)
        return labels[self.parent_screen.current_index]

    def _resaltar_label(self):
        labels = (self.parent_screen.matrix_A_labels if self.parent_screen.current_matrix == 'A'
                else self.parent_screen.matrix_B_labels)
        for i, label in enumerate(labels):
            if i == self.parent_screen.current_index:
                label.color = (1, 0, 0, 1)  # rojo para celda activa
                label.bold = True
            else:
                label.color = (0, 0, 0, 1)  # negro
                label.bold = False

    def agregar_numero(self, instance):
        current = self.get_current_input()
        if current.text == "0":
            current.text = instance.text
        else:
            current.text += instance.text

    def agregar_punto(self, instance):
        current = self.get_current_input()
        if '.' not in current.text:
            current.text += '.'

    def borrar(self, instance):
        current = self.get_current_input()
        current.text = '0'

    def cambio_signo(self, instance):
        current = self.get_current_input()
        try:
            val = float(current.text)
            current.text = str(-val)
        except ValueError:
            pass

    def apuntador_derecha(self, instance):
        if self.parent_screen.current_index < 8:
            self.parent_screen.current_index += 1

    def apuntador_izquierda(self, instance):
        if self.parent_screen.current_index > 0:
            self.parent_screen.current_index -= 1

    def apuntador_igual(self, instance):
        self.parent_screen.ejecutar_operacion()

    def get_current_input(self):
        if self.parent_screen.current_matrix == 'A':
            return self.parent_screen.matrix_A_labels[self.parent_screen.current_index]
        else:
            return self.parent_screen.matrix_B_labels[self.parent_screen.current_index]
