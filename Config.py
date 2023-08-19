import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17651177"))
    API_HASH = os.environ.get("API_HASH", "7d089f4a94b0f470ce2233fc58c35799")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6662876004:AAHq8FRC2ImP1FeqLya4KqgSWdop-meVoIU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHgBu1k-W3Hk4N7DcLnhSpeFfatLXaE9nnR7uPupPfPhbUFabfLh1Osr7y2vn037OtspOja6jJ3Xzp2_F8IzgodKB6A4BUJAeI4gMCVkR4P4LIOscRu6H7uCs7tD1bnFAtP9N2xY-xwhBj8ZBF2ojfX27x7WEGV_4dfR6kYYA34mm6aaMAPyLtiz6KEAvfwtorOWsBB2np9kyP5BbxnWdIQUkc84X-LSmmCuZw-aTZolHZH9TWBlYSV2t02yzVWQr0LcMMrvwfbDbaTE_TB-72UPIa5e31lEDQZH5FjCuEtzj-d5_S5FbTjmNK0PDDJo8jUe7Q8ATmb15Mds4ugtdyVsOeM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "hackingmade2") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "DevoKeDevMahadevm") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1774623002")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
