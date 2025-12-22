
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/employee_attrition_data.csv')

# Attrition count
sns.countplot(x='Attrition', data=df)
plt.title('Employee Attrition Distribution')
plt.show()

# Department-wise attrition
sns.countplot(x='Department', hue='Attrition', data=df)
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# Income vs Attrition
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title('Monthly Income vs Attrition')
plt.show()
