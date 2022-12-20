from locust import SequentialTaskSet,task,constant
from readcontent import CsvRead
import json
import requests
from content import ContentDetail

class LoginApiTest(SequentialTaskSet):
    file_data = CsvRead("login-details.csv").read()
    # weight= 2
    wait_time = constant(2)
    # tasks =[AdminApi]
    def on_start(self):
         print("Login API Initialized")
        #  super().__init__(parent)
         self.token_credential={}
         res= self.client.get("login/kcinit?college="+self.file_data['tenantId'])
         if(res.status_code==200):
                json_object = json.loads(res.text)
                self.token_credential=json_object
         else:
              print(res.text)
    
    @task
    def tokenApi(self):
         url = self.file_data['keyclockUrl']
         self.client.headers={
             'Content-Type': 'application/x-www-form-urlencoded',
         }
         data = {}
         data['username'] = self.file_data['userName']
         data['password'] = self.file_data['password']
         data['client_id'] =  self.token_credential['resource']
         data['client_secret'] =  self.token_credential['credentials']['secret']
         data['grant_type'] = 'password'

         res = requests.post(url+"?clientId="+self.file_data['tenantId'],data=data)
         if(res.status_code==200):
                json_object = json.loads(res.text)
                ContentDetail.token='Bearer '+json_object['access_token']
         else:
              print(res.text)

    @task
    def kcUserApi(self):
         self.client.headers={
            'Authorization': ContentDetail.token,
            'tenant-id':self.file_data['tenantId'],
            'Content-Type':'application/json'
         }
         res= self.client.get("login/kcuser?college="+self.file_data['tenantId'])
         if res.status_code== 200:
             ContentDetail.userData=json.loads(res.text)
         else:
            print('Error User Not found')
         self.interrupt(reschedule=False)