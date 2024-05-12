l=[]
l2=[]
i=1
std_num=int(input("how many student's result are to be made-->"))
while std_num>=i:

    r_no=int(input("Enter Rollno="))
    l.append(r_no)
    name=input("Enter Name=")
    l.append(name)
    for j in range(1):
        Hindi=int(input("Enter Hindi Marks="))
        l.append(Hindi)
        English=int(input("Enter English marks="))
        l.append(English)
        Math=int(input("Enter Math marks="))
        l.append(Math)
        Science=int(input("Enter Science marks="))
        l.append(Science)
        Sst=int(input("Enter SST marks="))
        l.append(Sst)
        total=Hindi+English+Math+Science+Sst 
        l.append(total)
    
        percentage=total//5
        l.append(percentage)
        if percentage>=75:
            D="A+"
        if percentage>=60 and 75>percentage:
            D="A"
        if percentage>=45 and 60>percentage:
            D="B"
        if percentage>=33 and 45>percentage:
            D="C+"
        if percentage<=32:
            D="Fail"

    l.append(D) 
    #l=[r_no,name,Hindi,English,Math,Science,Sst,total,percentage,D]
    #for i in l:
        #print(i,end="\t")
        #l2=i
    l2.extend(l)
    l.clear()    
    i+=1
print("\n\nRollno\t Name\tHindi\tEnglish\t Math\tScience\t SST\tTotal\tPercent\t Grade")
if std_num==1:
    for j in l2:
        print(" ",j,end="\t")
else: 
    for i in l2:
        if i==r_no:
            print("\n")
        print(" ",i,end="\t")