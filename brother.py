from datetime import date, timedelta
import itertools
from collections import defaultdict
import random
import csv

start_date = None
end_date = None
brothersList =[]
datesList = []
schedDict = defaultdict(list)
class brother():
    def __init__(self):
        self.name = None
        self.grade = None
        self.gpa = None
        self.numShifts = None

    def addBrother(x):
        brothersList.append(x)
    
    def getDates(a,b):
        global start_date,end_date
        start_date = a
        end_date = b
        

    def calcNumShifts():
        for i in range(len(brothersList)):
            x = brothersList[i]
            
            if 2.5 < float(x.gpa) < 3.0 :
                #assign num of shifts
                x.numShifts = 5
            elif float(x.gpa) < 2.5 :
                #assign num of shifts
                x.numShifts = 6
            elif float(x.gpa) > 3.0 :
                #assign num shifts
                x.numShifts = 4
    
    def calcDates():
        global start_date,end_date
        print(start_date)
        print(end_date)
        delta = timedelta(days=1)
        while start_date <= end_date:
            if start_date.weekday() == 3: #thurs
                datesList.append(start_date)
                #schedDict[start_date.strftime('%m-%d-%Y')] = []
            elif start_date.weekday() == 4: #fri
                datesList.append(start_date)
                #schedDict[start_date.strftime('%m-%d-%Y')] = []
            elif start_date.weekday() == 5: #Sat
                datesList.append(start_date)
                #schedDict[start_date.strftime('%m-%d-%Y')] = []
            start_date += delta
    
    def scheduler():
        sat = ['Freshman','Sophomore']
        fri = ['Junior']
        thr = ['Senior','5th Year','Old']
        random.shuffle(datesList)
        for x,i in itertools.product(range(len(brothersList)),range(len(datesList))):
            b = brothersList[x]
            d = datesList[i]
            if  b.numShifts > 0 and b.grade in sat and d.strftime('%A') == 'Saturday' and len(schedDict[d.strftime('%m-%d-%Y')]) <4:
                schedDict[d.strftime('%m-%d-%Y')].append(b.name)
                b.numShifts = b.numShifts-1
            elif b.numShifts > 0 and b.grade in fri and d.strftime('%A') == 'Friday' and len(schedDict[d.strftime('%m-%d-%Y')]) <4:
                schedDict[d.strftime('%m-%d-%Y')].append(b.name)
                b.numShifts = b.numShifts-1
            elif b.numShifts > 0 and b.grade in thr and d.strftime('%A') == 'Thursday' and len(schedDict[d.strftime('%m-%d-%Y')]) <4:
                schedDict[d.strftime('%m-%d-%Y')].append(b.name)
                b.numShifts = b.numShifts-1
            
        w = csv.writer(open('schedule.csv','w'))
        for key,val in sorted(schedDict.items()):
            w.writerow([key,val])
        print(schedDict)
            
            