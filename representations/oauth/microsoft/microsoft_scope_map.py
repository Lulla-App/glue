from collections.abc import Mapping, Iterable
from typing import Optional
from .constants import MicrosoftScope, MicrosoftScopeURI


class MicrosoftScopeMap(Mapping[MicrosoftScopeURI, set[MicrosoftScope]]):
    def __init__(self):
        self.mapping: Mapping[MicrosoftScopeURI, set[MicrosoftScope]] = {
            uri: set() for uri in MicrosoftScopeURI
        }

    def __getitem__(self, key: MicrosoftScopeURI) -> set[MicrosoftScope]:
        if not isinstance(key, MicrosoftScopeURI):
            raise TypeError(f"The key is not of the proper type")
        return self.mapping[key]

    def __iter__(self):
        return iter(self.mapping)

    def __len__(self):
        return len(self.mapping)

    def add(self, scope: MicrosoftScope, uris: set[MicrosoftScopeURI] = None):
        if uris == None and len(scope.uris) > 1:
            raise ValueError(
                f"because {scope} this multiple potential uris, so you need to specify one"
            )
        if (
            uris != None
            and isinstance(uris, set)
            and all(isinstance(uri, MicrosoftScopeURI) for uri in uris)
        ):
            raise TypeError("parameter uris is not of the proper type")
        if uris != None and all(uri not in scope.uris for uri in uris): # I'm not sure about this one
            raise ValueError(
                f"{scope.value} is not usable by one or more of the uris you're trying to use it with"
            )

        if uris == None:
            self.mapping[list(scope.uris)[0]].add(scope)
            return

        for uri in uris:
            self.mapping[uri].add(scope)

    def remove(self, scope: MicrosoftScope, uris: set[MicrosoftScopeURI] = None):
        if uris == None and len(scope.uris) > 1:
            raise ValueError(
                f"because {scope} this multiple potential uris, so you need to specify one"
            )
        if (
            uris != None
            and not isinstance(uris, set)
            and not all(isinstance(uri, MicrosoftScopeURI) for uri in uris)
        ):
            raise TypeError("parameter uris is not of the proper type")
        if uris != None and all(uri not in scope.uris for uri in uris):
            raise ValueError(
                f"{scope.value} is not usable by one or more of the uris you're trying to use it with"
            )

        if uris == None:
            self.mapping[list(scope.uris)[0]].remove(scope)
            return

        for uri in uris:
            self.mapping[uri].remove(scope)
