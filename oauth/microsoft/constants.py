from enum import Enum, unique


@unique
class MicrosoftScope(Enum):
    """An Enum containing all the scopes we support in microsoft's api"""

    USER_READ = "User.Read"
    TASK_READ_WRITE = "Tasks.ReadWrite"
    OFFLINE_ACCESS = "offline_access"


@unique
class MicrosoftScopeURI(Enum):
    """An Enum containing all the scope uri we support fron microsoft"""

    MS_GRAPH = "https://graph.microsoft.com/"
