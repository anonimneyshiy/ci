from fastapi import APIRouter, Body
from fastapi import Depends

from app.forms import UserLoginForm
from app.models import connect_db, User


router = APIRouter()


@router.post('/login', name='user: login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    user = database.query(User).fillter(User.email == user_form.email).one_or_none()
    if not user:
        return {'error': 'Email/password invalid'}
    return {'status': 'not ok'}
