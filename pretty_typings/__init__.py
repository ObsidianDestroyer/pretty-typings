from typing import Any, Dict, TypeVar, Union

Integer = TypeVar('Integer', bound=int)
String = TypeVar('String', bound=str)
Bool = TypeVar('Bool', bound=bool)
Float = TypeVar('Float', bound=float)

DictStrAny = Dict[String, Any]
StringifiedInt = Union[String, Integer]
StringifiedBool = Union[String, Bool]
StringifiedAny = Union[String, Any]

ClassObject = TypeVar('ClassObject', bound=object)
