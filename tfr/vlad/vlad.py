import typing as t
import inspect as i

T = t.TypeVar("T")
Normer = t.NewType("Normer", t.Callable[[t.Mapping], T])


def normer(cls: T) -> t.Callable[[t.Mapping], T]:
    if not hasattr(cls, "__annotations__"):
        return cls

    def cls_normer(attr_dict):
        fields = {}
        for field, value in attr_dict.items():
            sub_normer = normer(cls.__annotations__[field])
            fields[field] = sub_normer(value)

        return cls(**fields)

    return cls_normer


def get_constructor(typ):
    return typing


def make(cls):
    def maker(d):
        return cls(**d)

    return maker
