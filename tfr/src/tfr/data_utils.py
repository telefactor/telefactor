import re


def make_repo_name(
    app_name: str,
    phase_index: int,
) -> str:
    parts = [app_name, str(phase_index)]
    return ".".join(map(clean, parts))


def clean(name):
    return (
        Subber(name.lower())
        .sub(r"^\W+", "")
        .sub(r"\W+$", "")
        .sub(r"\W+", "-")
        .string
    )


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
