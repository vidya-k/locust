from locust import SequentialTaskSet,task,constant;
from readcontent import CsvRead
from content import ContentDetail

class CommonApi(SequentialTaskSet):
    wait_time = constant(2)
    weight= 1
    file_data = CsvRead("login-details.csv").read()


    def on_start(self):
        self.client.headers={
            'Authorization': ContentDetail.token,
            'tenant-id':self.file_data['tenantId'],
            'Content-Type':'Application/json'
        }

    @task
    def getTimetableData(self):
         
         res = self.client.get('studentdashboard/studentsectiontimetable?studentid=61b1beefd3dee6577a1b0fe8&academicyear=2022-23&termNumber=3&deptid=CS&degreeid=BE&section=A&termBatch=REGULAR&scheme=CBCS%202021')
         if res.status_code== 200:
             print('Success! Timetable Data  found')
         else:
            print('Error Timetable Data  Not found')

    @task
    def getNoticesData(self):        
         res = self.client.get('dashboardnotices?role=STUDENT&degreeid=BE&degreebatch=REGULAR&deptid=CS&userid=61b1beefd3dee6577a1b0fe8')
         if res.status_code== 200:
             print('Success! Notices Data  found')
         else:
            print('Error Notices Data  Not found')
         self.interrupt(reschedule=False)


    @task
    def getCourseEnrollmentData(self):        
         res = self.client.get('enrollments/student?academicyear=2022-23&degreeid=BE&semid=7&studentid=5fe43d2b2c8e807cd3cf57a0&degreebatch=REGULAR&scheme=Scheme%202018&deptid=EE&section=A')
         if res.status_code== 200:
             print('Success! Enrolled Courses data got')
         else:
            print('Error in getting enrolledCourses')
         self.interrupt(reschedule=False)

    @task
    def checkEnrollmentBlocked(self):        
         res = self.client.get('courseenrollments/checkenrollmentblocked?studentid=5fe43d2b2c8e807cd3cf57a0')
         if res.status_code== 200:
             print('Successfully ! checked studet is blocked or not')
         else:
            print('Error in checking block student')
         self.interrupt(reschedule=False)

    @task
    def getCoursesToEnroll(self):
         res= self.client.get('courseenrollments/student?academicyear=2022-23&degreeid=BE&termnumber=7&termtype=Semester&scheme=Scheme%202018&studentid=5fe43d2b2c8e807cd3cf57a0&specialization=&section=A&status=LATERAL&deptid=EE&deptid=EE&degreebatch=REGULAR')
         if res.status_code== 200:
             print('Success! got courses to enroll')
         else:
            print('Error in getiing courses to enroll')
         self.interrupt(reschedule=False)
    

    @task
    def checkEligibleToFastTrackRegistration(self):
         res= self.client.get('courseenrollments/checkEligibleToRegisterForFastTrack?studentid=5fe43d2b2c8e807cd3cf57a0')
         if res.status_code== 200:
             print('Successfully checked ! student is eligible to fasttrack registration or not')
         else:
            print('Error in checking fasttrack registration eligibility')
         self.interrupt(reschedule=False)
   
    @task
    def checkBacklogEnrollmentLimit(self):
         data = []
         data[0]['academicYear'] = self.file_data['userName']
         data[0]['candidateId'] = self.file_data['password']
         data[0]['courseCode'] =  self.token_credential['resource']
         data[0]['degreeId'] =  self.token_credential['credentials']['secret']
         data[0]['studentId'] = 'password'
         res= self.client.post('enrollments/checkforbacklogcourseenrollmentlimit',data=data)
         if res.status_code== 200:
             print('Successfully checked enrollment backlog limit')
         else:
            print('Errorin checking backlog enrollment limit')
         self.interrupt(reschedule=False)
    

    @task
    def getUniverstyExamData(self):
         res= self.client.get('university-exam/score/students/5fe43d2b2c8e807cd3cf57a0?academicyear=2021-22&degree=BE&departmentid=EE&termNumber=5&scheme=Scheme%202018&examid=FEBRUARY_APRIL_2022&usn=2GI20EE409')
         if res.status_code== 200:
             print('Successfully got university Data')
         else:
            print('Error in getting university exam data')
         self.interrupt(reschedule=False)


    @task
    def downloadMarksCard(self):
         res= self.client.post('student-ue-result/download-provisonal-marks-card?id=5fe43d2b2c8e807cd3cf57a0&termnumber=5&examid=FEBRUARY_APRIL_2022&academicYear=2021-22&universitydownload=false',data="")
         if res.status_code== 200:
             print('Successfully downloaded marks card')
         else:
            print('Error in downloading marks card')
         self.interrupt(reschedule=False)
