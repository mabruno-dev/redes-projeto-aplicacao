from pydantic import Field, BaseModel
from typing import List, Union
from datetime import datetime

class GetPhone(BaseModel):
    class Phone(BaseModel):
        phone_id: int = Field(default=-1)
        phone_person: int = Field(default=-1)
        phone_ddd: str = Field(default="")
        phone_number: str = Field(default="")
        created_at: Union[datetime, None] = Field(default=datetime.now())
        updated_at: Union[datetime, None] = Field(default=datetime.now())
        active: int = Field(default=-1)

    phone: List[Phone] = [Phone()]

class SetPhone(BaseModel):
    phone_id: int = Field(default=-1)
    phone_person: int = Field(default=-1)
    phone_ddd: str = Field(default="")
    phone_number: str = Field(default="")
    active: int = Field(default=-1)

    class Config: 
        json_schema_extra = {
            "example": {
                "phone_id": 1,
                "phone_person": "1",
                "phone_ddd":"21",
                "phone_number": "995430832",
                "active":1,
            }
        }