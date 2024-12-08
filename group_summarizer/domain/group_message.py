from dataclasses import dataclass
from group_summarizer.domain.group_member import GroupMember

@dataclass
class GroupMessage:
    member: GroupMember
    content: str
    date: str
