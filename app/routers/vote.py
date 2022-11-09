from os import stat
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db
from app import database

router = APIRouter(
  prefix="/vote",
  tags=["votes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id)
    post_result = post_query.first()
    if not post_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    vote_result = vote_query.first()

    if vote.dir: # True = like
        if vote_result:
            print("01")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already like post {vote.post_id}")
        else:
            print("02")
            new_vote = models.Vote(user_id = current_user.id, post_id = vote.post_id)
            db.add(new_vote)
            db.commit()
            return {"message": "successfully added like"}
    else: # False = delete like
        print('trying to delete vote')
        if vote_result:
            print("03")
            vote_query.delete(synchronize_session=False)
            db.commit()
            return {"message": "successfully deleted like"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"like on post {vote.post_id} does not exist")