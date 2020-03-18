from typing import Callable, Mapping, NewType, TypeVar


def make(cls):
    def maker(d):
        return cls(**d)

    return maker


T = TypeVar("T")
Normer = NewType("Normer", Callable[[Mapping], T])


def normer(cls: T) -> Callable[[Mapping], T]:
    if not hasattr(cls, "_field_types"):
        return cls

    def cls_normer(attr_dict):
        fields = {}
        for field, value in attr_dict.items():
            sub_normer = normer(cls._field_types[field])
            fields[field] = sub_normer(value)

        return cls(**fields)

    return cls_normer
