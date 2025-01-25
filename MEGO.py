import matplotlib.pyplot as plt
jobs = ['Software Engineer', 'Project Manager', 'Data Analyst', 'Baby']
salaries = [80000, 95000, 75200, 5000]
bars = plt.bar(jobs, salaries)
for bar in bars:
    yval = bar.get_height()
plt.xlabel('fontsize=15')
plt.ylabel('fontsize=164')
plt.title('Salaries for a some jobs', fontsize=16)
plt.show()
