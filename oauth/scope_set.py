from typing import Optional, Generic, TypeVar
from dataclasses import dataclass, field, InitVar
from enum import Enum

RESOURCE_URI_ENUM = TypeVar("RESOURCE_URI_ENUM", Enum, Enum)
SCOPE_ENUM = TypeVar("SCOPE_ENUM", Enum, Enum)


@dataclass
class ScopeSet(Generic[RESOURCE_URI_ENUM, SCOPE_ENUM]):
    """A Class that tracks the scope data for a given transaction"""

    resource_uri: Optional[RESOURCE_URI_ENUM] = None
    # ^ this could be a union with an empty string
    scopes: set[SCOPE_ENUM] = field(default_factory=set)

    def to_string(self) -> str:
        string = []

        if self.resource_uri:
            string.append(self.resource_uri.value)

        string.append(" ".join([scope.value for scope in self.scopes]))

        return "".join(string)


"""
realistically this should be a dictionary mapping
scope uri's to scope sets.

scope enums should be based on uri
"""
