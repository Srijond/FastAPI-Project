from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends, HTTPException, Response,status
from .. import schemas,database,models,oauth2
from blog.repository import blog



router = APIRouter(
    prefix="/blog",
    tags=['blog']

)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = blog.get_all(db)
    # user_table = models.Blog.__table__
    # create_query = str(CreateTable(user_table).compile(engine))

    # print(create_query)
    return blogs

@router.post('/',status_code=201)
def create(request: schemas.Blog, db:Session= Depends(get_db)):
    new_blog = blog.create(request,db)
    return new_blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    return blog.destroy(id,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id, db:Session = Depends(get_db)):
    return blog.show(id,db)
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request: schemas.Blog,db:Session = Depends(get_db)):
    return blog.update(id,request,db)