from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.models import User
from src.referral.schemas import Referral

router = APIRouter(
    prefix="/referrals",
    tags=["Referrals"]
)


@router.get("/{referrer_id}", response_model=List[Referral])
async def get_referrals(referrer_id: int,
                        session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).filter(User.referrer_id == referrer_id)
    result = await session.execute(stmt)
    referrals = result.scalars().all()
    return referrals
