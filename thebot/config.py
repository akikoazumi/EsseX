class Config(object):
    LOGGER = True
    API_ID = 3261733
    API_HASH = "240b164f1b8082e49e87793ac6594da9"
    TOKEN = "1605194389:AAFhgteAnU--yRbWaEt13GJXQ0kIPZRkzMg"
    DB_URI = ""
    LOG_CHANNEL = 0 # if you want a logging channel you can add this, else logs will go into Owner's PM

class Development(Config):
    TEST_DEVELOP = True
    LOGGER = True
