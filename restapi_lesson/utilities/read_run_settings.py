import configparser
import os
from Homework_17.restapi_lesson.CONSTS import ROOT_DIR

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user', 'name')

    @staticmethod
    def get_user_job():
        return config.get('user', 'job')

