from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Table, Column
from src.auth.models import user
from src.database import metadata


referral_code = Table(
    "referral_code",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("code", String, unique=True),
    Column("expiration_date", TIMESTAMP)
)
