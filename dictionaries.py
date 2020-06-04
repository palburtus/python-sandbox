employee = {'name' : 'John', 'years': 10, 'age' : 32}
employee['number'] = 10001
print(employee)
print("Age is ", employee['age'])
del employee['years']
print(employee)

print(list(employee))
print(sorted(employee))
print('namex    ' not in employee)
print('John' not in employee)




newEmployee = dict(name='joe', sex='male', age=33)
print(newEmployee)

for k,v in newEmployee.items():
    print("key:", k , "value:", v)