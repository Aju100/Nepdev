from typing import List
from pydantic import BaseModel

class NepaliDevSchema(BaseModel):
    name: str
    title: str
    actively_job_searching: bool = False
    address: str
    experience: int
    previous_companies: List[str]
    is_intern: List[str]
    blog_url: str
    github_url: str
    linkedln_url: str

class NepaliDevDB(NepaliDevSchema):
    id: int

    class Config:
        orm_mode = True