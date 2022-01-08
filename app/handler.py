from fastapi import APIRouter, Body
from fastapi import Depends

from app.forms import UserLoginForm
from app.models import connect_db


router = APIRouter()


@router.post('/login')
def login(user_form: UserLoginForm=Body(...),
          database=Depends(connect_db)):
    # user_form.email and user_form.password
    return {'status': 'not ok'}
