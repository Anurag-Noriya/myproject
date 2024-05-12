def APP(a):
        t1=(0,)
        t1=a
        print("Total Vout of APP=",sum(t1))
        

def BJP(b):
        t2=(0,)
        t2=b
        print("Total Vout of BJP=",sum(t2))
        
def CONGRESS(c):
        t3=(0,)
        t3=c
        print("Total Vout of CONGRESS=",sum(t3))

#e=EVM()
i=1
a=[]
b=[]
c=[]
while 1:

    print("Vout for App Pass ---->1:",end="\t\t")
    print("Vout for BJP Pass --> 2:")
    print("\nVout for Congess Pass ->3:",end="\t\t")
    print("Stop for Vouting pass ->4:")
    v=int(input("\n---->"))
    if v==1:
        a.append(v)
    if v==2:
        v=1
        b.append(v)
    if v==3:
        v=1
        c.append(v)
    if v==4:
        break

APP(a)
BJP(b)
CONGRESS(c)