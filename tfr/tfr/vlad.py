from typing import Callable, Mapping, NewType, TypeVar

from cerberus import Validator

def make(cls):
    def maker(d):
        return cls(**d)

    return maker

# Normer = NewTypeCallable[Mapping, ]
T = TypeVar('T') 
def normer(cls: T) -> Callable[[Mapping], T]:
    schema = normalizer_schema(cls)
    validator = Validator({
        "cls": schema
    })
    def cls_normer(document):
        return validator.normalized(document) 

    return cls_normer

def normalizer_schema(cls):
    if cls.hasattr('_field_types'):
        sub_coercers = coercers_for_field_types(cls)
    else:
        sub_coercers = []

    coercers = sub_coercers + [make(cls)]
    schema = {
        "type": cls,
        "coerce": coercers
    }

def coercers_for_field_types(cls):
    return []
