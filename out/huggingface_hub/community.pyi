from . import constants as constants
from .utils import parse_datetime as parse_datetime
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime

DiscussionStatus: Incomplete

@dataclass
class Discussion:
    title: str
    status: DiscussionStatus
    num: int
    repo_id: str
    repo_type: str
    author: str
    is_pull_request: bool
    created_at: datetime
    endpoint: str
    @property
    def git_reference(self) -> str | None: ...
    @property
    def url(self) -> str: ...
    def __init__(self, title, status, num, repo_id, repo_type, author, is_pull_request, created_at, endpoint) -> None: ...

@dataclass
class DiscussionWithDetails(Discussion):
    events: list['DiscussionEvent']
    conflicting_files: list[str] | bool | None
    target_branch: str | None
    merge_commit_oid: str | None
    diff: str | None
    def __init__(self, title, status, num, repo_id, repo_type, author, is_pull_request, created_at, endpoint, events, conflicting_files, target_branch, merge_commit_oid, diff) -> None: ...

@dataclass
class DiscussionEvent:
    id: str
    type: str
    created_at: datetime
    author: str
    def __init__(self, id, type, created_at, author, _event) -> None: ...

@dataclass
class DiscussionComment(DiscussionEvent):
    content: str
    edited: bool
    hidden: bool
    @property
    def rendered(self) -> str: ...
    @property
    def last_edited_at(self) -> datetime: ...
    @property
    def last_edited_by(self) -> str: ...
    @property
    def edit_history(self) -> list[dict]: ...
    @property
    def number_of_edits(self) -> int: ...
    def __init__(self, id, type, created_at, author, _event, content, edited, hidden) -> None: ...

@dataclass
class DiscussionStatusChange(DiscussionEvent):
    new_status: str
    def __init__(self, id, type, created_at, author, _event, new_status) -> None: ...

@dataclass
class DiscussionCommit(DiscussionEvent):
    summary: str
    oid: str
    def __init__(self, id, type, created_at, author, _event, summary, oid) -> None: ...

@dataclass
class DiscussionTitleChange(DiscussionEvent):
    old_title: str
    new_title: str
    def __init__(self, id, type, created_at, author, _event, old_title, new_title) -> None: ...

def deserialize_event(event: dict) -> DiscussionEvent: ...
