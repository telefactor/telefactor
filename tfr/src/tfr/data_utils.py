import re
import time


def name_to_id(name, pre="g"):
    cleaned = (
        Subber(name.lower())
        .sub(r"^\W+", "")
        .sub(r"\W+$", '')
        .sub(r"\W+", " ")
        .sub(r"\s+", "-")
        .string
    )
    timestamp = time.time()
    return f"{pre}:{cleaned}:{timestamp:.0f}"


def subber(string):
    return Subber(string)


class Subber:
    def __init__(self, string):
        self.string = string

    def sub(self, pattern, repl):
        self.string = re.sub(pattern, repl, self.string)
        return self

    def __str__(self):
        return self.string
