from typing import Union,List 
from pydantic import Field, BaseModel
from datetime import datetime


class GetPerson(BaseModel):
    class Person(BaseModel):
        person_id: int = Field(default=-1)
        person_name: str = Field(default="")
        person_last_name: str = Field(default="")
        active: int = Field(default=1)
        created_at: Union[datetime, None] = Field(default=datetime.now())
        updated_at: Union[datetime, None] = Field(default=datetime.now())
    person:List[Person] = [Person()]

class SetPerson(BaseModel):
    person_id: int = Field(default=-1)
    person_name: str = Field(default="")
    person_last_name: str = Field(default="")
    active: int = Field(default=1)

    class Config: 
        json_schema_extra = {
            "example": {
                "person_id": 1,
                "person_name": "",
                "person_last_name": "",
                "active":1,
            }
        }
