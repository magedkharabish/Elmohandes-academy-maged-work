import numpy as np
import matplotlib.pyplot as plt
students = ['ahhmed', 'ali', 'mohamed', 'zaki']
degrees = [90, 50, 78, 98]

# Plot
plt.bar(students, degrees)

# Add labels and title
plt.xlabel('Students')
plt.ylabel('Degrees')
plt.title('Degrees of Students')

