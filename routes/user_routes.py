from fastapi import APIRouter
from controllers import user_controller
from models.user_model import User
router = APIRouter(prefix='/users',tags=['Users'])

@router.post('/')
def create_user(user:User):
    return user_controller.create_user_controller(user)
@router.get('/')
def get_users():
    return user_controller.get_all_users_controller()
@router.get('/{user_id}')
def get_user(user_id:int):
    return user_controller.get_user_by_id_controller(user_id)

@router.put('/{user_id}')
def update_user(user_id:int,updated_user:User):
    return user_controller.update_user_controller(user_id,updated_user)
@router.delete('/{user_id}')
def delete_user(user_id:int):
    return user_controller.delete_user_controller(user_id)