class Emp:
    def __init__(self,l,id,name,birth,age,join,gender,address,contact,que,exp,lwp,depar,salary):
        
        self.l=l
        self.id=id
        self.name=name
        self.birth=birth
        self.age=age
        self.join=join
        self.gender=gender
        self.address=address
        self.contact=contact
        self.que=que
        self.exp=exp
        self.lwp=lwp
        self.depar=depar
        self.salary=salary
    def emp_inf(self):
        l.append(self.id)
        l.append(self.name)
        l.append(self.birth)
        l.append(self.age)
        l.append(self.join)
        l.append(self.gender)
        l.append(self.address)
        l.append(self.contact)
        l.append(self.que)
        l.append(self.exp)
        l.append(self.lwp)
        l.append(self.depar)
        l.append(self.salary)
    

    def show(self):
        print(self.l)
l=[]
id=int(input("* Employee Id:"))
name=input("\n* Employee Name:")
birth=input("\n* Employee Date of Birth:")
age=int(input("\n* Employee Age:"))
join=input("\n* Employee Joining Date:")
gender=int(input("\n* Press [1] Male Press [2] Female:"))
address=input("\n* Employee Address:")
contact_no=int(input("\n* Contact No."))
qualification=input("\n* Qualification:")
exp=input("\n* Experience:")
experience=exp+" Year"
last_work_place=input("\n* Last Work Place:")
department=input("\n* Department:")
salary=int(input("\n* Salary:"))
if gender==1:
    gender="Male"
if gender==2:
    gender="Female"
print("EmpId  Name  Date of Birth  Age  Join Date  Gender  Address  Contact  Qualification  Experience  Last Work  Salary")
ob1=Emp(l,id,name,birth,age,join,gender,address,contact_no,qualification,experience,last_work_place,department,salary)
ob1.emp_inf()
ob1.show()