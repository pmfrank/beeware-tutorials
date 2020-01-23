"""
An attempt to make a variable amount of buttons that do different things
"""
import toga
import functools
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ButtonList(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(
            style=Pack(
                direction=COLUMN
            )
        )

        buttons = dict()
        stuff = ['item1','item2','item3','item4','item5']

        for s in stuff:
            buttons[s] = toga.Button(
                    s,
                    id = s,
                    style=Pack(
                        padding = 5
                    ),
                    on_press = functools.partial(self.button_press, s) # Use partial function evaluation to get different response from each button
                )
                main_box.add(buttons[s])
            )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_press(self, widget, info):
        print(info.id)
        # This function will use Class level functions and variables to manipulate what the data does


def main():
    return ButtonList()
