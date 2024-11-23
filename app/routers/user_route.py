from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserResponse,UserCreate
from app.repository.user_repository import create_user,get_user,get_all_user,login_user
from app.DBHandler import get_db

router = APIRouter()

@router.post("/user",response_model=UserResponse)
def create_new_user(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db=db,user=user)
@router.get("/user",response_model=UserResponse)
def read_user(user_id:int,db:Session=Depends(get_db)):
    return get_user(db=db,user_id=user_id)
@router.get("/users",response_model=List[UserResponse])
def read_all_user(skip:int=0,limit:int=20,db:Session=Depends(get_db)):
    return get_all_user(db=db,skip=skip,limit=limit)
@router.get("/login",response_model=UserResponse)
def login(email:str,password:str,db:Session=Depends(get_db)):
    return login_user(db=db,email=email,password=password)