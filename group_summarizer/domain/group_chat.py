from dataclasses import dataclass
from typing import List

from group_summarizer.domain.group_member import GroupMember

@dataclass
class GroupChat:
    name: str
    members: List[GroupMember]
