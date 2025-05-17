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

class OperationScreen(Screen):
    pass