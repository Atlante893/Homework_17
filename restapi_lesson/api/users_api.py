from Homework_17.restapi_lesson.utilities.web_api.base_api import BaseAPI
import json


class UsersApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/api/users/"

    def get_user(self, user_id, headers=None):
        print('GET PEOPLE')
        return self.get(url=f"{self.user_url}{user_id}", headers=headers)

    def post_user(self):
        print('POST USER')
        return self.post(url=f"{self.user_url}", body=json.dumps({"name": f"{self.name}",
                                                                  "job": f"{self.job}"}),
                         headers={"Content-Type": "application/json"})

    def put_user(self):
        print('PUT USER')
        return self.put(url=f"{self.user_url}{2}", body=json.dumps({"name": f"{self.name}_Yeshchenko",
                                                                  "job": f"{self.job}"}),
                         headers={"Content-Type": "application/json"})

    def patch_user(self):
        print('PATCH USER')
        return self.patch(url=f"{self.user_url}{2}", json={"name": "Yeshchenko"})

    def delete_user(self):
        print('DELETE USER')
        return self.delete(url=f"{self.user_url}{2}")
