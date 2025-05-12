work_time = float(input("Work time: "))
hourly_salary = float(input("Hourly salary: "))

standard_worktime = 44

overStandard_worktime = max(0, work_time - standard_worktime)

actual_pay = standard_worktime * hourly_salary + overStandard_worktime * hourly_salary * 1.5

print("Total salary:", actual_pay)
