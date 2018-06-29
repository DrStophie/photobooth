from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.lang import Builder

smile_prompt = ['Get ready', 'Smile for the camera', 'Lookin good', 'Crazy eyes!', 'Wild card',
               'Sexy time', 'Strike a pose', 'Go vogue', 'Good one! Now give me tiger',
               'Bottoms up', 'Say cheese', 'Party mode', 'Its go time', 'Thriller mode',
               'Shum Shlum Shlipiddy Dop!']

capture_state = [
    {'state': 'first_shot', 'time': 7},
    {'state': 'additional_shot', 'time': 5},
]


Builder.load_string("""

#import clock
#import smile_prompt __main__.smile_prompt

<Capture>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.state
        Label:
            text: time.strftime('%H:%M:%S', time.gmtime(root.remaining))
        Button:
            text: "click me to take a pic"
            on_release: root.start_session(capture_state)
""")

class Capture(BoxLayout):
    random_smile_prompt = ListProperty()
    state = StringProperty('idle')
    remaining = NumericProperty()

    def start session(self, session):
        if self.state != 'idle':
                Clock.unschedule(self._countdown)
        self.capture_session = session[:]
        self._progress_session()

    def _progress_session(self):
        # retrieve the first state in the current session
        try:
            item = self.workout_session.pop(0)
        # session complete, return to idle state
        except IndexError:
            self.state = 'idle'
            self.remaining = 0
            return
        # copy data for Labels update and countdown by one second
        self.state = item['state']
        self.remaining = item['time']
        Clock.schedule_once(self._countdown, 1)

    def _countdown(slef, *largs):
        self.remaining -= 1
        if self.remaining <= 0:
            # proceed to next session
            self._progress_session()
        else:
            Clock.scheudle_once(self._countdown, 1)


class PhotoboothApp(App):

    def build(self):
        return Capture

PhotoboothApp().run()