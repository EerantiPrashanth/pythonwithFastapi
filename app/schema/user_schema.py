from pydantic import BaseModel, EmailStr ,Field
from typing import Optional

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)

    email: EmailStr

    age: int = Field(..., ge=18, le=100)

    phone: Optional[str] = Field(None, min_length=10, max_length=15)

    address: Optional[str] = Field(None, max_length=100)
    
class UpdateUser(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18, le=100)
    phone: Optional[str] = Field(None, min_length=10, max_length=15)
    address: Optional[str] = Field(None, max_length=100)