# -*- coding:utf-8 -*-
"""
@Date: 2023/11/20
@Author: zhaowanpeng
@Des: 用户模型
"""
from typing import Optional  # 用于表示一个可能存在的值或者一个空值（None）的情况
from sqlmodel import Field, SQLModel
from datetime import datetime


class User(SQLModel):
    id: Optional[str] = Field(default=None, primary_key=True)
    username: str
    password: str
    superuser: bool = False
    is_active: bool = True
    create_time: datetime = Field(default=datetime.utcnow)
    last_login: datetime
    role: int = Field()