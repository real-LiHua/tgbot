from .utils import is_pydantic_available as is_pydantic_available
from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Literal

class BaseModel:
    def __init__(self, *args, **kwargs) -> None: ...

WebhookEvent_T: Incomplete
RepoChangeEvent_T: Incomplete
RepoType_T: Incomplete
DiscussionStatus_T: Incomplete
SupportedWebhookVersion: Incomplete

class ObjectId(BaseModel):
    id: str

class WebhookPayloadUrl(BaseModel):
    web: str
    api: str | None

class WebhookPayloadMovedTo(BaseModel):
    name: str
    owner: ObjectId

class WebhookPayloadWebhook(ObjectId):
    version: SupportedWebhookVersion

class WebhookPayloadEvent(BaseModel):
    action: WebhookEvent_T
    scope: str

class WebhookPayloadDiscussionChanges(BaseModel):
    base: str
    mergeCommitId: str | None

class WebhookPayloadComment(ObjectId):
    author: ObjectId
    hidden: bool
    content: str | None
    url: WebhookPayloadUrl

class WebhookPayloadDiscussion(ObjectId):
    num: int
    author: ObjectId
    url: WebhookPayloadUrl
    title: str
    isPullRequest: bool
    status: DiscussionStatus_T
    changes: WebhookPayloadDiscussionChanges | None
    pinned: bool | None

class WebhookPayloadRepo(ObjectId):
    owner: ObjectId
    head_sha: str | None
    name: str
    private: bool
    subdomain: str | None
    tags: list[str] | None
    type: Literal['dataset', 'model', 'space']
    url: WebhookPayloadUrl

class WebhookPayloadUpdatedRef(BaseModel):
    ref: str
    oldSha: str | None
    newSha: str | None

class WebhookPayload(BaseModel):
    event: WebhookPayloadEvent
    repo: WebhookPayloadRepo
    discussion: WebhookPayloadDiscussion | None
    comment: WebhookPayloadComment | None
    webhook: WebhookPayloadWebhook
    movedTo: WebhookPayloadMovedTo | None
    updatedRefs: list[WebhookPayloadUpdatedRef] | None
