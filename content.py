from locust import SequentialTaskSet

class ContentDetail(SequentialTaskSet):

    userData={}
    token={}

    def __init__(self,parent):
         super().__init__(parent)
