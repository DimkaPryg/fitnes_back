from pydantic import BaseModel


class UserInfoBase(BaseModel):
    login: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True