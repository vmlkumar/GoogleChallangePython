#A small application
import operator
import random
from heapq import nlargest

    #to enter no.of students and their names    
def enterStudentNames():
        noOfStudents =int(input("Enter the number of students in a class:"))
        studentdict={}
        #to enter the student names                           
        i=1
        while i<=noOfStudents:
            name=str(input("Enter the name of the student "+str(i)+":"))
            studentdict[name]=""
            i +=1
        return studentdict
               
     #to enter the student marks
def enterStudentMarks(studentdict):
        for x in studentdict:
            marks=float(input("Enter the marks of the "+x+":"))
            studentdict[x]=marks
        return studentdict

     #to select students with top three highest marks as prize winners
def rankStudents(studentdict):
        highest3=nlargest(3,studentdict,key=studentdict.get)
                               
        prize=1
        for student in highest3:
             studentmarks=studentdict[student]
             print("the prize " +str(prize)+" goes to "+student+ " who secured "+ str(studentmarks)+" marks")
             prize +=1
       
     #to select student ramdomly for grand prize winner
def grandPrizeWinner(studentdict):
        gPWName,gPWMarks=random.choice(list(studentdict.items()))
        print("the grant prize winner is "+gPWName+" who secured "+str(gPWMarks)+ " marks")
        print("Congratulations!!")

studentNamesRecord=enterStudentNames()
studentRecord=enterStudentMarks(studentNamesRecord)
rankStudents(studentRecord)
grandPrizeWinner(studentRecord)
