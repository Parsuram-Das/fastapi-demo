from models.user_model import User
users_db =[]
def create_user(user:User):
    users_db.append(user)
    return user
def get_all_users():
    return users_db

def get_user_by_id(user_id:int):
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def update_user(user_id:int,updated_user:User):
    for idx,user in enumerate(users_db):
        if user.id == user_id:
            users_db[idx] = updated_user
            return updated_user
    return None

def delete_user(user_id:int):
    for idx,user in enumerate(users_db):
        if user.id == user_id:
            return users_db.pop(idx)
    return None