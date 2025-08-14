from fastapi import HTTPException
from services import user_service
from utils.response import success_response 
def create_user_controller(user):
    created_user= user_service.create_user(user)
    return success_response('User created successfully',created_user)

def get_all_users_controller():
    users=user_service.get_all_users()
    return success_response('Users retrieved successfully', users)

def get_user_by_id_controller(user_id:int):
    user= user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404,detail='User not found')
    return success_response('User retrieved successfully', user)
def update_user_controller(user_id:int, updated_user):
    user = user_service.update_user(user_id,updated_user)
    if not user:
        raise HTTPException (status_code=404,detail='User not found')
    return success_response('User updated successfully', user)

def delete_user_controller(user_id:int):
    deleted_user=user_service.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail='User not found')
    return success_response('User deleted successfully', deleted_user)