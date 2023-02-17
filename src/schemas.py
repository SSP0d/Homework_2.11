from datetime import date

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=20)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=10)
    birthday: date
    description: str = Field(min_length=3, max_length=255)


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
