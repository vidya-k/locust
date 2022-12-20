from locust import HttpUser,task,constant,SequentialTaskSet
from readcontent import CsvRead
from user_behaviour import UserBehaviourTask

class AppApiTest(HttpUser):
    file_data = CsvRead("login-details.csv").read()
    host=file_data['url']
    tasks=  [UserBehaviourTask]
    # def on_start(self):
        # self.client.headers={
        #     'Authorization': self.file_data['token'],
        #     'tenant-id':self.file_data['tenantId'],
        #     'Content-Type':'Application/json'
        # }

   
   

