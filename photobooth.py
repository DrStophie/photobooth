import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_string("""

<CustomButton@Button>:
    font_size: 32
    color: 1, 1, 1, 1
    size: 500, 500
    background_normal: ''
    background_color: .22, .22, .22, 1
    size_hint: .75, .2

<ScreenOne>:
    BoxLayout:
        CustomButton:
            text: "Its PB&J time! Touch to start"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press:
                root.manager.current = "screen_two"
                root.manager.transition.direction = "up"
                root.manager.transition.duration = .75

<ScreenTwo>:
    BoxLayout:
        CustomButton:
            text: "Here's the countdown"
            pos_hint: {"center_x": .5, "bottom": .2}
            on_press:
                root.manager.current = "camera_flash"
                root.manager.transition.direction = "down"
                root.manager.transition.duration = 1
                
<CameraFlash>:
    BoxLayout:
        Label:
            text: "Here we go!"
            color: 1, 1, 1, 1
            size_hint_x: 1
            size_hint_y: 1
        

""")

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class CameraFlash(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(CameraFlash(name="camera_flash"))

class PhotoBooth(App):

    def build(self):
        return screen_manager

if __name__ == "__main__":
    Window.fullscreen = 'auto'
    PhotoBooth().run()