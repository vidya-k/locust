import csv
import random

class CsvRead:
    
    def __init__(self,file):
        try:
            file = open(file)
        except FileNotFoundError:
            print("File Not found")
             
        self.file = file
        self.reader = csv.DictReader(file)

    def read(self):
        return random.choice(list(self.reader))

    # def write(self,data):
    #     with open(self.file, 'w') as csvfile: 
    #      # creating a csv dict writer object 
    #      writer = csv.DictWriter(csvfile, fieldnames = "token") 
        
    #      # writing data rows 
    #      writer.writerow(data)
         
    