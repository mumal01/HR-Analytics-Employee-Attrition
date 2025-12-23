1️⃣ Attrition Rate
SELECT 
    Attrition,
    COUNT(*) AS employee_count
FROM hr_employee_attrition
GROUP BY Attrition;

2️⃣ Attrition by Department
SELECT 
    Department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count
FROM hr_employee_attrition
GROUP BY Department;

3️⃣ Average Salary of Employees Who Left
SELECT 
    Attrition,
    AVG(MonthlyIncome) AS avg_monthly_income
FROM hr_employee_attrition
GROUP BY Attrition;

4️⃣ Experience vs Attrition
SELECT 
    CASE 
        WHEN TotalWorkingYears < 5 THEN '0-5 Years'
        WHEN TotalWorkingYears BETWEEN 5 AND 10 THEN '5-10 Years'
        ELSE '10+ Years'
    END AS experience_group,
    COUNT(*) AS employees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_count
FROM hr_employee_attrition
GROUP BY experience_group;
