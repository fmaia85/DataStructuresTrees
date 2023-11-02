
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.childLeft = None
        self.childRight = None
    #}__init__

    def print(self):
        print(f" {self.value} ")
        if self.childLeft is not None:
            self.childLeft.print()
        if self.childRight is not None:
            self.childRight.print()

    def __str__(self):
        s = f"{self.value}"
        if self.childLeft is not None or self.childRight is not None:
            s += "("
        if self.childLeft is not None:
            s += f"{self.childLeft}"
        if self.childLeft is not None and self.childRight is not None:
            s += ","
        if self.childRight is not None:
            s += f"{self.childRight}"
        if self.childLeft is not None or self.childRight is not None:
            s += ")"
        return s
    #}__str__

    def __repr__(self):
        return f"{self}"
    #}__repr__
#}class Node