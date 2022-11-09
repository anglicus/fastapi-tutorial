from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date, datetime

from app.models import Post
    
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: Optional[str]
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime
    owner: UserResponse
    
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    likes: int
    
    class Config:
        orm_mode = True
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str]
    
class Vote(BaseModel):
    post_id: int
    dir: bool # True = up, False = down, i.e. delete vote