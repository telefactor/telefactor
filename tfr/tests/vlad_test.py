# import pyteset
from typing import NamedTuple

from cerberus import Validator

from tfr import vlad


class TestSimple:
    class Simple(NamedTuple):
        a: str
        b: int

    simple_data = {"a": "ayy", "b": 420}

    def test_cerb(self):
        validator = Validator({"simple": {"coerce": [vlad.make(self.Simple)]}})

        result = validator.normalized({"simple": self.simple_data})
        print("result", result)
        simple = result["simple"]

        assert simple.a == "ayy"
        assert simple.b == 420

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

    nested_data = {
        "a": {
            "aa": "ayy"
        },
        "b": {
            "bb": 420
        }
    }

    def test_cerb(self):
        validator = Validator({
            "nested": {
                "coerce": [
                    Validator({
                        "a": {
                            "coerce": [
                                vlad.make(self.Nested.A)
                            ]
                        },
                        "b": {
                            "coerce": [
                                vlad.make(self.Nested.B)
                            ]
                        }
                    }).normalized,
                    vlad.make(self.Nested)
                ]
            }})

        result = validator.normalized({"nested": self.nested_data})
        print("validation", validator.errors)
        print("result", result)
        nested = result["nested"]

        assert nested.a.aa == "ayy"
        assert nested.b.bb == 420

    def test_normer(self):
        normer = vlad.normer(self.Nested)
        nested = normer(self.nested_data)

        assert nested.a.aa == "ayy"
        assert nested.b.bb == 420
