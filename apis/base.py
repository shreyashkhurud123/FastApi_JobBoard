# File for adding different routers here instead of the main.py file to avoid cluttering the main file
# Also it will be easily managable since the endpoint prefix will also be handled here

from fastapi import APIRouter

from apis.version1 import route_users

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/user", tags=["users"])
