import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26618097"))
    API_HASH = os.environ.get("API_HASH", "1154f54e18b67c1239f9674c643b7bcb")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5967250731:AAHdc_fnsJlewcP9UdKOfGPG939oVOhMY60")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBiro6EPQkk4s8AlwG0Wdb5NxLFAmcOmIal6e0EFXK0KtHYI4ug8bzx5or8k0gdiWgxzmHWLHYOVXq2ldGlpuYf4E_ysqV2D0-AwN9HIyMNWWpqpAIPtOXxU6Cg0RceFSpvETWvWnZPQ8doVHU2sO_au0PIHWbqa7AbzFPL0KsRc7S7YAS_gKsH1-eYe5zh80v3zrIy5XSNg3pWiiV2IzD3N_P9YMkhC839eZk-Qd5Cpw-4DRpZuHeUW2gHyRoN30Kd4bRbtno0xvigSa7dKTZmisEonm3eF5eZ3pqiRKX8_yMD8Cz_ExTfa-Xr2iCX2J51T-1oU1NnB5PBCxu4x8AAAAAV9RMh0A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001569815531"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
