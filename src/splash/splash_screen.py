from textual.app import ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from textual.widgets import Static, Footer

class SplashScreen(Screen):
    """The splash screen"""

    CSS_PATH="splash_screen.tcss"

    def compose(self) -> ComposeResult:
        yield Static(r" /$$   /$$                                           /$$     /$$          ", classes="display-text")
        yield Static(r"| $$$ | $$                                          | $$    |__/          ", classes="display-text")
        yield Static(r"| $$$$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$   /$$  /$$$$$$$", classes="display-text")
        yield Static(r"| $$ $$ $$ /$$__  $$| $$  | $$ /$$__  $$ /$$__  $$|_  $$_/  | $$ /$$_____/", classes="display-text")
        yield Static(r"| $$  $$$$| $$$$$$$$| $$  | $$| $$  \__/| $$  \ $$  | $$    | $$| $$      ", classes="display-text")
        yield Static(r"| $$\  $$$| $$_____/| $$  | $$| $$      | $$  | $$  | $$ /$$| $$| $$      ", classes="display-text")
        yield Static(r"| $$ \  $$|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$|  $$$$$$$", classes="display-text")
        yield Static(r"|__/  \__/ \_______/ \______/ |__/       \______/    \___/  |__/ \_______/", classes="display-text")
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "tokyo-night"

