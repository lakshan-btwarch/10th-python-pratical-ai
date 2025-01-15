# Code to plot a bar chart for class averages
import matplotlib.pyplot as plt
import pandas as pd

# Data for subjects and averages
subjects = ['SST', 'Maths', 'Science', '2nd Language', 'English', 'AI']
class_averages = {
    'Premidterm': [70, 68, 71, 75, 73, 70],
    'Midterm': [70, 69, 70, 75, 73, 74]
}

# Create the DataFrame
df = pd.DataFrame(class_averages, index=subjects)

# Plot the bar charts
plt.figure(figsize=(10, 5))

# Bar chart for premidterm
plt.subplot(1, 2, 1)
plt.bar(subjects, df['Premidterm'], color=['black', 'red', 'green', 'blue', 'yellow', 'orange'])
plt.xlabel('Subjects')
plt.ylabel('Class Average')
plt.title('Premidterm Averages')

# Bar chart for midterm
plt.subplot(1, 2, 2)
plt.bar(subjects, df['Midterm'], color=['black', 'red', 'green', 'blue', 'yellow', 'orange'])
plt.xlabel('Subjects')
plt.ylabel('Class Average')
plt.title('Midterm Averages')

plt.tight_layout()
plt.show()
