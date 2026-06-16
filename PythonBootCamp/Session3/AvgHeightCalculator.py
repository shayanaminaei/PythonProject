students_heights = input("Enter a list of students heights: ").strip()
for n in range (0,len(students_heights)):
    students_heights[n] = float(students_heights[n])
print(students_heights)
#--------------------------------
Sum_students_heights = sum(students_heights)
Avg_height = (Sum_students_heights/len(students_heights))
print(f"""There were {len(students_heights)} students height.
The average height is {Avg_height:.2f}.""")
