maindic = {}

def newpolicycalc(markslis,value):
        templis = []
        for elem in markslis:
            if value-2 <= elem <= value+2:
                templis.append(elem)
        templis.sort()
        highdiff = 0
        index = 0
        for i in range(len(templis)-1):
            diff = abs(templis[i] - templis[i+1])
            if diff >= highdiff:
                highdiff = diff
                index = i
        if len(templis) > 1:
            cutoff = (templis[index] + templis[index+1])/2
        else:
            cutoff = (templis[index])
        return cutoff

def gradecalc(cname,marks):
    cutofflis = maindic[cname]["cutoffs"] #length = 4
    if marks > cutofflis[0]:
        return "A"
    elif cutofflis[1] < marks <= cutofflis[0]:
        return "B"
    elif cutofflis[2] < marks <= cutofflis[1]:
        return "C"
    elif cutofflis[3] < marks <= cutofflis[2]:
        return "D"
    else:
        return "F"

class course:
    def __init__(self,coursename):
        self.cname = coursename
    
    def initalisecourse(self,credits):
        maindic[self.cname] = {}
        maindic[self.cname]["credits"] = int(credits)

    def addassem(self,list):
        maindic[self.cname]["assessments"] = {}
        for i in range(len(list)):
            maindic[self.cname]["assessments"][list[i][0]] = list[i][1]

    def addgradepolicy(self,list):
        maindic[self.cname]["gradepolicy"] = list


    def upload_marks(self):
        maindic[self.cname]["StudentsGrade"] = {}
        with open("Files/%s_Assign3_Q4.txt" %self.cname) as f:
            tempstr = f.readline().strip() #Loop To Read Data
            while tempstr != "":
                templis = tempstr.split(", ")
                maindic[self.cname]["StudentsGrade"][templis[0]] = list(map(int,templis[1:]))
                maindic[self.cname]["StudentsGrade"][templis[0]].append(sum(list(map(int,templis[1:]))))
                tempstr = f.readline().strip()

    def cutoff_calc(self):
        gradelis = maindic[self.cname]['gradepolicy'] 
        markslis = []
        newgradelis = []
        for elem in maindic[self.cname]["StudentsGrade"].values():
            markslis.append(elem[-1])
        for elem in gradelis:
            newgradelis.append(newpolicycalc(markslis,elem))
        maindic[self.cname]["cutoffs"] = newgradelis

    def dograding(self):
        maindic[self.cname]["FinalGrades"] = {}
        for x,y in maindic[self.cname]["StudentsGrade"].items():
            grade = gradecalc(self.cname,y[-1])
            maindic[self.cname]["FinalGrades"][x] = grade
            maindic[self.cname]["StudentsGrade"][x].append(grade)

    def summary(self):
        cname = self.cname
        print("Course Name -", cname)
        print("Course Credits -",maindic[cname]["credits"])
        print()
        print("Assesments & Weights")
        for x,y in maindic[cname]["assessments"].items():
            print("%s - %s"%(x,y))
        print()
        print("Final Cutoffs & Grades")
        cutofflis = maindic[cname]["cutoffs"] #length = 4
        print("A - Marks >",cutofflis[0]) 
        print("B - Marks Between %s and %s "%(cutofflis[0],cutofflis[1]))   
        print("C - Marks Between %s and %s "%(cutofflis[1],cutofflis[2]))
        print("D - Marks Between %s and %s "%(cutofflis[2],cutofflis[3]))
        print("F - Marks <",cutofflis[3])
        print()
        tempdic = {'A': 0, 'B': 0, 'C': 0, 'D': 0,'F': 0}
        for elem in maindic[cname]["FinalGrades"].values():
            tempdic[elem] += 1
        for x,y in tempdic.items():
            print("Number of %s's = %s" %(x,y))

IP = course("IP")
IP.initalisecourse(4)
IP.addassem([("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)])
IP.addgradepolicy([80, 65, 50, 40])
IP.upload_marks()
IP.cutoff_calc()
IP.dograding()



def printing_details():
    print("--------------------------------------------------------------------")
    print("IIITD Admin - Course Manager -", "\nSelect Option Number")
    print("1. Generate a summary. \n2. Print the grades of all the students in a file. \n3. Search for a given student's record \n4. Exit.")
    print("--------------------------------------------------------------------")
    

while True:
    printing_details()
    n = int(input("Your Selected Option - "))
    if n == 1:
        name = input("ENTER COURSE NAME - ")
        summary(name)
    elif n == 2:
        name = input("ENTER COURSE NAME - ")
        with open("Files/%s_MarksOutput.txt" %name,"w") as f:
            for x,y in maindic[name]["StudentsGrade"].items():
                tempstr = str(x) + ", " + str(y[-2]) + ", " + str(y[-1]) + "\n"
                f.writelines(tempstr)
    elif n == 3:
        name = input("ENTER COURSE NAME - ")
        m = input("Enter Student's Roll Number - ")
        if m in maindic[name]["StudentsGrade"].keys():
            lis = maindic[name]["StudentsGrade"][m] 
            ass_lis = []
            for x,y in maindic[name]["assessments"].items():
                ass_lis.append((x,y))
            print("%s's Details" %m)
            print()
            for i in range(len(ass_lis)):
                print("%s - %s/%s" %(ass_lis[i][0],lis[i],ass_lis[i][1]))
            print()
            print("Total Marks - %s/100" %lis[-2])
            print("Final Grade - %s" %lis[-1])
        else:
            print("Student Does NOT Exist!")
    elif n == 4:
        exit()
        break
    else:
        print("Invalid Input. Try Again :)")

