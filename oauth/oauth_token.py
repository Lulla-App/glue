from typing import Optional, TypeVar, Union, Generic
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from .scope_set import ScopeSet
from .token_type import TokenType
from enum import Enum

RESOURCE_URI_ENUM = TypeVar("RESOURCE_URI_ENUM", Enum, Enum)
SCOPE_ENUM = TypeVar("SCOPE_ENUM", Enum, Enum)


@dataclass
class OAuthToken(Generic[RESOURCE_URI_ENUM, SCOPE_ENUM]):
    access_token: str
    refresh_token: str
    token_type: TokenType
    expires_in: Optional[timedelta] = None
    scopes: Union[ScopeSet[RESOURCE_URI_ENUM, SCOPE_ENUM], None] = None

    created_on: datetime = field(default_factory=datetime.utcnow)  # something I defined
