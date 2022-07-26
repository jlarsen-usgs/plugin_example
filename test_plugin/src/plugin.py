

class FancyHelloWord():
    def __init__(self):
        self.str = "@@!! Hello World !!@@"

    def display(self):
        print(self.str)


def plugin():
    return FancyHelloWord