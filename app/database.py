from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

# Credenciais do mongoDB ATLAS
uri = "mongodb+srv://HEITOR:5USzx1vc8BBKNTAl@cluster0.vpobjyw.mongodb.net/TESTE?retryWrites=true&w=majority"

# Conectando com a api do banco de dados
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

db = client.TESTE  

async def ping():
    try:
        await db.command('ping')
        print("Connected to MongoDB!")
    except Exception as e:
        print(e)
