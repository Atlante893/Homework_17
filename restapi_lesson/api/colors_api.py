from Homework_17.restapi_lesson.utilities.web_api.base_api import BaseAPI


class ColorsAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.color_url = "/api/unknown/"

    def get_color(self, color_id, headers=None):
        print('GET COLORS')
        return self.get(url=f"{self.color_url}{color_id}", headers=headers)

