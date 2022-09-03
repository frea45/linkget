import os

class Config:
    API_ID = int( os.getenv("api_id","") )
    API_HASH = os.getenv("api_hash","")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001787336960") )
    CHANNEL_USERNAME = os.getenv("channel_username","ir_botz")
    TOKEN = os.getenv("token","1943275919:AAFwSScrlR_i-AzdNTOiw8EEctbU_exOaGg")
    DOMAIN  = os.getenv("domain","https://dlchin.herokuapp.com")
