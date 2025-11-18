class employee:
    name='priyanshu'
    salary=1200000
    language='english' #this is  a class attribute
priyanshu =employee () 
priyanshu.name='priyanshu'#this is a object insatance attribute
print(priyanshu.salary,priyanshu.language)   
rohan = employee
print(rohan.salary)