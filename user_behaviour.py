from locust import SequentialTaskSet
from student import CommonApi
from admin import AdminApi
from login_details_api import LoginApiTest

class UserBehaviourTask(SequentialTaskSet):
    tasks=[LoginApiTest,AdminApi]