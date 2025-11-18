class employee:
    salary=1200000
    language='english' #this is  a class attribute
priyanshu =employee () 
priyanshu.language='python'#this is a object insatance attribute
print(priyanshu.salary,priyanshu.language)   
rohan = employee
print(rohan.salary)