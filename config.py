from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("21827814"))
API_HASH = getenv("af097d21fa5049b0ed0d614ed3b885cd")

BOT_TOKEN = getenv("7369149161:AAFAoyZ818kS-St-mpcy2TTumzFlLFZWAX8")
#OWNER_ID = int(getenv("7037832227"))
OWNER_ID = int(getenv("OWNER_ID", "7376728791"))
MONGO_DB_URI = getenv("mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", None)
