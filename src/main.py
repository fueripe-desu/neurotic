from typing import Iterable
from textual.app import App, SystemCommand
from textual.binding import Binding
from textual.screen import Screen
from splash.splash_screen import SplashScreen

class NeuroticApp(App):
    """The main class for Neurotic memory management."""

    SCREENS = { "splash": SplashScreen }
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit")
    ]

    def push_deck_screen():
        pass

    def on_mount(self) -> None:
        self.push_screen("splash");

    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)
        yield SystemCommand(
            title="Create deck", 
            help="Creates a new collection of cards (deck).",
            callback=self.push_deck_screen
        )

if __name__ == "__main__":
    app = NeuroticApp()
    app.run()

