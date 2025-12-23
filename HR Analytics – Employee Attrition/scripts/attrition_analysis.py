1️⃣ Load & Inspect Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hr_employee_attrition.csv")

print(df.shape)
df.head()

2️⃣ Attrition Rate
attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print(attrition_rate)


📌 Insight: ~16% of employees left the organization.

3️⃣ Attrition by Department
plt.figure()
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title("Attrition by Department")
plt.show()


📌 Insight:

Sales has the highest attrition

R&D has better retention

4️⃣ Salary vs Attrition
plt.figure()
sns.boxplot(data=df, x='Attrition', y='MonthlyIncome')
plt.title("Monthly Income vs Attrition")
plt.show()


📌 Insight:
Employees with lower monthly income are more likely to leave.

5️⃣ Experience Impact
sns.histplot(data=df, x='TotalWorkingYears', hue='Attrition', bins=20)
plt.title("Experience vs Attrition")
plt.show()


📌 Insight:
Employees with < 5 years experience show higher attrition.

6️⃣ Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
