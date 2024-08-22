import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
firstTermMarks = [55, 78, 85, 91, 66, 79, 82, 75, 89, 95, 68, 74, 92, 88, 77, 81, 69, 84, 73, 87]


print(f'The mean marks of first term {np.mean(firstTermMarks)}')
print(f'The median marks of first term {np.median(firstTermMarks)}')
print(f'The first quartile of first term {round(np.quantile(firstTermMarks,0.25))}')
print(f'The third quartile of first term {round(np.quantile(firstTermMarks,0.75))}')
print(f'The Standard Deviation first term {np.std(firstTermMarks)}')


sns.set_style('whitegrid')
# Normal Distribution Plot
sns.histplot(firstTermMarks, kde=True)
plt.title('First Term Marks Distribution')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.savefig('FirstTermNormal.jpg')

# Box Plot
sns.boxplot(firstTermMarks)
plt.title('First Term Marks Box Plot')
plt.xlabel('Marks')
plt.savefig('FirstTermBoxPlot.jpg')



secondTermMarks = [23, 65, 82, 97, 98, 79, 80, 77, 92, 98, 50, 74, 93, 89, 56, 55, 65, 81, 65, 91]

print("Second Term-----")
print(f'The mean marks of Second term {np.mean(secondTermMarks)}')
print(f'The median marks of Second term {np.median(secondTermMarks)}')
print(f'The first quartile of Second term {round(np.quantile(secondTermMarks,0.25))}')
print(f'The third quartile of Second term {round(np.quantile(secondTermMarks,0.75))}')
print(f'The Standard Deviation of Second term {np.std(secondTermMarks)}')

sns.set_style('whitegrid')
# Normal Distribution Plot
sns.histplot(secondTermMarks, kde=True)
plt.title('Second Term Marks Distribution')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.savefig('SecondTermNormal.jpg')

# Box Plot
sns.boxplot(secondTermMarks)
plt.title('Second Term Marks Box Plot')
plt.xlabel('Marks')
plt.savefig('SecondTermBoxPlot.jpg')

