from textual.app import App
from textual.binding import Binding
from splash.splash_screen import SplashScreen

class NeuroticApp(App):
    """The main class for Neurotic memory management."""

    SCREENS = { "splash": SplashScreen }
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit")
    ]

    def on_mount(self) -> None:
        self.push_screen("splash");

if __name__ == "__main__":
    app = NeuroticApp()
    app.run()

