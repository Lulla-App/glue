from typing import Optional
from dataclasses import dataclass, field
from datetime import timedelta, datetime

from .. import TokenType
from .constants import MicrosoftScope, MicrosoftScopeURI
from .microsoft_scope_map import MicrosoftScopeMap


@dataclass
class MicrosoftOAuthToken:
    access_token: str
    refresh_token: str
    token_type: TokenType
    expires_in: Optional[timedelta] = None
    scopes: MicrosoftScopeMap = field(default_factory=MicrosoftScopeMap)

    ext_expires_in: Optional[timedelta] = None

    created_on: datetime = field(default_factory=datetime.utcnow)
