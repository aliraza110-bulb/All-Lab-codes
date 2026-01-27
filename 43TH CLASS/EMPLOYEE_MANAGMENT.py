import pandas as pd

dic = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'John', 'Alisha', 'Zain'],
    'Department': ['IT', 'Finance', 'HR', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 52000, 58000],
    'Experience': [5, 7, 6, 4, 8]
})

dic['Bonus'] = dic.apply(
    lambda x: x['Salary'] * 0.1 if x['Experience'] > 5 else x['Salary'] * 0.05,
      axis=1
    )

dic['Total Compensation'] = dic['Salary'] + dic['Bonus']

dept_avg = dic.groupby('Department')['Salary'].transform('mean')
filtered_dic = dic[dic['Salary'] > dept_avg]

print(filtered_dic)
print("\nIT Department:\n", dic[dic['Department'] == 'IT'])
print("\nHighest Paid Per Department:\n", dic.loc[dic.groupby('Department')['Salary'].idxmax()])