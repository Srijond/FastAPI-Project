from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends, HTTPException, Response,status
from .. import schemas,database,models



router = APIRouter(
    prefix="/user"
)
get_db = database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return new_user
@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
        return user
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")








