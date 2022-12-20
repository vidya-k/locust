from locust import SequentialTaskSet,task,constant;
from readcontent import CsvRead
from content import ContentDetail
import json

class AdminApi(SequentialTaskSet):
    wait_time = constant(2)
    # weight= 1
    file_data = CsvRead("login-details.csv").read()


    def on_start(self):
        self.enrollmentData=[]
        self.client.headers={
            'Authorization': ContentDetail.token,
            'tenant-id':self.file_data['tenantId'],
            'Content-Type':'Application/json'
        }

    @task
    def getEnrollmentData(self):
         res = self.client.get('admin-courseenrollments?semid=FastTrack&schemeyear=Scheme%202018&deptid=CS&degreeid=BE&academicyear=2021-22&section=A&termbatch=REGULAR&termtype=Semester')
         if res.status_code== 200:
             print('Success! Admin Enrollment data ')
             json_object = json.loads(res.text)
             self.enrollmentData=json_object
         else:
            print('Error in getting Enrollment Data')

    @task
    def saveEnrollmentData(self):
         res = self.client.post('admin-courseenrollments/save',data=self.enrollmentData)
         if res.status_code== 200:
             print('Success! Enrollment Completed')
         else:
            print('Error in saving Enrollment Data')
    
    @task
    def getFastTrackEnrollmentReport(self):
         res = self.client.post('fasttrack-fee-payment/download-fasttrack-registration-report',data='')
         if res.status_code== 200:
             print('Success! Enrollment Report')
         else:
            print('Error in  Enrollment Report')
    
    @task
    def getProgressReport(self):
         data_list = ['UNIVERSITY_ASSESSMENT']
         json_object = json.dumps(data_list)
         res = self.client.post('assessmentreport/assessment?academicYear=2021-22&degreeId=BE&degreeBatch=REGULAR&deptId=EE&termNumber=FastTrack&scheme=Scheme%202018&section=A',data=json_object)
         if res.status_code== 200:
             print('Success! Progress Report')
         else:
            print('Error in  Progress Report')
         self.interrupt(reschedule=False)