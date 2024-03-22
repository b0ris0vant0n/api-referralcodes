from dotenv import load_dotenv
import os

load_dotenv()

# DB Data
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# Referrals Code
REFERRALS_CODE_VALIDITY = int(os.environ.get("REFERRALS_CODE_VALIDITY"))
REFERRALS_CODE_LENGTH = int(os.environ.get("REFERRALS_CODE_LENGTH"))

# HunterEmail
EMAIL_API_KEY = os.environ.get("EMAILHUNTER_APIKEY")

# Secret
SECRET = os.environ.get("SECRET")
