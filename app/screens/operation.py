'''
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
'''


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp, sp
from tabulate import tabulate
from kivy.properties import StringProperty


class ColorLabel(Label):
    def __init__(self, **kwargs):
        super(ColorLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.3)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MatrixLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MatrixLayout, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, 1)
        
        #TODO: Configuracion del apuntador
        self.labels = []
        
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        for data in range(9):
            label = ColorLabel(
                text=str(data),
                size_hint=(1, 1),
                color=(0, 0, 0, 1)
            )
            self.labels.append(label)
            self.add_widget(label)
        
    def _update_rect(self, *args):
        # Actualizar el tamaño y la posicion del rectangulo
        self.rect.pos = self.pos
        self.rect.size = self.size

class OperationScreen(Screen):
    def __init__(self, **kwargs):
        super(OperationScreen, self).__init__(**kwargs)

        
        #TODO: Codigo provisional para visualizacion de datos
        with self.canvas.before:
            Color(1,0,0,1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título de la pantalla
        title = Label(
            text='Operaciones con Matrices',
            size_hint=(1, 0.1),
            font_size='20sp',
            halign='center',
            valign='middle'
        )

        self.operation_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.8),
            padding=10,
            spacing=10
        )
        with self.operation_container.canvas.before:
            Color(1,1,0,1)
            self.rect3 = RoundedRectangle(
                size=self.operation_container.size,
                pos=self.operation_container.pos
            )
        self.operation_container.bind(size=self._update_rect3, pos=self._update_rect3)
        
        self.matrix_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(300),
            padding=10,
            spacing=10
        )
        with self.matrix_container.canvas.before:
            Color(0,1,1,1)
            self.rect2 = RoundedRectangle(size=self.matrix_container.size, pos=self.matrix_container.pos, radius=[20])
        self.matrix_container.bind(size=self._update_rect2, pos=self._update_rect2)
        
        
        #? Matriz Respuesta
        self.matrix_answer = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(140),
        )
        with self.matrix_answer.canvas.before:
            Color(0,1,0,1)
            self.rect_answer = RoundedRectangle(size=self.matrix_answer.size, pos=self.matrix_answer.pos, radius=[20])
        self.matrix_answer.bind(size=self._update_rect_answer, pos=self._update_rect_answer)

        matrix_answer_label = Label(
            text='Answer',
            size_hint=(1, 0.3),
            color=(0, 0, 0, 1)
        )
        
        matrix_answer_output = MatrixLayout()
        self.matrix_answer.add_widget(matrix_answer_label)
        self.matrix_answer.add_widget(matrix_answer_output)
        
        #TODO: Container para ambos botones
        self.input_matrix_container = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(50),
            padding=10,
            spacing=10
        )
        
        #? Matriz A
        self.matrix_A = BoxLayout(
            orientation='vertical',
            size_hint=(1,None),
            height=dp(110),
        )
        with self.matrix_A.canvas.before:
            Color(0,1,0,1)
            self.rectA = RoundedRectangle(size=self.matrix_A.size, pos=self.matrix_A.pos, radius=[20])
        self.matrix_A.bind(size=self._update_rectA, pos=self._update_rectA)
        
        self.matrix_A_label = Label(
            text='Matriz A',
            size_hint=(1, 0.3),
            color=(0, 0, 0, 1)
        )
        self.matrix_A_output = MatrixLayout()
        self.matrix_A_labels = self.matrix_A_output.labels
        self.current_matrix = 'A'
        self.current_index = 0
        
        self.matrix_A.add_widget(self.matrix_A_label)
        self.matrix_A.add_widget(self.matrix_A_output)
        self.input_matrix_container.add_widget(self.matrix_A)
        
        #? Matriz B
        self.matrix_B = BoxLayout(
            orientation='vertical',
            size_hint=(1,None),
            height=dp(110),
        )
        with self.matrix_B.canvas.before:
            Color(0,1,0,1)
            self.rectB = RoundedRectangle(size=self.matrix_B.size, pos=self.matrix_B.pos, radius=[20])
        self.matrix_B.bind(size=self._update_rectB, pos=self._update_rectB)

        self.matrix_B_label = Label(
            text='Matriz B',
            size_hint=(1, 0.3),
            color=(0, 0, 0, 1)
        )
        self.matrix_B_output = MatrixLayout()
        self.matrix_B_labels = self.matrix_B_output.labels
        
        self.matrix_B.add_widget(self.matrix_B_label)
        self.matrix_B.add_widget(self.matrix_B_output)
        self.input_matrix_container.add_widget(self.matrix_B)
        
        # TODO:  Agregarlo al contenedor principal
        self.matrix_container.add_widget(self.input_matrix_container)
        self.matrix_container.add_widget(self.matrix_answer)
        self.operation_container.add_widget(self.matrix_container)
        
        #! Botones para elegir entre editar y resoluciones
        self.button_container_ER = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.15),
            padding=10,
            spacing=10
        )
        with self.button_container_ER.canvas.before:
            Color(0,1,0,1)
            self.rect4 = RoundedRectangle(size=self.button_container_ER.size, pos=self.button_container_ER.pos, radius=[20])
        self.button_container_ER.bind(size=self._update_rect4, pos=self._update_rect4)
        
        edit_button = Button(
            text='Editar',
            size_hint=(0.5, 1),
            on_release=self.modo_edicion   #? Agregar esta funcion
        )
        edit_A = Button(
            text='A',
            size_hint=(0.5, 1),
            on_release=lambda btn: self.switch_matrix('A')
        )
        edit_B = Button(
            text='B',
            size_hint=(0.5, 1),
            on_release=lambda btn: self.switch_matrix('B')
        )
        edit_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 1)
        )
        edit_box.add_widget(edit_A)
        edit_box.add_widget(edit_B)
        
        self.button_container_ER.add_widget(edit_button)
        self.button_container_ER.add_widget(edit_box)
        
        # TODO:  Agregarlo al contenedor principal
        self.operation_container.add_widget(self.button_container_ER)
        
        #! Agregar el contenedor para Edicion o Resultados
        self.section_screen = ScreenManager()
        self.add_edition_screen()
        self.add_result_screen()
        self.operation_container.add_widget(self.section_screen)
        # Botón para volver al menú principal
        end_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.05),
        )
        back_button = Button(
            text='Volver al Menú',
            size_hint=(1, 1),
            on_release=self.volver_al_menu
        )
        result_button = Button(
            text='Resultados',
            size_hint=(0.5, 1),
            on_release=self.modo_resultados #? Agregar esta funcion
        )
        end_box.add_widget(back_button)
        end_box.add_widget(result_button)
        # Añadir todo al layout principal
        main_layout.add_widget(title)
        main_layout.add_widget(self.operation_container)
        main_layout.add_widget(end_box)

        self.add_widget(main_layout)

    def volver_al_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'
    
    def add_edition_screen(self):
        edition_screen = Screen(name='edition')
        self.num_pad = Num_buttons(self) 
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
    
    def switch_matrix(self, matrix_name):
        self.current_matrix = matrix_name
        self.current_index = 0
        self.num_pad._resaltar_label()

    def _update_rect(self, *args):
        # Actualizar el tamaño y la posicion del rectangulo
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def _update_rect2(self, *args):
        # Actualizar el tamaño y la posicion del rectangulo
        self.rect2.pos = self.matrix_container.pos
        self.rect2.size = self.matrix_container.size
    
    def _update_rect3(self, *args):
        self.rect3.pos = self.operation_container.pos
        self.rect3.size = self.operation_container.size
    
    def _update_rect4(self, *args):
        self.rect4.pos = self.button_container_ER.pos
        self.rect4.size = self.button_container_ER.size

    def _update_rectA(self, *args):
        self.rectA.pos = self.matrix_A.pos
        self.rectA.size = self.matrix_A.size

    def _update_rectB(self, *args):
        self.rectB.pos = self.matrix_B.pos
        self.rectB.size = self.matrix_B.size

    def _update_rect_answer(self, *args):
        self.rect_answer.pos = self.matrix_answer.pos
        self.rect_answer.size = self.matrix_answer.size

class Num_buttons(GridLayout):
    current_matrix = StringProperty("A")
    def __init__(self, parent_screen,**kwargs):
        super(Num_buttons, self).__init__(**kwargs)
        self.parent_screen = parent_screen
        
        self.cols = 4
        self.rows = 4
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, 1)
        
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

        #? Creando Botones
        button_1 = Button(
            text='1',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_2 = Button(
            text='2',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_3 = Button(
            text='3',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_right = Button(
            text='right',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.apuntador_derecha  #? Agregar esta funcion
        )
        button_4 = Button(
            text='4',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_5 = Button(
            text='5',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_6 = Button(
            text='6',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_left = Button(
            text='Left',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.apuntador_izquierda  #? Agregar esta funcion
        )
        button_7 = Button(
            text='7',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_8 = Button(
            text='8',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_9 = Button(
            text='9',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_equal = Button(
            text='=',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.apuntador_igual  #? Agregar esta funcion
        )
        button_0 = Button(
            text='0',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
                on_release=self.agregar_numero  #? Agregar esta funcion
        )
        button_dot = Button(
            text='.',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
                on_release=self.agregar_punto  #? Agregar esta funcion
        )
        button_sign = Button(
            text='+-',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
                on_release=self.cambio_signo  #? Agregar esta funcion
        )
        button_AC = Button(
            text='AC',
            size_hint=(0.25, 0.25),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.borrar #? Agregar esta funcion
        )
        #! Agregar botones
        self.add_widget(button_1)
        self.add_widget(button_2)
        self.add_widget(button_3)
        self.add_widget(button_right)
        self.add_widget(button_4)
        self.add_widget(button_5)
        self.add_widget(button_6)
        self.add_widget(button_left)
        self.add_widget(button_7)
        self.add_widget(button_8)
        self.add_widget(button_9)
        self.add_widget(button_equal)
        self.add_widget(button_0)
        self.add_widget(button_dot)
        self.add_widget(button_sign)
        self.add_widget(button_AC)

    # TODO: Métodos para cada botón
    def agregar_punto(self, instance):
        label = self._get_current_label()
        if '.' not in label.text:
            label.text += '.'

    def cambio_signo(self, instance):
        label = self._get_current_label()
        if label.text.startswith('-'):
            label.text = label.text[1:]
        else:
            label.text = '-' + label.text

    def agregar_numero(self, instance):
        numero = instance.text
        label = self._get_current_label()
        if label.text == "0":
            label.text = numero
        else:
            label.text += numero

    def apuntador_derecha(self, instance):
        self.parent_screen.current_index = (self.parent_screen.current_index + 1) % 9
        self._resaltar_label()

    def apuntador_izquierda(self, instance):
        self.parent_screen.current_index = (self.parent_screen.current_index - 1) % 9
        self._resaltar_label()

    def apuntador_igual(self, instance):
        print("Valor actual:", self._get_current_label().text)

    def borrar(self, instance):
        label = self._get_current_label()
        label.text = '0'

    def _get_current_label(self):
        labels = (self.parent_screen.matrix_A_labels if self.parent_screen.current_matrix == 'A'
                else self.parent_screen.matrix_B_labels)
        return labels[self.parent_screen.current_index]

    def _resaltar_label(self):
        labels = (self.parent_screen.matrix_A_labels if self.parent_screen.current_matrix == 'A'
                else self.parent_screen.matrix_B_labels)
        for i, label in enumerate(labels):
            label.color = (1, 0, 0, 1) if i == self.parent_screen.current_index else (0, 0, 0, 1)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
