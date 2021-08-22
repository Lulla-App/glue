from typing import Optional
from dataclasses import dataclass
from datetime import timedelta
from ..oauth_token import OAuthToken
from .constants import MicrosoftScope, MicrosoftScopeURI


@dataclass
class MicrosoftOAuthToken(OAuthToken[MicrosoftScopeURI, MicrosoftScope]):
    ext_expires_in: Optional[timedelta] = None
