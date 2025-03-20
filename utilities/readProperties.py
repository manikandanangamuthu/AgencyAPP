import configparser


config=configparser.RawConfigParser()

config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        URL=config.get('common info','baseURL')
        return URL

    @staticmethod
    def getUsername():
        username= config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password= config.get('common info', 'password')
        return password

    @staticmethod
    def upload_companylogo():
        logo=config.get('common info','companylogo')
        return logo
