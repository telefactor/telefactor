# import pyteset
from typing import NamedTuple

from tfr import vlad


class TestSimple:
    class Simple(NamedTuple):
        a: str
        b: int

    simple_data = {"a": "ayy", "b": 420}

    def test_normer(self):
        normer = vlad.normer(self.Simple)
        simple = normer(self.simple_data)

        assert simple.a == "ayy"
        assert simple.b == 420


class TestNested:
    class Nested(NamedTuple):
        class A(NamedTuple):
            aa: str

        class B(NamedTuple):
            bb: int

        a: A
        b: B

    nested_data = {"a": {"aa": "ayy"}, "b": {"bb": 420}}

    def test_normer(self):
        normer = vlad.normer(self.Nested)
        nested = normer(self.nested_data)

        assert nested.a.aa == "ayy"
        assert nested.b.bb == 420
