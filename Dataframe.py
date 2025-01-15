# Code to create a DataFrame of class averages
import pandas as pd

# Data for subjects and averages
subjects = ['SST', 'Maths', 'Science', '2nd Language', 'English', 'AI']
class_averages = {
    'Premidterm': [70, 68, 71, 75, 73, 70],
    'Midterm': [70, 69, 70, 75, 73, 74]
}

# Create the DataFrame
df = pd.DataFrame(class_averages, index=subjects)

print("Class Averages DataFrame:")
print(df)
