from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from .session import Base

class NepaliDev(Base):
    __tablename__ = "NepaliDev"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=True),
    title =  Column(String(50)),
    actively_job_searching(Boolean, default=False),
    address= Column(String(30)),
    experience = Column(Integer),
    previous_companies = Column(ARRAY(String)),
    is_intern =  Column(Array(String),default=False),
    blog_url = Column(String),
    github_url = Column(String),
    linkedln_url = Column(String),

    def __init__(self, title, name):
        self.title = title
        self.name = name
