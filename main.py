# import sys
# import os

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI
from routes import user_routes

app=FastAPI(title='User CRUD API')
app.include_router(user_routes.router)
@app.get('/')
def home():
    return {'message':'welcome to the user CRUD API'}