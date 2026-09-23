total_marks = 0

for i in range(1,6):
    total_marks += int(input(f"Enter {i} subject marks : "))


percentage = (total_marks/500)*100

if percentage>=80:
    Grade = "A1"
elif percentage>=70:
    Grade = "A"
elif percentage>=60:
    Grade = "B"
elif percentage>=50:
    Grade = "C"
elif percentage>=40:
    Grade = "D"
else:
    Grade = "F"

if Grade=="F":
    result = "Fail"
else:
    result = "Pass"


print("\n<<<<<<<<<<- Mark_Sheet ->>>>>>>>>>\n")
print(f"Total marks : {total_marks}")
print(f"Percentage : {percentage}")
print(f"Grade : {Grade}")
print(f"Result : {result}\n") 