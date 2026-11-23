name = input("Enter student name: ")

m1 = int(input("Enter Tamil marks: "))
m2 = int(input("Enter English marks: "))
m3 = int(input("Enter Maths marks: "))

total = m1 + m2 + m3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
