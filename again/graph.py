from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
import time


class CircularProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text="0%", font_size=self.thickness)

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:

            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
            Color(1, 0, 0)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized * 360))

            # Draw the inner circle (colour should be equal to the background)
            Color(0, 0, 0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            print('s', self.pos[0], self.thickness,
                  self.pos[1], self.thickness)
            # Center and draw the progress text
            Color(1, 0, 0)  # s 0 40 0 40

 # 200 73 200 48
            print('\n', self.size[0], self.texture_size[0],
                  self.size[1], self.texture_size[1])
            Rectangle(texture=self.label.texture, size=self.texture_size,
                      pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))

    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        time.sleep(0.01)
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = str(int(self.value_normalized * 100)) + "%"
        self.refresh_text()

        # Draw all the elements
        self.draw()


class Main(App):
    # Simple animation to show the circular progress bar in action
    def animate(self, dt):
        if self.root.value < 99:
            print(self.root.value)
            self.root.set_value(self.root.value + 1)
        else:
            print('jjjj')
    # Simple layout for easy example

    def build(self):
        container = Builder.load_string(
            '''CircularProgressBar:
    id:cp
    size_hint: (None, None)
    height: 200
    width: 200
    max: 100
    pos_hint:{'x':0.3,'y':0.2}
''')
        a = 1
        # Animate the progress bar
        # while(self.root.cp.value != 50):
        while a < 99:
            e = Clock.schedule_once(self.animate)
            a += 1
        e.cancel()
        return container


if __name__ == '__main__':
    Main().run()
