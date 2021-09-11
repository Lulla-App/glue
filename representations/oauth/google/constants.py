from enum import Enum, unique


@unique
class GoogleScopeURI(Enum):
    GOOGLE_APIS = "https://www.googleapis.com/auth/"


@unique
class GoogleScope(Enum):
    def __new__(cls, value, uri_set):
        # TEMP SOLUTION
        obj = object.__new__(cls)
        obj._value_ = value
        obj.uris: set[GoogleScopeURI] = uri_set
        return obj

    CALENDAR = "calendar", set([GoogleScopeURI.GOOGLE_APIS])
    CALENDAR_EVENTS = "calendar.events", set([GoogleScopeURI.GOOGLE_APIS])
