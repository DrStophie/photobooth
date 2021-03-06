from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window

smile_prompt = ['Get ready', 'Smile for the camera', 'Lookin good', 'Crazy eyes!', 'Wild card',
               'Sexy time', 'Strike a pose', 'Go vogue', 'Good one! Now give me tiger',
               'Bottoms up', 'Say cheese', 'Party mode', 'Its go time', 'Thriller mode',
               'Shum Shlum Shlipiddy Dop!']

capture_state = [
    {'state': 'first_shot', 'time': 6},
    {'state': 'additional_shot', 'time': 5},
    {'state': 'second additional_shot', 'time': 5},
    {'state': 'Good Job', 'time': 5},
    {'state': 'prompt for number of copies', 'time': 5},
    {'state': 'Printing', 'time': 2},
]


Builder.load_string("""
#:import time time
#:import capture_state __main__.capture_state
#:import smile_prompt __main__.smile_prompt

<Capture>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.state
        Label:
            text: time.strftime('%-S', time.gmtime(root.remaining))
        Button:
            text: "click me to take a pic"
            on_release: root.start_session(capture_state)
""")

class Capture(BoxLayout):
    random_smile_prompt = ListProperty()
    state = StringProperty('idle')
    remaining = NumericProperty()

    def start_session(self, session):
        if self.state != 'idle':
                Clock.unschedule(self._countdown)
        self.random_smile_prompt = session[:]
        self._progress_session()

    def _progress_session(self):
        # retrieve the first state in the current session
        try:
            item = self.random_smile_prompt.pop(0)
        # session complete, return to idle state
        except IndexError:
            self.state = 'idle'
            self.remaining = 0
            return
        # copy data for Labels update and countdown by one second
        self.state = item['state']
        self.remaining = item['time']
        Clock.schedule_once(self._countdown, 1)

    def _countdown(self, *largs):
        self.remaining -= 1
        if self.remaining <= 0:
            # proceed to next session
            self._progress_session()
        else:
            Clock.schedule_once(self._countdown, 1)


class PhotoboothApp(App):
    def build(self):
        return Capture()
Window.fullscreen = 'auto'
PhotoboothApp().run()