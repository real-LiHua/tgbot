from __future__ import annotations

from typing import List, Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class SearXNG(BaseModel):
    q: str = Field(
        ...,
        description="This string is passed to external search services. Thus, SearXNG supports syntax of each search service. For example, site:github.com SearXNG is a valid query for Google. However, if simply the query above is passed to any search engine which does not filter its results based on this syntax, you might not get the results you wanted.",
    )
    categories: Optional[List] = Field(
        None, description="specifies the active search categories"
    )
    engines: Optional[List] = Field(
        None, description="specifies the active search engines"
    )
    language: Optional[str] = Field(None, description="Code of the language.")
    pageno: Optional[int] = Field(None, description="Search page number.")
    time_range: Optional[str] = Field(
        None,
        description="[day,month,year]Time range of search for engines which support it. See if an engine supports time range search in the preferences page of an instance.",
    )
    safesearch: Optional[int] = Field(
        None,
        description="[ 0, 1, 2 ]Filter search results of engines which support safe search. See if an engine supports safe search in the preferences page of an instance.",
    )
