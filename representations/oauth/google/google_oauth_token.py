from typing import Optional
from dataclasses import dataclass, field
from datetime import timedelta, datetime

from .. import TokenType
from .google_scope_map import GoogleScopeMap


@dataclass
class GoogleOAuthToken:
    access_token: str
    refresh_token: str
    token_type: TokenType
    expires_in: timedelta
    scopes: GoogleScopeMap = field(default_factory=GoogleScopeMap)

    created_on: datetime = field(default_factory=datetime.utcnow)
