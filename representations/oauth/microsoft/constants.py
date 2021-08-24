from enum import Enum, unique


@unique
class MicrosoftScopeURI(Enum):
    """An Enum containing all the scope uri we support fron microsoft"""

    MS_GRAPH = "https://graph.microsoft.com/"


@unique
class MicrosoftScope(Enum):
    """An Enum containing all the scopes we support in microsoft's api"""

    def __new__(cls, value, uri_set):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.uris: set[MicrosoftScopeURI] = uri_set
        # ^ I think this can be written in a way where it's better communicated
        # ^ I want to add proper error raising here
        return obj

    USER_READ = "User.Read", set([MicrosoftScopeURI.MS_GRAPH])
    TASK_READ_WRITE = "Tasks.ReadWrite", set([MicrosoftScopeURI.MS_GRAPH])
    OFFLINE_ACCESS = "offline_access", set([MicrosoftScopeURI.MS_GRAPH])
