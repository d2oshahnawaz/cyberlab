name = input("Student Name: ")

m1 = int(input("Maths Marks: "))
m2 = int(input("Python Marks: "))
m3 = int(input("ML Marks: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nResult")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Grade: First Division")
else:
    print("Grade: Second Division")
