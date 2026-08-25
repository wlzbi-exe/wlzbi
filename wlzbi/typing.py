import sys
import time
import shutil

_DEFAULT_SPEED = 0.05
_DEFAULT_COLOR = None
_DEFAULT_ALIGN = "left"

_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}

_BOLD_COLORS = {
    f"bold{name}": code for name, code in _COLORS.items()
}


class Type:
    def __init__(self, text):
        self.text = str(text)
        self._align = _DEFAULT_ALIGN
        self._color = _DEFAULT_COLOR
        self._speed = _DEFAULT_SPEED

    def left(self, color=None, speed=None):
        self._align = "left"
        self._color = color
        if speed is not None:
            self._speed = speed
        return self._run()

    def right(self, color=None, speed=None):
        self._align = "right"
        self._color = color
        if speed is not None:
            self._speed = speed
        return self._run()

    def center(self, color=None, speed=None):
        self._align = "center"
        self._color = color
        if speed is not None:
            self._speed = speed
        return self._run()

    def centre(self, color=None, speed=None):
        return self.center(color, speed)

    def _get_color(self):
        if self._color is None:
            return ""

        color = str(self._color).lower()

        if color in _COLORS:
            return f"\033[{_COLORS[color]}m"

        if color in _BOLD_COLORS:
            return f"\033[1;{_BOLD_COLORS[color]}m"

        raise ValueError(
            f"Invalid color '{self._color}'. "
            f"Use: {', '.join(_COLORS)} or bold colors."
        )

    def _align_text(self, text):
        width = shutil.get_terminal_size().columns

        if self._align == "right":
            return text.rjust(width)

        if self._align == "center":
            return text.center(width)

        return text

    def _run(self):
        if self._speed < 0:
            raise ValueError("Speed cannot be negative.")

        color = self._get_color()
        reset = "\033[0m" if color else ""

        current = ""

        for char in self.text:
            current += char

            sys.stdout.write("\r")
            sys.stdout.write("\033[2K")
            sys.stdout.write(color + self._align_text(current) + reset)
            sys.stdout.flush()

            time.sleep(self._speed)

        sys.stdout.write("\n")
        sys.stdout.flush()

        return self


def type(text):
    return Type(text)