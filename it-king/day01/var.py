# Author: Peter
name = "Peter"
print("hello world ", name)

name = input("name: ")
age = int(input("age: "))
print(type(age), type(str(age)))
job = input("job: ")
salary = input("salary: ")

info = ''' 
--------------- info of %s
Name: %s
Age: %s
Job: %s
Salary: %s
''' % (name, name, age, job, salary)

print(info)



info2 = '''
--------------- info2 of {_name}
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
'''.format(_name=name, _age=age, _job=job, _salary=salary)
print(info2)

info3 = '''
--------------- info3 of {0}
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
'''.format(name, age, job, salary)
print(info3)


