from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column
from src.auth.models import user

metadata = MetaData()


referral_code = Table(
    "referral_code",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("code", String, unique=True),
    Column("expiration_date", TIMESTAMP)
)
