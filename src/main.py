from fastapi_users import FastAPIUsers

from fastapi import FastAPI

from src.redis_config import get_redis, close_redis

from src.auth.base_config import auth_backend
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.codes.router import router as router_codes
from src.referral.router import router as referral

app = FastAPI(
    title="Referral Codes App"
)

fastapi_user = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


@app.on_event("startup")
async def startup_event():
    await get_redis()


@app.on_event("shutdown")
async def shutdown_event():
    await close_redis()


app.include_router(
    fastapi_user.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Authorization"],
)

app.include_router(
    fastapi_user.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Authorization"],
)

current_user = fastapi_user.current_user()


app.include_router(router_codes)
app.include_router(referral)
