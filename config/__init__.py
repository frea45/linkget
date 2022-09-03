import os

class Config:
    API_ID = int( os.getenv("api_id","3335796") )
    API_HASH = os.getenv("api_hash","138b992a0e672e8346d8439c3f42ea78")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001787336960") )
    CHANNEL_USERNAME = os.getenv("channel_username","ir_botz")
    TOKEN = os.getenv("token","1943275919:AAFwSScrlR_i-AzdNTOiw8EEctbU_exOaGg")
    DOMAIN  = os.getenv("domain","https://dlchin.herokuapp.com")
