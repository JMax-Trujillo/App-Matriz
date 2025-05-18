# import os
# video_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'login.mp4')
# video_path = os.path.abspath(video_path)
# from kivy.uix.screenmanager import Screen
# from kivy.config import Config
# Config.set('graphics', 'width', '360')
# Config.set('graphics', 'height', '640')
# Config.set('graphics', 'resizable', '0')

# # from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.video import Video
# from kivy.core.video import Video as CoreVideo
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.graphics import Color, RoundedRectangle
# from kivy.core.video.video_ffpyplayer import VideoFFPy
# # from kivy.lang import Builder
# # Builder.load_file("app/ui/home.kv")


# CoreVideo.provider = 'ffpyplayer'

# class RoundedBox(FloatLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas.before:
#             Color(1, 1, 1, 0.3)
#             self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
#         self.bind(size=self._update_rect, pos=self._update_rect)

#     def _update_rect(self, *args):
#         self.rect.size = self.size
#         self.rect.pos = self.pos

# class RoundedTextInput(TextInput):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas.before:
#             Color(1, 1, 1, 0.5)
#             self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
#         self.background_color = (0, 0, 0, 0)
#         self.foreground_color = (0, 0, 0, 1)
#         self.hint_text_color = (0.3, 0.3, 0.3, 1)
#         self.padding = [10, 10, 10, 10]
#         self.bind(size=self._update_rect, pos=self._update_rect)

#     def _update_rect(self, *args):
#         self.rect.size = self.size
#         self.rect.pos = self.pos

# class HomeScreen(Screen):
#     def __init__(self, **kw):
#         super().__init__(**kw)

#         layout = FloatLayout()

#         video = Video(source=video_path,
#                       state='play',
#                       options={'eos': 'loop'},
#                       volume=0,
#                       allow_stretch=True,
#                       keep_ratio=False,
#                       size_hint=(1, 1),
#                       pos_hint={'x': 0, 'y': 0})
#         layout.add_widget(video)

#         login_card = RoundedBox(
#             size_hint=(0.7, 0.45),
#             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#         )

#         form_layout = BoxLayout(
#             orientation='vertical',
#             spacing=12,
#             padding=[20, 20, 20, 20],
#             size_hint=(1, 1),
#             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#         )

#         title = Label(
#             text="Login",
#             font_size=24,
#             bold=True,
#             color=(0, 0, 0, 1),
#             size_hint=(1, None),
#             height=30
#         )
#         form_layout.add_widget(title)

#         username = RoundedTextInput(
#             hint_text="Username",
#             size_hint=(1, None),
#             height=40,
#             multiline=False
#         )
#         form_layout.add_widget(username)

#         password = RoundedTextInput(
#             hint_text="Password",
#             password=True,
#             size_hint=(1, None),
#             height=40,
#             multiline=False
#         )
#         form_layout.add_widget(password)

#         login_button = Button(
#             text="Log in",
#             size_hint=(1, None),
#             height=40,
#             background_color=(0.0, 0.4, 1.0, 1),
#             color=(1, 1, 1, 1)
#         )
#         form_layout.add_widget(login_button)

#         login_card.add_widget(form_layout)
#         layout.add_widget(login_card)

#         self.add_widget(layout)




# buttons={
#             'Suma': (0.1, 0.5, 0.5, 0.3),
#             'Resta': (0.1, 0.5, 0.5, 0.3),
#             'Multiplicacion': (0.1, 0.5, 0.5, 0.3),
#             'Determinante': (0.1, 0.5, 0.5, 0.3),
#             'Traspuesta': (0.1, 0.5, 0.5, 0.3),
#             'Inversa': (0.1, 0.5, 0.5, 0.3),
#         }

# for i in buttons:
#     print(i)
#     print(buttons[i])

print("Gelkasd")