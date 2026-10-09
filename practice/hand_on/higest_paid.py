employees = [
  ("Asha",  "Engineering", 85000),
  ("Ravi",  "Engineering", 92000),
  ("Meera", "Sales",       60000),
  ("John",  "Sales",       72000),
  ("Priya", "HR",          55000)
]
for name, department, salary in employees:
    pay=[]
    for nm,dept,sal in employees:
        if dept==department:
            pay.append(sal)
    if salary==max(pay):
        print(f"{department} -> {name} : ({salary})")