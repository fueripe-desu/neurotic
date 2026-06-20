from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header

class NeuroticApp(App):
    """The main class for Neurotic memory management."""

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Neurotic"
        self.theme = "tokyo-night"

if __name__ == "__main__":
    app = NeuroticApp()
    app.run()

