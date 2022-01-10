from configparser import ConfigParser

# create object of ConfigParser class
config = ConfigParser()

# Read from Config file
config.read("../Configurations/Configure.cfg")  # ../ represents current project directory


# when we say @staticmethod we can access particular method with class name without creating object of that class
class ReadConfig:
    @staticmethod
    def get_username():
        username = config.get('Section1', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Section1', 'password')
        return password
