# from numpy import append

print('---------------Covid Expert System-----------------')
symp=[]
symp_count=0
severity=0



def ques():
    s=''
    i=int(0)
    global severity
    # print('How many symptoms do you have from following list:-\n (sore throat,headache,body ache,diarrhoea,rashes on skin,red eyes)?')
    # i=int(input("> "))
    severity=i
    symp_count=i

    print('Do you have fever?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('fever')
        severity+=2
        symp_count+=1
        print('\tFrom how many days you have fever?')
        i=int(input("\t---> "))
        if(i>7):
                severity+=1



    print('Do you have cough?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('cough')
        severity+=2
        symp_count+=1
        print('\tDry cough or wet cough(1/2)?')
        i=int(input("\t---> "))
        if(i==1):
            severity+=1



    print('Do you feel tired frequently?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('tiredness')
        severity+=2
        symp_count+=1
        print('\tHow frequent in a day do you feel so?')
        i=int(input("\t> "))
        if(i>8):
            severity+=1

    print('Do you have lost of taste?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('loss of taste')
        severity+=2
        symp_count+=1

    print('Do you feel difficulty breathing or shortness of breath?(y/n)')
    s=input("--> ")
    if(s=='y'):
        symp.append('breathing difficulty')
        severity+=3
        symp_count+=1

    print('Do you feel loss of speech or mobility, or confusion?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('loss of speech/mobility/confusion')
        severity+=3
        symp_count+=1


    print('Do you have chest pain?(y/n)')
    s=input("---> ")
    if(s=='y'):
        symp.append('chest pain')
        severity+=4
        symp_count+=1


def report():
    print(severity)
    print('\n\nYou have following symptoms:-\n')
    for k in symp:
        print("->",k)
    print()

    if(severity>15):
        print("Diagnosis:There are very high chances that you are covid Positive")
        print("Precautions:- Isolate Yourself, Get RTPCR test done")
        print("Refer your case to a doctor as soon as possible and follow the procedure you may need to get hospitalize so be prepared")

    elif(severity<15 and severity>10):
        print("Diagnosis:There are high chances that you are covid positive but not much serious")
        print("Precautions:- Isolate Yourself, Get RTPCR test done")
        print("Refer your case to a doctor on phone and follow the procedure ")

    elif(severity<10 and severity>5):
        print("Diagnosis:There are slight chances that you are covid positive")
        print("Precautions:- Isolate Yourself, Get RTPCR test done")
        print("Manage the symptons at home nothing much serious")

    elif(severity<5):
        print("Diagnosis:You are most probably not affected by covid")
        print("Take general medicines if you have any mild symptoms")
    



ques()
report()
        
