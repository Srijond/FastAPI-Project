from pydantic import BaseModel
from typing import List, Union


class Blog(BaseModel):
    title: str
    body:str
    user_name:str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] 

    class Config:
        orm_mode = True
 
class ShowUserInfo(BaseModel):
    name: str
    email: str

class ShowBlog(BaseModel):
    title: str
    body:str
    creator:ShowUserInfo
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None    