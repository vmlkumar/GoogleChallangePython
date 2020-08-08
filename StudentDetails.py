#Small Application

#Read the names and marks of atleast 3 students
#Rank the top 3 students with highest marks
#Give cash rewards. $500 for first rank,$300 for second rank,$100 for third rank. Value cannot be modified.
#Appreciate the students who secured 950 marks and above.
import operator

def readStudentDetails():
    numberOfStudents=int(input("Enter the number of students:"))
    studentRecord={}
    for student in range (0,numberOfStudents):
        name=input("Enter the name of the student {}:".format(student))
        marks=int(input("Enter the marks of the student:"))
        studentRecord[name]=marks
    return studentRecord    
def  rankStudents(studentRecord):
    try:
    
        sortedStudentRecord=sorted(studentRecord.items(), key=operator.itemgetter(1),reverse=True)
        print("{} has secured first rank,scoring {} marks".format(sortedStudentRecord[0][0],sortedStudentRecord[0][1]))
        print("{} has secured first rank,scoring {} marks".format(sortedStudentRecord[1][0],sortedStudentRecord[1][1]))
        print("{} has secured first rank,scoring {} marks".format(sortedStudentRecord[2][0],sortedStudentRecord[2][1]))
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of three students")
        quit()
def rewardStudents(sortedStudentRecord,reward):
    print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[0][0],reward[0]))
    print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[0][0],reward[1]))
    print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[0][0],reward[2]))
def appretiation(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1]>=950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break


studentRecord=readStudentDetails()
sortedStudentRecord=rankStudents(studentRecord)
reward=(500,300,100)
rewardStudents(sortedStudentRecord,reward)
appretiation(sortedStudentRecord)



