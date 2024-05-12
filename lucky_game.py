import random
name=input("Enter Your Name:")
lucky_Num=random.randint(1,100)
print("\n\t\t\t[------ONLY ENTER 1 TO 100------]")
for a in range(5):
    print("\n\t\t\t\t",a+1,".Enter Number:",end="")
    you_num=int(input())

    if lucky_Num==you_num:
        break
if lucky_Num==you_num:
    print("\n\n\t\t\t\t<<<Congratulation",name,"Your Lucky>>>->",you_num,":)")
else:
    print("\n\n\t\t\t\tBad luck",name," Number is->",lucky_Num,":(")
    print("\t\t\t\tTry Again")