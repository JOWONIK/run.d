from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from db import PyObjectId


class Content(BaseModel):
    content: str


class MultiLang(BaseModel):
    ko: Optional[Content]
    en: Optional[Content]


class Source(BaseModel):
    type: str
    url: str


class EventList(BaseModel):
    start_timestamp: datetime
    source: List[Source]
    files: List[str]
    multi_lang: MultiLang


class InsertEventInModel(BaseModel):
    main_lang: Optional[str]
    trans_lang: Optional[str]
    title_ko: Optional[str]
    title_en: Optional[str]
    project_id: List[PyObjectId]
    category: str
    sub_category: str
    event_timestamp: datetime
    status: str
    is_visible: bool
    follow_ids: List[PyObjectId]
    related_assets: List[PyObjectId]
    event_list: List[
        EventList
    ]
    create_timestamp: datetime
    create_id: str
    modify_timestamp: datetime
    modify_id: str
