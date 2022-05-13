print("--------------THE COVID EXPERT SYSTEM-----------------")
symp=[]
symp_count=0
severity=0

def ques():
    
    s=''
    i=int(0)
    global severity
    severity=i
    symp_count=i

    print("Do you have fever?(y/n)")
    s=input('-->')
    if(s=='y'):
        severity+=2
        symp_count+=1
        symp.append('fever')

        print("\t from days?")
        i=int(input("\t--->"))
        if(i>5):
            severity+=1

def report():
    print(severity)
    print("\n\nsymptoms: \n")
    for k in symp:
        print('-->',k)
    print()
    if(severity>15):
        print("dossjn")
    elif(severity<15):
        print("hsuw")


ques()
report()
