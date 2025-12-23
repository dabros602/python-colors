class ColorString(str):
    def __init__(self, string):
        self.UNFORMATTED = "\033[0m"
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"

    def black(self):
        return f"{self.BLACK}{self}{self.UNFORMATTED}"

    def red(self):
        return f"{self.RED}{self}{self.UNFORMATTED}"

    def green(self):
        return f"{self.GREEN}{self}{self.UNFORMATTED}"

    def yellow(self):
        return f"{self.YELLOW}{self}{self.UNFORMATTED}"

    def blue(self):
        return f"{self.BLUE}{self}{self.UNFORMATTED}"

    def magenta(self):
        return f"{self.MAGENTA}{self}{self.UNFORMATTED}"

    def cyan(self):
        return f"{self.CYAN}{self}{self.UNFORMATTED}"

    def white(self):
        return f"{self.WHITE}{self}{self.UNFORMATTED}"


class ColorString8Bit(str):
    def color(self, color):
        return f"\x1b[38;5;{color}m{self}\x1b[0m"


class RGBString(str):
    def color(self, r, g, b):
        return f"\x1b[38;2;{r};{g};{b}m{self}\x1b[0m"