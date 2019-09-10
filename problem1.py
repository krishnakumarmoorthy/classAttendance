import pandas as pd
# [Example] Read datasets
data = pd.read_csv("training-attendanceT/SECTION1.csv", names=['Sno','Department','Branch','Semester','Course','RegistrationNo','StudentName','Date','Slot group','Time','ClassConducted','ClassAttended'])
datum=pd.DataFrame(data)
reg=[]
for val in datum.RegistrationNo:
    reg.append(val)
dat=[]
for val in datum.Date:
    dat.append(val)
cA=[]
for val in datum.ClassAttended:
    cA.append(val)
file=open("training-attendanceT/testcase.txt",'r')
n=int(file.readline())
k=1
while(n>0):
    re=str(file.readline().rstrip())
    da=str(file.readline().rstrip())
    count=0
    for i in range(len(reg)):
        if(reg[i] == str(re)):
            #print("true")
            if(dat[i] == str(da)):
                count = count + int(cA[i])

    filePath="output"+str(k)+".txt"
    filewrite = open(filePath,"w")
    filewrite.write(re+"\n"+str(count))
    n-=1
    k+=1
#[Example] Write output file 
#file.open("/code/output1.txt","w")
