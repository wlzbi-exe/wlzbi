import random
from cfonts import render
from colorama import init

init(autoreset=True)

COLOR_COMBOS = [
    ["green", "yellow"],
    ["magenta", "red"],
    ["blue", "cyan"],
    ["white", "gray"],
    ["red", "magenta"],
    ["yellow", "green"],
    ["cyan", "green"],
    ["blue", "magenta"],
    ["yellow", "red"],
    ["cyan", "yellow"],
    ["green", "blue"],
    ["magenta", "yellow"],
    ["red", "blue"],
    ["white", "cyan"],
    ["gray", "magenta"],
    ["green", "red"],
    ["blue", "yellow"],
    ["cyan", "red"],
    ["white", "green"],
    ["magenta", "cyan"],
    ["red", "yellow"],
    ["green", "cyan"],
    ["blue", "green"],
]


class Logo:
    def __init__(self, text, subtitle=""):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if not isinstance(subtitle, str):
            raise TypeError("subtitle must be a string")

        self.text = text
        self.subtitle = subtitle
        self.align = "right"

    def left(self):
        self.align = "left"
        return self

    def right(self):
        self.align = "right"
        return self

    def center(self):
        self.align = "center"
        return self

    def centre(self):
        self.align = "center"
        return self

    def _print(self):
        logo_colors, subtitle_colors = random.sample(COLOR_COMBOS, 2)

        main = render(
            self.text,
            colors=logo_colors,
            align="center",
            font="block",
            background="black",
        )

        print(main, end="")

        if self.subtitle:
            subtitle = render(
                self.subtitle,
                colors=subtitle_colors,
                align=self.align,
                font="console",
                background="black",
            )

            print(subtitle, end="")

    def __del__(self):
        try:
            self._print()
        except Exception:
            pass


def logo(text, subtitle=""):
    return Logo(text, subtitle)