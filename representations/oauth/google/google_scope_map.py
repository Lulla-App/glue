from collections.abc import Mapping
from .constants import GoogleScope, GoogleScopeURI


class GoogleScopeMap(Mapping):
    def __init__(self):
        self.mapping: Mapping[GoogleScopeURI, set[GoogleScope]] = {
            uri: set() for uri in GoogleScopeURI
        }

    def __getitem__(self, key: GoogleScopeURI) -> set[GoogleScope]:
        if not isinstance(key, GoogleScopeURI):
            raise TypeError(f"The key is not of the proper type")
        return self.mapping[key]

    def __iter__(self):
        return iter(self.mapping)

    def __len__(self):
        return len(self.mapping)

    def add(self, scope: GoogleScope, uris: set[GoogleScopeURI] = None):
        if uris == None and len(scope.uris) > 1:
            raise ValueError(
                f"because {scope} this multiple potential uris, so you need to specify one"
            )
        if (
            uris != None
            and not isinstance(uris, set)
            and not all(isinstance(uri, GoogleScopeURI) for uri in uris)
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

    def remove(self, scope: GoogleScope, uris: set[GoogleScopeURI] = None):
        if uris == None and len(scope.uris) > 1:
            raise ValueError(
                f"because {scope} this multiple potential uris, so you need to specify one"
            )
        if (
            uris != None
            and isinstance(uris, set)
            and all(isinstance(uri, GoogleScopeURI) for uri in uris)
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
