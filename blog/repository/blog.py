from fastapi import HTTPException,status,Response
from sqlalchemy.orm import Session
from blog import schemas
from .. import models

def get_all(db:Session):
   blogs =  db.query(models.Blog).all()
   return blogs

def create(request: schemas.Blog,db:Session):
    user_id = db.query(models.User.id).filter(models.User.name == request.user_name).scalar()
    # import pdb;pdb.set_trace()
    new_blog = models.Blog(title=request.title,body=request.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blod with {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()

    return 'done'

def update(id:int,request: schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blod with {id} not found")
    
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    

    blog_response = {
        'title': blog.title,
        'body': blog.body,
        'user_name': blog.creator.name  # Assuming 'name' exists in User model
    }
    
    return blog_response

