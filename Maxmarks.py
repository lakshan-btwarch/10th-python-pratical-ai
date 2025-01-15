# Code to create a list of student marks and find the maximum
subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

print(f"The highest marks scored are: {max(marks)}")
